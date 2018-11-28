#include<iostream>
#include<vector>
#include<algorithm>
#include<cstdio>
#define INF (999999999)

using namespace std;

//int dp[20][1000005][2];
int mem[2][3000005][2];
vector <int> list;
int fxor;
/*int solve(int pos, int val, int empty) {
  if(pos >= list.size())
    if((fxor^val) == val && empty == 1)
      return 0;
    else
      return -INF;
  int &ret = dp[pos][val][empty];
  if(ret != -1)
    return ret;
  ret = 0;
  ret = max(solve(pos+1, val^list[pos], 1), list[pos]+ solve(pos+1,val, empty));
  return ret;
}*/
int main() {
  int T;
  scanf("%d",&T);
  for(int cas =1; cas<=T; cas++){
    int N;
    scanf("%d",&N);
    //memset(dp,0xff,sizeof(dp));
    //memset(mem,0xff,sizeof(mem));
    list.clear();
    list.resize(N);
    fxor = 0;
    int maxc = 0;
    for(int i=0;i<N;i++) {
      scanf("%d", &list[i]);
      maxc = max(maxc, list[i]);
      fxor ^=list[i];
    }
    maxc++;
    maxc*=2;
    for(int i =0;i<maxc;i++) {
      if((fxor^i) == i) {
        mem[1][i][1] = 0;
      } else {
        mem[1][i][1] = -INF;
      }
      mem[1][i][0] = -INF;
      mem[0][i][0] = -INF;
      mem[0][i][1] = -INF;
    }

    int i;
    int flag = 0;
    for(i = N-1; i>=0;i--) {
      for(int j =0; j< maxc ;j++) {
        if(flag%2 ==0 ) {
          mem[0][j][0] = max(mem[1][j^list[i]][1], list[i] + mem[1][j][0]);
          mem[0][j][1] = max(mem[1][j^list[i]][1], list[i] + mem[1][j][1]);
          //cout<<"0 : "<<mem[0][j][1]<<" "<<mem[0][j][0]<<endl;
        } else {
          mem[1][j][0] = max(mem[0][j^list[i]][1], list[i] + mem[0][j][0]);
          mem[1][j][1] = max(mem[0][j^list[i]][1], list[i] + mem[0][j][1]);
          //cout<<"1 : "<<mem[1][j][1]<<" "<<mem[1][j][0]<<endl;
        }
      }
      flag++;
    }
    flag--;
    int ret;
    if(flag%2==0)
      ret = mem[0][0][0];
    else
      ret = mem[1][0][0];
    if (ret < 0)
      printf("Case #%d: NO\n", cas);
    else
      printf("Case #%d: %d\n", cas, ret);
  }
}
