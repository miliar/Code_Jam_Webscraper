#include<stdio.h>
#include<iostream>
#include<cstring>
#include<string>
#include<vector>
#include<algorithm>
using namespace std;

#define MAXN 600
#define MOD 10000

int ncases;
char inp[MAXN];
int n;
char goal[] = "welcome to code jam";
int K = 19;

int numways[MAXN][20];

int main(){
  scanf("%d\n", &ncases);
  for(int ncase = 1; ncase <= ncases; ncase++){
    printf("Case #%d: ", ncase);
    cin.getline(inp, MAXN);

    n = strlen(inp);
    memset(numways, 0, sizeof(numways));
    numways[0][0] = 1;
    for(int i = 0; i < n; i++){
      for(int j = 0; j < K; j++){
        if (inp[i] == goal[j]) {
          for(int k = 0; k <= i; k++){
            numways[i+1][j+1] += numways[k][j];
            numways[i+1][j+1] %= MOD;
          }
        }
      }
    }
    int ans = 0;
    for(int i = 0; i <= n; i++){
      ans = (ans + numways[i][K])%MOD;
    }
    printf("%04d\n", ans);
  }
}
