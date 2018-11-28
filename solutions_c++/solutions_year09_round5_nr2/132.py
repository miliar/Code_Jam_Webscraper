// Compiler : MS VC++ 8.0
// input  file : d.in
// output file : d.out

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
#include <ctime>
#include <conio.h>
#include <list>

using namespace std;
typedef long long lint;
typedef vector<int> VI; typedef vector<VI> VVI;
typedef vector<lint> VL; typedef vector<VL> VVL;
typedef vector<double> VD; typedef vector<VD> VVD;
typedef vector<char> VC; typedef vector<VC> VVC;
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
const int inf = 1000100100; // (inf + inf) fits into "int" type.
const double Pi = acos(-1.);
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

const int MOD = 10009;

string poly;
int nterms;
int ntermlen[8];
int terms[8][8];

int K;
int n;
VS dict;
VVI words;
VI res;
int fak[16];

void preparePoly() {
  memset(ntermlen,0,sizeof(ntermlen));
  int ti = 0;
  FORS (p,poly) {
    if (poly[p]=='+') ti++; else
      terms[ti][ntermlen[ti]++] = poly[p]-'a';
  }
  nterms = ti+1;
}

int calcPoly(const VI& arg) {
  int ret = 0;
  REP (ti,nterms)  {
    int cur = 1;
    REP (i,ntermlen[ti]) {
      cur = cur * arg[terms[ti][i]] % MOD;
    }
    ret = (ret + cur) % MOD;
  }
  return ret;
}

void add(VI& a, const VI& b, int mul) {
  REP (i,26) a[i] += mul * b[i];
}

void sub(VI& a, const VI& b, int mul) {
  REP (i,26) a[i] -= mul * b[i];
}

int fillS(VI& s, int left, int wi, int mult) {
  if (left == 0) {
    int ret = mult % MOD * calcPoly(s) % MOD;
    return ret;
  }
  if (wi == n) return 0;

  int ret = 0;
  REP (m,left+1) {
    if (m) add(s,words[wi],m);
    int cur = fillS(s, left-m, wi+1, mult/fak[m]);
    ret = (ret + cur) % MOD;
    if (m) sub(s,words[wi],m);
  }
  return ret;
}

void fillRes(int d) {
  VI s(26);
  res[d-1] = fillS(s,d,0,fak[d]);
}

void solve() {
  fak[0]=1; FOR (i,1,16) fak[i]=fak[i-1]*i;

  preparePoly();
  words = VVI(n,VI(26));
  
  REP (wi,n) FORS (i,dict[wi]) {
    words[wi][dict[wi][i]-'a']++;
  }

  res = VI(K,-1);
  FOR (d,1,K+1) fillRes(d);
}


void main()
{
  clock_t clock_global = clock();
  ifstream ifs("d.in");
  ofstream ofs("d.out"); ofs << setprecision(9);
  int ntests;
  ifs >> ntests;
  getline(ifs,string());
  FOR (test,1,ntests+1) {
    clock_t clock_test = clock();
    ofs << caseNo(test);
    cout << caseNo(test) << " ... ";
    //-------------------------------------------------------------
    ifs >> poly >> K >> n;
    dict.resize(n);
    getline(ifs,string());
    REP (i,n) getline(ifs, dict[i]);
    solve();
    REP (d,K) ofs << " " << res[d];
    //-------------------------------------------------------------
    ofs << endl;
    cout << double(clock() - clock_test) / CLOCKS_PER_SEC << " sec.\n";
  }
  ifs.close();
  ofs.close();
  cout << "EXECTION FINISHED IN " << double(clock() - clock_global) / CLOCKS_PER_SEC << " sec.\n";
  _getch();
}
