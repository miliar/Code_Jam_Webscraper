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
// returns number of bits in non-negative n
inline int bits(lint n) {int r=0; while (n>0) r++, n&=n-1; return r;}   

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

int n,k;
int pr1[128][32];
int& pr(int i, int j) {
  assert(i>=0 && i<n); 
  assert(j>=0 && j<k);
  return pr1[i][j];
}

int mem[1<<16];

VVI cr1;
VI cr2; 

int calc(int mask) {
  if (mask==0) return 0;
  int& ret = mem[mask];
  if (ret != -1) return ret;

  ret = inf;
  for (int mask1 = mask; mask1 > 0; mask1 = (mask1-1) & mask) {
    if (cr2[mask1]) continue;
    int cur = calc(mask ^ mask1) + 1;
    MIN(ret,cur);
  }
  return ret;
}

int solve() {
  cr1 = VVI(n,VI(n));
  REP (i,n) REP (j,n) {
    if (i == j) continue;
    bool ab = 0, be = 0, eq = 0;
    REP (p,k) {
      int p1 = pr(i,p), p2 = pr(j,p);
      if (p1 == p2) eq = 1; else
        if (p1 < p2) be = 1; else ab = 1;
    }
    if (eq) cr1[i][j] = 1;
    if (ab && be) cr1[i][j] = 1;
  }

  int all = 1<<n;

  cr2 = VI(all);
  FOR (mask,1,all) {
    if (bits(mask)==1) continue;
    int p = 0;
    while ((mask & 1<<p) == 0) ++p;
    int mask1 = mask ^ 1<<p;
    if (cr2[mask1]) {
      cr2[mask]=1;
      continue;
    }
    FOR (q,p+1,n) {
      if ((mask & 1<<q)==0) continue;
      if (cr1[p][q]) {
        cr2[mask]=1;
        break;
      }
    }
  }

  memset(mem,-1,sizeof(mem));
  int ret = calc(all-1);
  return ret;
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
    ifs >> n >> k;
    REP (i,n) REP (j,k) ifs >> pr(i,j);
    int res = solve();
    ofs << " " << res;
    //-------------------------------------------------------------
    ofs << endl;
    cout << double(clock() - clock_test) / CLOCKS_PER_SEC << " sec.\n";
  }
  ifs.close();
  ofs.close();
  cout << "EXECTION FINISHED IN " << double(clock() - clock_global) / CLOCKS_PER_SEC << " sec.\n";
  _getch();
}
