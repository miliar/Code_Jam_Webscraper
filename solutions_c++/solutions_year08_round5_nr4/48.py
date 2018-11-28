#include <algorithm>
#include <bitset>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <deque>
#include <iostream>
#include <map>
#include <set>
#include <sstream>
#include <vector>
using namespace std;
#define FOR(i,n) for(int i=0;i<n;i++)
#define FORI(i,v) FOR(i,(int)v.size())
#define BEND(v) v.begin(),v.end()
#define dump(x) cerr << #x << " = " << (x) << endl;
typedef long long ll; typedef long double ld;

const int MOD = 10007;
int cas = 0;
int H,W,R;
int rr[16],rc[16];
int dp[128][128];
int dodp(int r, int c) {
  if (r >= H || c >= W) return 0;
  int& ans = dp[r][c];
  if (ans != -1) return ans;
  if (r == H-1 && c == W-1) {
    return ans = 1;
  } else {
    FOR(i,R) if (rr[i] == r && rc[i] == c) return ans = 0;

    return ans = (dodp(r+2,c+1) + dodp(r+1,c+2)) % MOD;
  }
}
void doit() {
  scanf("%d%d%d",&H,&W,&R);

  FOR(i,R) {
    scanf("%d%d",&rr[i],&rc[i]);
    rr[i]--;
    rc[i]--;
  }

  memset(dp,-1,sizeof(dp));

  printf("Case #%d: %d\n",++cas,dodp(0,0));
}
int T;
int main() {
scanf("%d",&T);
FOR(i,T)doit();
}
