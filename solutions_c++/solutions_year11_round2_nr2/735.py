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
const lli INF = 1000000000000ll;
template<class T> void pp(T t, int n){
  rep(i, n){
    cout << t[i] << ' ';
  }
  cout << endl;
}

const lli maxi =  400000000;


vector<lli> pos;
lli n, D;

bool canPut(int t){
  lli leftLimit = -INF;
  vector<lli> Q = pos;
  while(!Q.empty()){
    if(leftLimit == Q.back()){
      leftLimit += D;
    }
    else if(leftLimit < Q.back()){
      leftLimit = max(leftLimit, Q.back() - t) + D;
    }
    else {
      if(Q.back() + t < leftLimit)return false;
      leftLimit = min(Q.back() + t, leftLimit) + D;
    }
    Q.pop_back();
  }
  return true;
}

int main(){
  int T;
  cin >> T;
  rep(tc, T){
    cout << "Case #" << tc+1 << ": ";
    cout << flush;
    cin >> n >> D;
    D *= 2;
    pos.clear();
    rep(i, n){
      lli p, num;
      cin >> p >> num;
      rep(j, num)pos.push_back(p*2);
    }
    sort(ALL(pos));
    reverse(ALL(pos));
    lli right = maxi, left = 0;
    while(1){
      lli mid = (right+ left)/2;
      if(canPut(mid)){
        right = mid;
      }
      else {
        left = mid;
      }
      if(right <= left+1){
        lli ans = max(right, left);
        if(canPut(min(left, right))){
          ans =min(right, left);
        }
        printf("%.7Lf\n", (long double)ans/ 2.0);
        break;
      }
    }
  }
  return 0;
}
