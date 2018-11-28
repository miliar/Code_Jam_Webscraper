#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>
#include <limits>
#include <fstream>

using namespace std;

inline int toInt(string s) {int v; istringstream sin(s);sin>>v;return v;}
template<class T> inline string toString(T x) {ostringstream sout;sout<<x;return sout.str();}

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef pair<int, int> PII;
typedef long long LLI;

#define ALL(a)  (a).begin(),(a).end()
#define RALL(a) (a).rbegin(), (a).rend()
#define PB push_back
#define MP make_pair
#define SZ(a) int((a).size())
#define EACH(i,c) for(typeof((c).begin()) i=(c).begin(); i!=(c).end(); ++i)
#define EXIST(s,e) ((s).find(e)!=(s).end())
#define SORT(c) sort((c).begin(),(c).end())

#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n)  FOR(i,0,n)

const double EPS = 1e-9;
const double PI  = acos(-1.0);

#define CLR(a) memset((a), 0 ,sizeof(a))

struct DDMY{ ostringstream o; template<class T>DDMY& operator,(const T &t){o<<t<<",";return *this;} string operator*(){ return o.str().substr(0,o.str().size()-1); } };
#define debug(args...) cout<<"("#args")=("<< *(DDMY(),args)<<") (L"<<__LINE__<<")"<<endl


bool check(LLI t, LLI D, const vector<LLI> &pt){
  LLI minp = pt[0] - t;
  FOR(i,1,SZ(pt)){
    //debug(pt[i],pt[i]+t,pt[i]-t,minp+D);
    if(minp + D <= pt[i] + t){
      minp = max(minp+D,pt[i]-t);
    }else{
      return false;
    }
  }
  return true;
}


long double solve(LLI D, vector<LLI> pt){
  SORT(pt);
  LLI mint = 0;
  LLI maxt = (pt.size()*D+2) * 100;
  LLI t = 0,t_rem=0;
  while(mint < maxt){
    t = mint + ((maxt - mint) / 2);
    if(t_rem == t) break;
    //debug(t,mint,maxt);
    if(check(t,D,pt)){
      maxt = t;
      t_rem = t;
    }else{
      mint = t+1;
    }
  }
  return mint;
}


int main(int argc, char *argv[]){
  ios::sync_with_stdio(false);

  int T;
  cin >> T;
  for(int i = 0; i < T; i++){
    long double res = 0.0;
    vector<LLI> pt;
    LLI C,D;
    cin >> C >> D;
    REP(j,C){
      LLI P,V;
      cin >> P >> V;
      REP(k,V){
        pt.push_back(2*P);
      }
    }
    res = solve(2*D,pt);
    cout << "Case #" << i + 1 << ": " << (res/2) << endl;
  }

  return 0;
}
