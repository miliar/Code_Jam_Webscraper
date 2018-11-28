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

int nextb(int i, const vector<pair<char, int> > &v){
  FOR(j,i,SZ(v)){
    if(v[j].first == 'B'){
      return v[j].second;
    }
  }
  return -1;
}

int nexto(int i, const vector<pair<char, int> > &v){
  FOR(j,i,SZ(v)){
    if(v[j].first == 'O'){
      return v[j].second;
    }
  }
  return -1;
}

int solve(const vector<pair<char, int> > &v){
  int i = 0;
  int rb = 1;
  int ro = 1;
  int tt = 0;
  while(i < v.size()){
    int nxb = nextb(i,v);
    int nxo = nexto(i,v);
    if(v[i].first == 'B'){
      int t = abs(nxb - rb) + 1;
      rb = nxb;
      tt += t;
      if(nxo != -1){
        if(abs(nxo - ro) > t){
          if(nxo < ro){
            ro -= t;
          }else{
            ro += t;
          }
        }else{
          ro = nxo;
        }
      }
    }else{ //O
      int t = abs(nxo - ro) + 1;
      ro = nxo;
      tt += t;
      if(nxb != -1){
        if(abs(nxb - rb) > t){
          if(nxb < rb){
            rb -= t;
          }else{
            rb += t;
          }
        }else{
          rb = nxb;
        }
      }
    }
    i++;
  }
  return tt;
}


int main(int argc, char *argv[]){
  ios::sync_with_stdio(false);
  int N;

  cin >> N;
  REP(i,N){
    int M;
    vector<pair<char, int> > v;
    cin >> M;
    REP(j,M){
      char r;
      int p;
      cin >> r >> p;
      v.push_back(make_pair(r,p));
    }
    cout << "Case #" << i + 1 << ": "
         << solve(v) << endl;
  }

  return 0;
}
