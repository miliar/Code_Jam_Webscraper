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

lint mem[128][128];
int rock[128][128];
int H, W;

lint calc(int r, int c) {
  if (rock[r][c]) return 0;
  if (r < 0 || c < 0) return 0;
  if (r == 0 && c == 0) return 1;

  lint& ret = mem[r][c];
  if (ret != -1) return ret;
  ret = calc(r-2,c-1) + calc(r-1,c-2);
  ret %= 10007;
  return ret;
}

lint solve() {
  memset(mem,-1,sizeof(mem));
  lint ret = calc(H-1,W-1);
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
    int R;
    ifs >> H >> W >> R;
    memset(rock,0,sizeof(rock));
    REP (i,R) {
      int r,c;
      ifs >> r >> c;
      rock[r-1][c-1]=1;
    }
    lint ret = solve();
    ofs << " " << ret;
    //-------------------------------------------------------------
    ofs << endl;
    cout << double(clock() - clock_test) / CLOCKS_PER_SEC << " sec.\n";
  }
  ifs.close();
  ofs.close();
  cout << "EXECTION FINISHED IN " << double(clock() - clock_global) / CLOCKS_PER_SEC << " sec.\n";
  _getch();
}
