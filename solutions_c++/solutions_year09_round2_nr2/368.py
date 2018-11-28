#include <cstdio>
#include <cstdlib>
#include <string>

using namespace std;

int val[10];

void calculaVal(long long n){
  for (int i = 0; i < 10; i++)
    val[i] = 0;

  while (n > 0){
    val[n%10]++;
    n /= 10;
  }
}

bool checa(long long n){
  int at[10];
  for (int i = 0; i < 10; i++)
    at[i] = 0;

  while (n > 0){
    at[n%10]++;
    n /= 10;
  }
  
  for (int i = 1; i < 10; i++){
    if (at[i] != val[i])
      return false;
  }
  return true;
}

void inverte(char n[], int sz){
  int i = 0, j = sz;
  char t;

  while (i < j){
    t = n[i];
    n[i] = n[j];
    n[j] = t;
    i++;
    j--;
  }
}

bool achaProx(char n[], int t){
  if (t == 0) return false;
  if (achaProx(n, t-1)) return true;

  int p = 0;
  while (t >= p && n[p] <= n[t]) p++;
  //printf("%d %d .. %c %c\n", p, t, n[p], n[t]);
  if (t <= p) return false;
  if (n[t] < n[p]){
    char temp = n[t];
    n[t] = n[p];
    n[p] = temp;
    inverte(n, t-1);
    return true;
  }
  return false;
}

int main(){
  int t, n;

  scanf("%d", &t);

  for (int ka = 1; ka <= t; ka++){
    char n[25];
    scanf("%s",&n);

    inverte(n, strlen(n)-1);
    if (!achaProx(n, strlen(n)-1)){
      int sz = strlen(n);

      int p = 0;
      while (n[p] == '0') p++;

      n[sz] = n[p];
      n[p] = '0';
      n[sz+1] = '\0';
      inverte(n, sz-1);
    }
    inverte(n, strlen(n)-1);

    printf("Case #%d: %s\n", ka, n);
  }

  return 0;
}
