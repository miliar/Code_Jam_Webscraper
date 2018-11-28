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

const int CT = 512;
int n;
VVI in;
int fl[CT*2][CT*2];

void mirror(double r0, double c0, int& r1, int& c1, int type) {
  double dc = c0-c1;
  double dr = r0-r1;
  if (type) 
    r1 = int(r0 + dc), c1 = int(c0 + dr);
  else
    r1 = int(r0 - dc), c1 = int(c0 - dr);
}

int min_r, min_c, max_r, max_c;

int put(int r, int c, int v) {
  assert(r>=0 && r<CT*2 && c>=0 && c<CT*2);
  if (fl[r][c] != -1) {
    if (fl[r][c] == v) return 0;
    return -1;
  }
  min_r = min(min_r,r);
  min_c = min(min_c,c);
  max_r = max(max_r,r);
  max_c = max(max_c,c);
  fl[r][c]=v;
  return 1;
}

int put3(double r0, double c0, int r, int c, int v) {
  int ret = 0;
  int cur = put(r,c,v);
  if (cur == -1) return -1;
  ret+=cur;


  int r1 = r, c1 = c;
  mirror(r0,c0,r1,c1,0);
  cur = put(r1,c1,v);
  if (cur == -1) return -1;
  ret+=cur;

  mirror(r0,c0,r,c,1);
  cur = put(r,c,v);
  if (cur == -1) return -1;
  ret+=cur;

  return ret;
}

void clean_fl() {
  FOR (r,min_r,max_r+1) FOR (c,min_c,max_c+1) fl[r][c]=-1;
}

int goodCenter(double r0, double c0) {
  int r0int = int(r0);
  int c0int = int(c0);
  double r0frac = r0-r0int;
  double c0frac = c0-c0int;

  double CT_r = CT + r0frac;
  double CT_c = CT + c0frac;

  min_r = min_c = inf;
  max_r = max_c = -inf;

  int ret=0;

  REP (r,n) REP (c,n) {
    assert(r-r0+CT_r == int(r-r0+CT_r));
    assert(c-c0+CT_c == int(c-c0+CT_c));
    int cur = put3(CT_r, CT_c, r-r0+CT_r, c-c0+CT_c, in[r][c]);
    if (cur == -1) {
      clean_fl();
      return -1;
    }
    ret+=cur;
  }
  clean_fl();
  int max_dif = max((max_r - min_r + 1), (max_c - min_c + 1));
  ret = max_dif * max_dif - n*n;
  return ret;
}

int solve() {
  int ret = inf;
  for (double r = -2-n/2; r <= n + n/2 + 2; r += 0.5) 
  for (double c = -2-n/2; c <= n + n/2 + 2; c += 0.5) 
  {
    int cur = goodCenter(r,c);
    if (cur == -1) continue;
    ret = min(ret,cur);
  }
  assert(ret < inf);
  return ret;
}


void main()
{
  memset(fl,-1,sizeof(fl));
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
    ifs >> n;
    in = VVI(n,VI(n,-1));
    REP (i,n) {
      REP (j,i+1) {
        ifs >> in[i-j][j];
      }
    }
    int i = 5;
    REP (i,n-1) {
      FOR (j,i+1,n) {
        ifs >> in[i+n-j][j];
      }
    }

    int res = -1;
    //if (test == 2) 
    res = solve();
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
