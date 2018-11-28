#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <queue>
#include <list>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>
using namespace std;
#define REP(i,a,n) for(int i=(a); i<(int)(n); i++)
#define rep(i,n) REP(i,0,n)
#define FOR(it,c) for(__typeof((c).begin()) it=(c).begin(); it!=(c).end(); ++it)
#define ALLOF(c) (c).begin(), (c).end()
typedef long long ll;

vector<int> C;

string solve(){
  sort(ALLOF(C));
  ll sum = 0;
  rep(i,C.size()) sum ^= C[i];
  if(sum != 0) return "NO";

  /*
  int maxsum = -1;
  int sean, patrick;
  REP(i,1,C.size()){
    sean = 0;
    patrick = 0;
    sum = 0;
    rep(j,C.size()){
      if(j<i){
        patrick ^= C[j];
      }else{
        sean ^= C[j];
        sum += C[j];
      }
    }
    //cout << sean << " " << patrick << endl;
    if(sean==patrick) maxsum = max(maxsum, sum);
  }
  if(maxsum==-1) return "NO";
  */
  ll maxsum = 0;
  REP(i,1,C.size()){ maxsum += C[i]; }

  stringstream ss("");
  ss << maxsum;
  return ss.str();
}

int main(){
  int T, N, d;
  cin >> T;
  rep(t,T){
    C.clear();
    cin >> N;
    rep(i,N){
      cin >> d;
      C.push_back(d);
    }
    cout << "Case #" << t+1 << ": " << solve() << endl;
  }
  return 0;
}
