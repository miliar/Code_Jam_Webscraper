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

const double EPS = 1e-10;
const double PI  = acos(-1.0);

#define CLR(a) memset((a), 0 ,sizeof(a))

#define dump(x)  cout << #x << " = " << (x) << endl;
#define debug(x) cout << #x << " = " << (x) << " (L" << __LINE__ << ")" << " " << __FILE__ << endl;

string solve(map<string,char> &composed,
             const set<pair<char, char> > &opposed, const string &s){
  string str(s);
  string ostr;
  map<char,int> m;
  for(int i = 0; i < SZ(str); i++){
    ostr += str[i];
    m[str[i]]++;
    if(int(ostr.size()) >= 2){
      const string sp = ostr.substr(ostr.size()-2,2);
      if(composed.find(sp) != composed.end()){
        ostr = ostr.substr(0,ostr.size()-2);
        ostr += composed[sp];
        m[sp[0]]--;
        m[sp[1]]--;
        m[composed[sp]]++;
      }
      for(set<pair<char, char> >::const_iterator itr = opposed.begin();
          itr != opposed.end(); ++itr){
        if(m[itr->first] > 0 && m[itr->second] > 0){
          m.clear();
          ostr.clear();
        }
      }
    }
  }

  ostringstream oss;
  oss << "[";
  for(int i = 0; i < SZ(ostr); i++){
    oss << ostr[i];
    if(i != SZ(ostr)-1){
      oss << ", ";
    }
  }
  oss << "]";
  return oss.str();
}


int main(int argc, char *argv[]){
  ios::sync_with_stdio(false);
  int T;

  cin >> T;
  REP(i,T){
    vector<pair<char, int> > v;
    map<string,char> composed;
    set<pair<char,char> > opposed;
    string s;
    int C,D,N;
    cin >> C;
    REP(k,C){
      string line;
      cin >> line;
      if(line.size() != 0){
        string key1 = line.substr(0,2);
        string key2(key1.rbegin(),key1.rend());
        composed[key1] = line[line.size()-1];
        composed[key2] = line[line.size()-1];
      }
    }
    cin >> D;
    REP(k,D){
      string line;
      cin >> line;
      if(line.size() != 0){
        opposed.insert(make_pair(line[0],line[1]));
      }
    }
    cin >> N;
    cin >> s;

    cout << "Case #" << i + 1 << ": "
         << solve(composed,opposed,s) << endl;
  }

  return 0;
}
