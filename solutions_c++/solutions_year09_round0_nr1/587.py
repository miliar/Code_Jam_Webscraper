#include <iostream>
#include <sstream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <list>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <complex>
#include <cstdio>
#include <cassert>
#include <cmath>

#if defined (__GNUC__) && (__GNUC__ <= 2)
#include <hash_map>
#include <hash_set>
#else
#include <ext/hash_map>
#include <ext/hash_set>
using namespace __gnu_cxx;
#endif
using namespace std;

#define FOR(i,a,b) for(int i=(a),_b=(b);i<_b;i++)
#define REP(i,n) FOR(i,0,(n))
#define FORD(i,a,b) for(int i=(a),_b=(b);i>_b;i--)
#define sz size()
template<class T> inline int size(const T& c) { return c.sz; }
#define FORA(i,c) REP(i,size(c))

#define itype(c) __typeof((c).begin())
#define FORE(e,c) for(itype(c) e=(c).begin();e!=(c).end();e++)
#define pb push_back
//#define X first
//#define Y second
#define mp make_pair
#define all(x) (x).begin(),(x).end()
#define SORT(x) sort(all(x))
#define REVERSE(x) reverse(all(x))
#define CLEAR(x,c) memset(x,c,sizeof(x))

typedef long long LL;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef list<int> LI;
typedef list<LI> LLI;
typedef vector<string> VS;
LL s2i(string s) { istringstream i(s); LL x; i>>x; return x; }
template<class T> string i2s(T x) { ostringstream o; o << x; return o.str(); }

class X
{
public:
  double c;
  string n;

  bool operator==(const X a)
  {
    return ((c == a.c) && (n == a.n));
  }

  bool operator<(const X a)
  {
    return ((c < a.c) && (n < a.n));
  }
};

template<class T, class VT> int indexof(T x, VT v)
{
  int i=0;
  FORE(xx,v)
  {
    if((*xx) == x) return i;
    i++;
  }
  return -1;
}


#define pi acos(-1.)
#define eps 1e-7
#define inf 1000000000
#define maxn 1100
#define maxp 1100000

#define LIMIT_BIG 1000000
#define LIMIT_SMALL 10

ifstream fin("data.in");
#define cin fin

ofstream fout("data.out");
//#define cout fout

typedef pair<int,int> PII;
typedef vector<PII > VT;
typedef list<PII> LT;

VT tta, ttb;

bool compare_VT(PII a, PII b)
{
  return (a.first < b.first) || ((a.first == b.first) && (a.second < b.second));
}

bool compare_VT_D(PII a, PII b)
{
  return (a.second < b.second) || ((a.second == b.second) && (a.first < b.first));
}


typedef vector <char> VC;
typedef vector <VC> VVC;

int main(){
  int T;
  int NA, NB;

  int L, D, N;

  cin>>L>>D>>N;

  VS Dw;
  REP(wi, D)
  {
    string x;
    cin>>x;
    Dw.pb(x);
  }
#define LLIMIT (((L+2)*L + 1) * 2)
//  cout << "limit=" << LLIMIT<<endl;

  assert(LLIMIT < inf);
  char s[20000];//LLIMIT + 100];
  cin.getline(s,20000);//LLIMIT);

  VVC p;

  REP(C, N)
  {
    char s[20000];//LLIMIT + 100];
    char x[20000];//LLIMIT + 100];
    cin.getline(s,20000);//LLIMIT);
//    cout << s<<endl<<endl;

    while(s[strlen(s)-1] == '\n') s[strlen(s)-1] = 0;
    while(s[strlen(s)-1] == ' ') s[strlen(s)-1] = 0;
    while(s[0] == ' ')
    {
      strcpy(x, s+1);
      strcpy(s,x);
    }

    cout << s<<endl<<endl;

    p.clear();
    for(int si=0; s[si]; si++)
    {
      VC c;
      if(s[si] == '(')
      {
        c.clear();
        si++;
        while(s[si] != ')')
        {
          c.pb(s[si]);
          cout << s[si] << ",";
          si++;
        }
        cout << ">>"<<endl;
      }
      else
      {
        c.pb(s[si]);
        cout<< s[si]<<">>"<<endl;
      }
      p.pb(c);
    }

    int found = 0;
    FORE(dww, Dw)
    {
      bool notthistime = false;
      for(int i=0;i<L;i++)
      {
        if(indexof((*dww)[i], p[i]) < 0)
        {
          notthistime = true;
          break;
        }
      }
      if(notthistime) continue;

      found++;
    }

    cout << "found = "<<found<<endl;
    cout << "Case #"<<C+1<<": "<<found<<endl;
    fout << "Case #"<<C+1<<": "<<found<<endl;

  }
}
