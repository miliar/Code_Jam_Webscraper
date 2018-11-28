#include <stdio.h>
#include <iostream>
#include <algorithm>
#define MAX 50
using namespace std;

int a[MAX];
int n;

void init(){
  int i, j;
  char k;
  cin >> n;
  for (i = 0; i < n; i++){
    a[i] = 0;
    for (j = 0; j < n; j++){
      cin >> k;
      if (k == '1') {
        a[i] = j;
      }
    }
  }
}

void calc(){
  int ans = 0;
  int i, j, k, t;

  for (i = 0; i < n; i++){
    for (j = i; j < n; j++)
      if (a[j] <= i) break;

    ans += (j - i);
    t = a[j];
    for (k = j; k > i; k--) a[k] = a[k - 1];
    a[i] = t;
  }

  cout << ans << endl;
}

int main(){
  freopen("A.txt", "r", stdin);
  freopen("fdout.txt", "w", stdout);
  int T, i;
  cin >> T;
  for (i = 1; i <= T; i++){
    init();
    printf("Case #%d: ", i);
    calc();
  }
  return 0;
}