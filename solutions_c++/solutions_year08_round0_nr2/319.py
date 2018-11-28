// Compiler : MS VC++ 8.0
// input  file : data.in
// output file : data.out

#include <string>
#include <sstream>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
#include <cmath>
#include <numeric>
#include <iomanip>
#include <iostream>
#include <cassert>
#include <fstream>

using namespace std;
typedef long long lint;
typedef vector<int> VI; typedef vector<VI> VVI;
typedef vector<lint> VL; typedef vector<VL> VVL;
typedef vector<double> VD; typedef vector<VD> VVD;
typedef vector<string> VS;
#define SIZE(c) ((int)(c).size())
#define SEQ(c) (c).begin(),(c).end()
#define FOR(i,a,b) for(int _U(b),i=(a);i<_U;++i)
#define REP(i,n) FOR(i,0,n)
#define FORD(i,a,b) for(int _U(a),i=(b)-1;i>=_U;--i)
#define FORS(i,c) FOR(i,0,SIZE(c))
#define REPD(i,n) FORD(i,0,n)
template<class T>string tostr(T v){ostringstream o;o<<v;return o.str();}
string tostrdouble(double v) {ostringstream o;o<<fixed<<setprecision(7)<<v; return o.str();}
#define UNIQUE(c) {sort(SEQ(c)); (c).erase(unique(SEQ(c)),(c).end());}
typedef pair<int,int> PII;
#define MIN(A,B) if ((B)<(A)) (A)=(B)
#define MAX(A,B) if ((B)>(A)) (A)=(B)
const int inf = 1000100100;
///////////////////////////////////////////////////////////////////////////////////
template <class T>
vector<T> splitString(string s, string sep = " ") {
  vector<T> ret;
  int pos = -1, posPrev = -2;
  do {
    posPrev = pos;
    pos = (int)s.find_first_of(sep, posPrev+1);
    if (pos == -1) pos = (int)s.size();
    if (pos-posPrev > 1) {
      istringstream is(s.substr(posPrev+1,pos-posPrev-1));
      T v; is >> v; ret.push_back(v);
    }
  } while (posPrev < (int)s.size());
  return ret;
}
///////////////////////////////////////////////////////////////////////////////////
string caseNo(int i) {return "Case #" + tostr(i) + ":";}

///////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////////

PII getTimes(string s) {
  replace(SEQ(s),':',' ');
  VI v = splitString<int>(s);
  assert(v.size() == 4);
  PII ret(v[0]*60+v[1],v[2]*60+v[3]);
  return ret;
}
///////////////////////////////////////////////////////////////////////////////////

int nab, nba;
vector<PII> ab, ba;
int pause;

typedef multiset<int> Set;
Set afree, bfree;


///////////////////////////////////////////////////////////////////////////////////

PII ret;

void handleA(int i) {
  assert(i < nab);  
  if (afree.empty() || *afree.begin() > ab[i].first) {
    afree.insert(0);
    ++ret.first;
  }
  Set::iterator it = afree.upper_bound(ab[i].first);
  --it;
  afree.erase(it);
  bfree.insert(ab[i].second + pause);
}

void handleB(int j) {
  assert(j < nba);
  if (bfree.empty() || *bfree.begin() > ba[j].first) {
    bfree.insert(0);
    ++ret.second;
  }
  Set::iterator it = bfree.upper_bound(ba[j].first);
  --it;
  bfree.erase(it);
  afree.insert(ba[j].second + pause);
}

PII solve() {
  ret = PII(0,0);
  int i = 0, j = 0;
  sort(SEQ(ab));
  sort(SEQ(ba));
  afree.clear(); bfree.clear();
  while (i < nab && j < nba) {
    if (ab[i].first < ba[j].first) handleA(i++); else handleB(j++);
  }
  while (i < nab) handleA(i++);
  while (j < nba) handleB(j++);
  return ret;
}

void main()
{
  ifstream ifs("data.in");
  ofstream ofs("data.out");
  int ntests;
  ifs >> ntests;
  getline(ifs,string());
  FOR (test,1,ntests+1) {
    ofs << caseNo(test);
    cout << caseNo(test) << endl;

    ifs >> pause;
    ifs >> nab >> nba;
    getline(ifs,string());
    
    ab.resize(nab);
    string s;
    REP (i,nab) {
      getline(ifs, s);
      ab[i] = getTimes(s);
    }
    ba.resize(nba);
    REP (i,nba) {
      getline(ifs, s);
      ba[i] = getTimes(s);
    }
    PII ret = solve();
    ofs << " " << ret.first << " " << ret.second;
    ofs << endl;
  }
}
