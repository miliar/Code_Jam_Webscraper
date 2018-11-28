#include <iostream>
#include <fstream>

using namespace std;

int qwe(int y){
  int x = y;
  int i = 1;
  while (x / i > 0) i *= 10;
  i = i / 10;
  int j;
  j = x / i;
  x = x % i;
  x = x * 10 + j;
  while (x / i == 0){
    j = x / i;
    x = x % i;
    x = x * 10 + j;    
  }
  return x;
}

int next[10000010];
bool used[10000010];
int st[2000010];
  

int main(){
  
  freopen("CC.in", "r", stdin);
  freopen("CC.out", "w", stdout);
  
  for (int i = 1; i < 2000001; i++){
    if (next[i] == 0){
      int j = i;
      next[i] = qwe(j);
      while (next[j] != i){
        j = next[j];
        next[j] = qwe(j);
      }
    }
  }
  
  int sz;
  
  int l, r, k, cnt, n;
  scanf("%d\n", &n);
  for (int ii = 0; ii < n; ii++){
  scanf("%d%d\n", &l, &r);
  cnt = 0;
  sz = 0;
  for (int i = l; i <= r; i++){
    if (used[i] == false){
      int j = i;
      st[sz] = i;
      sz++;
      used[i] = true;
      k = 1;
      while (next[j] != i){
        j = next[j];
        st[sz] = j;
        if ((j >= l) && (j <= r)) {
          k++;
          sz++;
          used[j] = true;
        }
      }
      cnt = cnt + (k * (k - 1) / 2);
    }
  }
  for (int j = 1; j < sz; j++) used[st[j]] = false;
  cout << "Case #" << ii + 1 << ": " << cnt << "\n";
  }
  return 0;
}