#define _CRT_SECURE_NO_DEPRECATE
#include <cstdio>
#include <iostream>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <cassert>
#include <vector>
#include <string>
#include <set>
#include <map>

using namespace std;

const int MAX = 256;

int n, N;
int we[MAX][MAX];
int need[MAX][MAX];

bool eq(const int & a, const int & b){
  return (a<0) || (b<0) || (a==b);
}

int main(){
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  int tn;
  scanf("%d", &tn);
  for (int t=1; t<=tn; t++){
    printf("Case #%d: ", t);
    scanf("%d", &n);
    for (int i=1; i<=n; i++){
      for (int j=1; j<=i; j++){
        scanf("%d", &we[i-j+1][j]);
      }
    }
    for (int i=n-1; i>=1; i--){
      for (int j=1; j<=i; j++){
        scanf("%d", &we[n-j+1][n-i+j]);
      }
    }
    for (N=n; ; N++){
      for (int i=1; i+n<=N+1; i++){
        for (int j=1; j+n<=N+1; j++){
          memset(need, 0xFF, sizeof(need));
          for (int r=1; r<=n; r++){
            for (int c=1; c<=n; c++){
              need[i+r-1][j+c-1] = we[r][c];
            }
          }
          bool ok = true;
          for (int r=i; r<i+n; r++){
            for (int c=j; c<j+n; c++){
              ok &= eq(need[r][c], need[c][r]);
              ok &= eq(need[r][c], need[N+1-c][N+1-r]);
              if (!ok) break;
            }
          }
          if (ok) goto out;
        }
      }
    }
out:
    printf("%d\n", N*N - n*n);
    fflush(stdout);
  }
  return 0;
}
