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
const int inf = 1000100100;
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

int A, N, M;
int X1, Y1, X2, Y2, X3, Y3;

bool solve() {
  for (X1=0; X1<=N; ++X1) for (Y1=0;Y1<=M;++Y1) {
    for (X2=X1;X2<=N;++X2) for (Y2=Y1;Y2<=M;++Y2) {
      if (X2 == X1 && Y2 == Y1) continue;
      X3 = 0, Y3 = 0;
      while (X3 <= N && Y3 <= M) {
        int dx1 = X1-X3, dx2 = X2-X3, dy1 = Y1-Y3, dy2 = Y2-Y3;
        int a = abs(dx1 * dy2 - dx2 * dy1);
        if (a == A) 
          return 1;
        if (a < A) ++Y3; else ++X3;
      }
    }
  }
  return 0;
}


void main()
{
  clock_t clock_global = clock();
  ifstream ifs("data.in");
  ofstream ofs("data.out"); ofs << setprecision(9);
  int ntests;
  ifs >> ntests;
  getline(ifs,string());
  FOR (test,1,ntests+1) {
    clock_t clock_test = clock();
    ofs << caseNo(test);
    cout << caseNo(test) << " ... ";
    //-------------------------------------------------------------
    ifs >> N >> M >> A;
    bool ret = solve();
    if (ret) {
      ofs << " " << X1 << " " << Y1 << " " << X2 << " " << Y2 << " " << X3 << " " << Y3;
      int actual = (X1 - X3) * (Y2 - Y3) - (X2 - X3) * (Y1 - Y3);
      actual = abs(actual);
      assert(actual == A);
    }
    else ofs << " IMPOSSIBLE";
    //-------------------------------------------------------------
    ofs << endl;
    cout << double(clock() - clock_test) / CLOCKS_PER_SEC << " sec.\n";
  }
  ifs.close();
  ofs.close();
  cout << "EXECTION FINISHED IN " << double(clock() - clock_global) / CLOCKS_PER_SEC << " sec.\n";
  _getch();
}
