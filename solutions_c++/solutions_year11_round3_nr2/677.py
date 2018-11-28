#if 0
#!/bin/bash
src=$0;
obj=${src%.*};
echo "g++ -O2 -o $obj $src";
g++ -O2 -o $obj $src;
./$obj <  > "out.txt";
exit;
#endif
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

template<class T> std::ostream &operator<<(std::ostream &o,const std::vector<T> &v)
{ o << "["; for(std::size_t i=0;i<v.size();i++) o << v[i] << (i < v.size()-1 ? ",":""); return o << "]"; }
template<class T,class U> std::ostream &operator<<(std::ostream &o,const std::pair<T,U> &v)
{ return o << v.first << ":" << v.second; }
template<class T,class U> std::ostream &operator<<(std::ostream &o,const std::map<T,U> &v)
{ o << "{"; typename std::map<T,U>::const_iterator i=v.begin(),j=i;++j;for(;i!=v.end();++i,++j) o << *i << (j!=v.end()? ",":""); return o << "}"; }
template<class T> std::ostream &operator<<(std::ostream &o,const std::set<T> &v)
{ o << "{"; typename std::set<T>::const_iterator i=v.begin(),j=i;++j;for(;i!=v.end();++i,++j) o << *i << (j!=v.end()? ",":""); return o << "}"; }



LLI solve(LLI L, LLI t, LLI N, vector<LLI> &v){
  LLI res = 0;
  while(t > 0){
    if(v.size() == 0) break;
    LLI first_t = v[0] * 2;
    if(first_t > t){
      v[0] = (first_t - t) / 2;
      res += t;
      t = 0;
    }else{
      v.erase(v.begin());
      res += first_t;
      t -= first_t;
    }
  }
  sort(v.begin(),v.end(),greater<LLI>());
  REP(i,min(L,(LLI)SZ(v))){
    res += v[i];
  }
  for(int i = L; i < SZ(v); i++){
    res += 2*v[i];
  }
  return res;
}


int main(int argc, char *argv[]){
  ios::sync_with_stdio(false);

  int T;
  cin >> T;
  for(int i = 0; i < T; i++){
    LLI res = 0;

    LLI L,t,N,C;
    vector<LLI> v;
    cin >> L >> t >> N >> C;
    REP(j,C){
      LLI k;
      cin >> k;
      v.push_back(k);
    }
    vector<LLI> v2;
    REP(j,N){
      v2.push_back(v[j%C]);
    }
    res = solve(L,t,N,v2);
    cout << "Case #" << i + 1 << ": " << res << endl;
  }

  return 0;
}
