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
#define REP(i,a,n) for(int i=a; i<(int)(n); i++)
#define rep(i,n) REP(i,0,n)
#define FOR(it,c) for(__typeof((c).begin()) it=(c).begin(); it!=(c).end(); ++it)
#define ALLOF(c) (c).begin(), (c).end()
using namespace std;

vector<int> B, O;
vector<char> R;
vector<int> P;

int solve(){
  int Bnow = 1, Onow = 1;
  int Bidx = 0, Oidx = 0;
  int t = 1;
  int idx = 0;
  
  while(true){
    bool flg = false;
    //B
    if(R[idx]=='B' && P[idx]==Bnow){
      idx++;
      Bidx++;
      flg=true;
    }
    else if(B[Bidx]<Bnow) Bnow--;
    else if(B[Bidx]>Bnow) Bnow++;
    
    //O
    if(!flg && R[idx]=='O' && P[idx]==Onow){
      idx++;
      Oidx++;
    }
    else if(O[Oidx]<Onow) Onow--;
    else if(O[Oidx]>Onow) Onow++;
    
    if(idx==P.size()) return t;
    t++;
  }
}


int main(){
  int T, N, p;
  char r;
  cin >> T;
  rep(t,T){
    cin >> N;
    B.clear();
    O.clear();
    R.clear();
    P.clear();
    rep(i,N){
      cin >> r >> p;
      R.push_back(r);
      P.push_back(p);
      if(r=='B') B.push_back(p);
      else O.push_back(p);
    }
    B.push_back(-1);
    O.push_back(-1);
    cout << "Case #" << t+1 << ": " << solve() << endl;
  }
  return 0;
}
