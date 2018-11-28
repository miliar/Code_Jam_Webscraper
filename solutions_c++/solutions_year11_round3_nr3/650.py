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

long long gcd(long long m, long long n){
  long long temp;
  while(m % n != 0){
    temp = n;
    n = m % n;
    m = temp;
  }
  return n;
}

long long lcm (long long m, long long n){
  return m * n / gcd(m,n);
}

template<class T> std::ostream &operator<<(std::ostream &o,const std::vector<T> &v)
{ o << "["; for(std::size_t i=0;i<v.size();i++) o << v[i] << (i < v.size()-1 ? ",":""); return o << "]"; }
template<class T,class U> std::ostream &operator<<(std::ostream &o,const std::pair<T,U> &v)
{ return o << v.first << ":" << v.second; }
template<class T,class U> std::ostream &operator<<(std::ostream &o,const std::map<T,U> &v)
{ o << "{"; typename std::map<T,U>::const_iterator i=v.begin(),j=i;++j;for(;i!=v.end();++i,++j) o << *i << (j!=v.end()? ",":""); return o << "}"; }
template<class T> std::ostream &operator<<(std::ostream &o,const std::set<T> &v)
{ o << "{"; typename std::set<T>::const_iterator i=v.begin(),j=i;++j;for(;i!=v.end();++i,++j) o << *i << (j!=v.end()? ",":""); return o << "}"; }


LLI solve(LLI L, LLI H, vector<LLI> &v){
  /*
  debug(L,H,v);
  while(1){
    LLI res = v[0];
    vector<LLI> v2;
    bool flg = true;
    for(int i=1;i < SZ(v); i++){
      LLI lcmn = lcm(res,v[i]);
      if(lcmn > H){
        v2.push_back(v[i]);
      }else{
        res = lcmn;
        flg = false;
      }
    }
    v2.push_back(res);
    v = v2;
    if(flg) break;
  }
  REP(i,SZ(v)){
    if(v[i] < L && v[i] > H) continue;
    REP(j,SZ(v)){
      if(v[i] > v[j] && v[i] % v[j] != 0){
        goto fail;
      }else if(v[i] < v[j] && v[j] % v[i] != 0){
        goto fail;
      }
    }
    return v[i];
  fail:;
  }
  return -1;
  */
}

LLI solve2(LLI L, LLI H, vector<LLI> &v){
  for(LLI i = L; i <= H; i++){
    REP(j,SZ(v)){
      if(v[j] > i){
        if(v[j] % i != 0){
          goto fail;
        }
      }else{
        if(i % v[j] != 0){
          goto fail;
        }
      }
    }
    return i;
  fail:;
  }
  return -1;
}


int main(int argc, char *argv[]){
  ios::sync_with_stdio(false);

  int T;
  cin >> T;
  for(int i = 0; i < T; i++){
    LLI res = 0;
    LLI N,L,H;
    vector<LLI> v;
    cin >> N >> L >> H;
    REP(j,N){
      LLI k;
      cin >> k;
      v.push_back(k);
    }
    res = solve2(L,H,v);
    if(res == -1){
      cout << "Case #" << i + 1 << ": " << "NO" << endl;
    }else{
      cout << "Case #" << i + 1 << ": " << res << endl;
    }
  }

  return 0;
}
