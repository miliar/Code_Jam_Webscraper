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


#include <cassert>


bool convert(vector<string> &v){
  //debug(v);
  for(int i= 0; i < SZ(v); i++){
    for(int j=0; j < SZ(v[i]); j++){
      if(v[i][j] == '#'){
        if(i == SZ(v)-1 || j == SZ(v[i])-1){
          cout << "Impossible" << endl;
          return false;
        }else{
          if(v[i][j+1] == '#' && v[i+1][j] == '#' && v[i+1][j+1] == '#'){
            v[i][j] = '/';
            v[i][j+1] = '\\';
            v[i+1][j] = '\\';
            v[i+1][j+1] = '/';
          }else{
            cout << "Impossible" << endl;
            return false;
          }
        }
      }
    }
  }
  REP(i,SZ(v)){
    cout << v[i] << endl;
  }

  return true;
}


int main(int argc, char *argv[]){
  ios::sync_with_stdio(false);

  int T;
  cin >> T;
  for(int i = 0; i < T; i++){
    vector<string> v;
    int R,C;
    string line;
    cin >> R >> C;
    getline(cin,line);
    REP(j,R){
      getline(cin,line);
      v.push_back(line);
      assert(SZ(line) == C);
    }
    cout << "Case #" << i + 1 << ": " << endl;
    convert(v);
  }

  return 0;
}
