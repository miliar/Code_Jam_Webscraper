#include <cstdio>
#include <cstdlib>

using namespace std;

int v[50], n;

int resolve(){
  int x = 0;
  for (int val = 1; val < n; val++){
    int i;
    for (i = val; i <= n && val < v[i]; i++);
    x += i-val;
    //printf("%d %d -> %d\n", i, val, x);
    int aux = v[i];
    for (int j = i-1; j >= val; j--)
      v[j+1] = v[j];
    v[val] = aux;

    /*    for (int p = 1; p <= n;p++){
      printf("%d ", v[p]);
    }
    printf("\n");*/
  }
  return x;
}

int main(){
  int t;
  char tab[50][50];

  scanf("%d", &t);
  
  for (int ka = 1; ka <= t; ka ++){
    scanf("%d", &n);
    for (int i = 0; i < n; i++){
      scanf("%s", &tab[i]);
      int j;
      for (j = n-1; j >= 0; j--){
	if (tab[i][j] == '1')
	  break;
      }
      v[i+1] = j+1;
    }
    /*for (int p = 1; p <= n;p++){
      printf("%d ", v[p]);
    }
    printf("\n");*/
    int ans = resolve();

    printf("Case #%d: %d\n", ka, ans);
  } 

  return 0;
}
