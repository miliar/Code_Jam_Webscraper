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

int gcd(int a, int b){return (b==0?a:gcd(b,a%b));}
int lcm(int a, int b){return a/gcd(a,b)*b;}

int N, L, H;
vector<int> freq;
int ret;

void solve(){
  ret = -1;
  
  REP(i,L,H+1){
    bool flg = true;
    rep(j,freq.size()){
      if(i>freq[j]){
        if(i%freq[j]!=0){
          flg = false;
        }
      }else{
        if(freq[j]%i!=0){
          flg = false;
        }
      }
      if(!flg) break;
    }
    if(flg){
      ret = i;
      return;
    }
  }
}


int main(){
  int T;
  cin >> T;
  rep(t,T){
    cin >> N >> L >> H;
    freq.clear();
    rep(i,N){
      int f;
      cin >> f;
      freq.push_back(f);
    }

    solve();
    
    cout << "Case #" << t+1 << ": ";
    if(ret==-1) cout << "NO" << endl;
    else cout << ret << endl;
  }
  return 0;
}
