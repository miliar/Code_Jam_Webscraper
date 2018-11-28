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
const int inf = 100010010;
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

int M, V, In;
VI G, C, Val;

int mem[12000][2];

int calc(int nd, int v) {
  if (nd > In) {
    if (Val[nd]==v) return 0;
    return inf;
  }
  int& ret = mem[nd][v];
  if (ret != -1) return ret;
  ret = inf;
  int s1 = nd*2, s2 = nd*2+1;

  int g = G[nd];

  REP (iter,2) {
    int cur;
    int val1 = calc(s1,v), val2 = calc(s2,v);
    if (g == 1) {
      if (v == 1) {
        cur = val1 + val2;
      } else {
        cur = min(val1, val2);
      }
    } else { // g == 0
      if (v == 1) {
        cur = min(val1, val2);
      } else {
        cur = val1 + val2;
      }
    }
    cur += iter;

    ret = min(ret, cur);

    if (C[nd]==0) break;
    g = 1-g;
  }
  return ret;
}

int solve() {
  memset(mem,-1,sizeof(mem));
  int ret = calc(1, V);
  if (ret >= inf) ret = -1;
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
    ifs >> M >> V;
    In = (M-1)/2;
    G.resize(In+1);
    C.resize(In+1);
    Val.assign(M+1,-1);
    FOR (i,1,In+1) ifs >> G[i] >> C[i];
    FOR (i,In+1,M+1) ifs >> Val[i];

    int ret = solve();
    if (ret == -1) ofs << " IMPOSSIBLE"; else ofs << " " << ret;
    //-------------------------------------------------------------
    ofs << endl;
    cout << double(clock() - clock_test) / CLOCKS_PER_SEC << " sec.\n";
  }
  ifs.close();
  ofs.close();
  cout << "EXECTION FINISHED IN " << double(clock() - clock_global) / CLOCKS_PER_SEC << " sec.\n";
  _getch();
}
