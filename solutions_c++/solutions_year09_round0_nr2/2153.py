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
int dr[] = {-1, 0,0,1};
int dc[] = { 0,-1,1,0};

const PII undef = PII(-1,-1);

int H,W;
int alt[128][128];
//VVI alt(3,VI(3));

char res[128][128];

int basin[128][128];
//VVI basin(3,VI(3));

PII flow(int rInit, int cInit) {
  int r = rInit, c = cInit;
  REP (d,4) {
    int r1=rInit+dr[d], c1=cInit+dc[d];
    if (r1<0 || r1>=H || c1<0 || c1>=W) continue;
    if (alt[r1][c1] < alt[r][c]) 
      r = r1, c = c1;
  }
  PII ret(r,c);
  if (r==rInit && c==cInit) ret = undef;
  return ret;
}

void fill(int r, int c, int bs) {
  basin[r][c]=bs;
  REP (d,4) {
    int r1 = r + dr[d], c1 = c + dc[d];
    if (r1<0 || c1<0 || r1>=H || c1>=W) continue;
    if (flow(r1,c1) == PII(r,c))
      fill(r1,c1,bs);
  }
}

void solve() {
  REP (r,H) REP (c,W) basin[r][c] = -1;
  int bs = 0;
  REP (r,H) REP (c,W) if (flow(r,c) == undef) {
    fill(r,c,bs);
    ++bs;
  }

  VC names(26);
  char free='a';

  REP (r,H) REP (c,W) {
    int b = basin[r][c];
    if (names[b] == 0) names[b]=free++;
    res[r][c]=names[b];
  }
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
    ifs >> H >> W;
    REP (r,H) REP (c,W) ifs >> alt[r][c];
    solve();
    ofs << endl;
    REP (r,H) {
      REP (c,W) {
        if (c) ofs << " ";
        ofs << res[r][c];
      }
      ofs << endl;
    }
    //-------------------------------------------------------------
    ofs << endl;
    cout << double(clock() - clock_test) / CLOCKS_PER_SEC << " sec.\n";
  }
  ifs.close();
  ofs.close();
  cout << "EXECTION FINISHED IN " << double(clock() - clock_global) / CLOCKS_PER_SEC << " sec.\n";
  _getch();
}
