#include<iostream>
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
typedef long double LD;

#define PI 3.14159265358979323
#define EE 2.71828182845
#define EPS 10e-10
#define INF 10000000

inline LL MAX(LL a, LL b){ return a < b ? b : a;}
inline LL MIN(LL a, LL b){ return a < b ? a : b;}

#define FOR(i,n)      for(int i=0;i<(n);i++)
#define FORD(i,n)     for(int i=(n)-1;i>=0;i--)

#define MP make_pair
#define PB push_back

int i2s(string s){
  istringstream is(s);
  int v;
  is >> v;
  return v;
}

string s2i(int i){
  ostringstream os;
  os << i;
  return os.str();
}

set< PLL > S;

int main(){
  int TT;
  cin >> TT;
  S.clear();
  FOR(tt,TT){
    S.clear();
    int A,B;
    cin >> A >> B;
    for(int i=A;i<B;i++){
      string s = s2i(i);
      FOR(j,s.length()-1){
	string ns = s.substr(j+1) + s.substr(0,j+1);
	if ( i2s(ns) > i && i2s(ns) <= B ) S.insert( MP(i,i2s(ns)));
      }
    }
    cout << "Case #" << (tt+1) << ": " << S.size() << endl;
  }
}
