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
const lint lim = (1LL<<32);
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



int n;
VL X,Y;

lint mod[3][3];

lint solve() {
  lint ret = 0;

  memset(mod,0,sizeof(mod));
  REP (i,n) ++mod[X[i]%3][Y[i]%3];
  REP (i,9) {
    lint a = i%3, b = i/3;
    if (mod[a][b]<3) continue;
    lint v = mod[a][b];
    lint cur = v * (v-1) * (v-2) / 6;
    ret += cur;
  }
  REP (i,9) REP (j,9) if (i != j) {
    lint a1 = i%3, b1 = i/3, a2 = j%3, b2 = j/3;
    if ((a1 + 2*a2) % 3 != 0) continue;
    if ((b1 + 2*b2) % 3 != 0) continue;
    lint v1 = mod[a1][b1], v2 = mod[a2][b2];
    if (v2 < 2) continue;
    lint cur = v1 * v2 * (v2-1) / 2;
    ret += cur;
  }

  REP (i,9) FOR (j,i+1,9) FOR (k,j+1,9) {
    lint a1 = i%3, b1 = i/3, a2 = j%3, b2 = j/3, a3 = k%3, b3 = k/3;
    if ((a1+a2+a3) % 3 != 0 || (b1+b2+b3) % 3 != 0) continue;
    lint v1 = mod[a1][b1], v2 = mod[a2][b2], v3 = mod[a3][b3];
    lint cur = v1 * v2 * v3;
    ret += cur;
  }
  return ret;
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
    lint A,B,C,D,x0,y0,M;
    ifs >> n >> A >> B >> C >> D >> x0 >> y0 >> M;
    X.resize(n); Y.resize(n);

    X[0] = x0, Y[0] = y0;
    FOR (i,1,n) {
      X[i] = (A * X[i-1] + B) % M;
      Y[i] = (C * Y[i-1] + D) % M;
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
