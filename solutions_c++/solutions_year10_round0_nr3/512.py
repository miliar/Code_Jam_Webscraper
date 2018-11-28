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

lint runs,cap,n;
VL g;

lint solve() {
  VL prev_cycle((size_t)n,-1), prev_money((size_t)n);
  lint r = 0;
  int pos = 0;
  lint money = 0;

  bool jumped = false;
  
  while (r < runs) {
    if (prev_cycle[pos] == -1 || jumped) {
      prev_cycle[pos] = r;
      prev_money[pos] = money;
      lint fill = 0;
      int pos1 = pos;
      fill += g[(size_t)pos];
      pos = (pos+1) % int(n);
      while (pos != pos1 && fill+g[pos] <= cap) {
        fill += g[pos];
        pos = (pos+1) % int(n);
      }
      money += fill;
      ++r;
    } else {
      jumped = true;
      lint r_left = runs - r;
      lint r_repeat = r - prev_cycle[pos];
      lint m_repeat = money - prev_money[pos];

      lint r_inc = r_left - r_left % r_repeat;
      lint m_inc = m_repeat * (r_left / r_repeat);

      r += r_inc;
      money += m_inc;
    }
  }

  return money;
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
    ifs >> runs >> cap >> n;
    g = VL((size_t)n);
    REP (i,(int)n) ifs >> g[i];
    lint res = solve();
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
