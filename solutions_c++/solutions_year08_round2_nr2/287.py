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

template <class T>
T gcd(T a, T b) 
{
  T t;
  while (b>0) t=a,a=b,b=t%b;
  return a;
}

template <class T>
T lcm(T a, T b) {
  if (a==0 && b==0) return 0;
  return a/gcd(a,b)*b;
}

///////////////////////////////////////////////////////////////////////////////////
string caseNo(int i) {return "Case #" + tostr(i) + ":";}


///////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////////

const int nera = 1000*1000+100;
char era[nera];

VL primes;

void buildEra() {
  memset(era,1,sizeof(era));
  lint i = 2;
  while (i*i<nera) {
    if (era[i]) {
      lint j = i+i;
      while (j < nera) {
        era[j]=0;
        j += i;
      }
    }
    ++i;
  }
  FOR (i,2,nera) if (era[i]) primes.push_back(i);
}
/////////////////////////////////////////////////////


lint A,B,P;

typedef set<int> Set;

VI gr;

bool share(lint a, lint b) {
  lint g = gcd(a,b);
  int i = 2;
  while (g != 1) {
    if (g%i==0) {
      if (i>=P) return 1;
      while (g%i==0) g/=i;
    }
    ++i;
  }
  return 0;
}

lint solve() {
  gr = VI(1024);
  for (lint i = A; i  <= B; ++i) {
    gr[i]=i;
  }
  for (lint i = A; i <= B; ++i) for (lint j = i+1; j <= B; ++j) {
    if (share(i,j)) {
      //cout << i << " " << j << endl;
      lint k1 = j;
      while (gr[k1] != k1) k1 = gr[k1];
      lint k2 = i;
      while (gr[k2] != k2) k2 = gr[k2];
      gr[k2] = k1;
    }
  }
  lint ret = 0;
  for (lint i = A; i <= B; ++i) if (gr[i]==i) ++ret;
  return ret;
}

void main()
{
  buildEra();

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
    ifs >> A >> B >> P;
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
