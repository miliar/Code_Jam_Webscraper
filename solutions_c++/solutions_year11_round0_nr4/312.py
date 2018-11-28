#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
using namespace std;

#define maxn 1010

int T;
int n;
int a[maxn];

int main() {

  freopen("D-large.in", "rt", stdin);
  freopen("D-large.out", "wt", stdout);
  
  scanf("%d", &T);
  for(int cT = 0; cT < T; cT++) {
    
    scanf("%d", &n);
    for(int i = 0; i < n; i++)
      scanf("%d", &a[i]);
    int cnt = 0;
    for(int i = 0; i < n; i++)
      if (a[i]-1 != i) cnt ++;
    printf("Case #%d: %d\n", cT+1, cnt);
    
  }
  
  return 0;

}
