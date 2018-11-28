#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <stack>
#include <vector>
#include <cmath>
#include <list>
#include <sstream>
#include <algorithm>

using namespace std;

typedef pair<int,int> PII;
typedef long long LL;
typedef vector<int> VI;
typedef pair<LL,LL> PLL;
typedef vector<pair<int,int> > VPII;
typedef vector<LL> VLL;
typedef vector<vector<int> > VVI;
typedef vector<string> VS;

#define PI 3.14159265358979323
#define EE 2.71828182845
#define EPS 10e-11
#define INF 1000000000000ll

inline LL MAX(LL a, LL b){ return a < b ? b : a;}
inline LL MIN(LL a, LL b){ return a < b ? a : b;}

#define FOR(i,n)      for(int i=0;i<(n);i++)
#define FORD(i,n)     for(int i=(n)-1;i>=0;i--)

#define MP make_pair
#define PB push_back

int TT;
LL ans;
int symbols;
set<char> S;
string s;
VI digs;
map<char,int> M;
int O[65];

int main(){
  cin >> TT;
  FOR(tt,TT){
    cin >> s;
    S.clear();
    M.clear();
    memset(O,0,sizeof(O));
    FOR(i,s.length()) S.insert(s[i]);
    symbols = MAX(2,S.size());
    M[s[0]] = 1; 
    O[1] = 1;
    FOR(i,s.length()-1){
      int p = i+1;
      if (M.find(s[p]) == M.end()){
        int b = 0;
        while (O[b] == 1) b++;
        M[s[p]] = b;
        O[b] = 1;
      }
    }
    ans = 0;

    //cout << symbols << endl;
    LL t = 1;
    FOR(i,s.length()){
      ans+= M[s[s.length()-i-1]]*t;
      //ans*=symbols;
      t*=symbols;
    }
    cout << "Case #" << (tt+1) << ": "  << ans << endl;
  }
}


