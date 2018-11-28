#include<iostream>
#include<string>
#include<algorithm>
#include<vector>
#include<map>
#include<set>
#include<cstdlib>
#include<cstdio>
#include<cmath>
#include<sstream>
#include<cassert>
#include<queue>
#include<stack>
#include<bitset>
#include<cstring>

#define REP(i,b,n) for(int i=b;i<(int)n;i++)
#define rep(i,n)   REP(i,0,n)
#define ALL(C)     (C).begin(),(C).end()
#define FOR(it,o)  for(__typeof((o).begin()) it=(o).begin(); it!=(o).end(); ++it)

using namespace std;
typedef long long lli;
typedef vector<int> vint;
typedef pair<int, int> pii;
const double EPS = 0.00000001;
const int INF = 1000000000;
template<class T> void pp(T t, int n){
  rep(i, n){
    cout << t[i] << ' ';
  }
  cout << endl;
}

const int N = 1000;

char c[N];
int pos[N];

int solve(int n){
  int lastPos[2], lastT[2];
  rep(i, 2){
    lastPos[i] = 1;
    lastT[i] = 0;
  }
  int now = 0;
  rep(i, n){
    int id = 0;
    if(c[i] == 'B')id = 1;
    now = max(now+1, abs(lastPos[id] - pos[i]) + lastT[id] + 1);
    lastT[id] = now;
    lastPos[id] = pos[i];
  }
  return now;
}

int main(){
  int T;
  cin >> T;
  rep(tc, T){
    int n;
    cin >> n;
    rep(i, n)cin >> c[i] >> pos[i];
    cout << "Case #" << tc+1 << ": " << solve(n) << endl;
  }
  return 0;
}
