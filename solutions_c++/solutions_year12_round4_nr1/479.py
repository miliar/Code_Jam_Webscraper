#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include<cassert>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>
#include<bitset>

#define REP(i,b,n) for(int i=b;i<(int)n;i++)
#define rep(i,n)   REP(i,0,n)
#define ALL(C)     (C).begin(),(C).end()
#define FOR(it,o)  for(__typeof((o).begin()) it=(o).begin(); it!=(o).end(); ++it)
#define dbg(x) cerr << #x << " = " << (x) << endl


typedef long long ll;

using namespace std;

const int N = 10001;
int dp[N];

bool solve(vector<int> &D, vector<int> &L){
  int n = D.size();
  rep(i, N)dp[i] = -1;
  dp[0] = D[0];
  rep(i, n){
    int l1 = dp[i], d1 = D[i];
    if(l1 == -1)return false;
    REP(j, i+1, n){
      int l2 = L[j];
      int d2 = D[j];
      if(l1 >= d2 - d1){
	dp[j] = max(dp[j], min(d2-d1, l2));
      }
    }
  }
  return true;
}

int main(){
  int T;
  cin >> T;
  rep(tc, T){
    cout <<"Case #" << tc+1<<": "<<flush;
    int n;
    cin >> n;
    vector<int> D(n), L(n);
    rep(i, n){
      cin >> D[i] >> L[i];
    }
    int d;
    cin >> d;
    D.push_back(d);
    L.push_back(0);
    
    if(solve(D, L))cout<<"YES" << endl;
    else cout << "NO" << endl;
  }
  
  
  return 0;
}
