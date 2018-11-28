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

#define LIMIT_BIG (500 * 2)
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

typedef vector < pair < pair <int, int> , int > >  VPI;

VPI cache;

int in_cache(int si, int xi)
{
  FORE(cc, cache)
  {
    if(((*cc).first.first == si) && ((*cc).first.second == xi)) return (*cc).second;
  }
  return -1;
}


int solve(char *s, int si, char *x, int xi)
{
  int retval = 0;

  assert(si < LIMIT_BIG);
  assert(xi < LIMIT_BIG);
  if(x[xi] == 0) retval = 1;
  else
  {
  if(s[si] == 0) retval = 0;
  else
  {

  int rv = in_cache(si,xi);
  if(rv >= 0) return rv;

  if(s[si] == x[xi])
  {
    retval += solve(s, si+1, x, xi+1);
  }

  retval += solve(s, si+1, x, xi);

  }
  }
  if(in_cache(si,xi) < 0)
  {
    cache.pb(mp(mp(si,xi), retval % 10000));
  }
  return retval % 10000;
}


int maps[200][200];
int water[200][200];


int drain(int H, int W, int j, int i, int bed)
{
  int x=maps[j][i];
  int n,w,e,s;
  int jd,id;


  if((water[j][i] >= 0) && (water[j][i] != bed)) return water[j][i];
  if(j>0) n = maps[j-1][i]; else n=inf;
  if(i>0) w = maps[j][i-1]; else w=inf;
  if(i<W-1) e = maps[j][i+1]; else e=inf;
  if(j<H-1) s = maps[j+1][i]; else s=inf;

  if(min(n,min(w,min(e,s))) == n)
  {
    if(x > n)
    {
      jd = -1;
      id = 0;
    }
    else
    {
      jd = 0; id = 0;
    }
  }
  else if(min(n,min(w,min(e,s))) == w)
  {
    if(x > w)
    {
      jd = 0;
      id = -1;
    }
    else
    {
      jd = 0; id = 0;
    }
  }
  else if(min(n,min(w,min(e,s))) == e)
  {
    if(x > e)
    {
      jd = 0;
      id = 1;
    }
    else
    {
      jd = 0; id = 0;
    }
  }
  else if(min(n,min(w,min(e,s))) == s)
  {
    if(x > s)
    {
      jd = 1;
      id = 0;
    }
    else
    {
      jd = 0; id = 0;
    }
  }

  if((jd != 0) || (id != 0))
  {
    int d = drain(H,W,j+jd,i+id, bed);
    if(d != bed)
    {
      water[j][i] = d;
      return d;
    }
    else
    {
      water[j][i] = bed;
      return bed;
    }
  }
  else
  {
    water[j][i] = bed;
    return bed;
  }
}


VI connected[200*200];


int main(){
  int W,H,T;


  cin>>T;

  REP(C, T)
  {
    cin>>H>>W;
    REP(j,H)
    {
      REP(i,W)
      {
        cin>>maps[j][i];
        water[j][i] = -1;
      }
    }

    for(int k=0;k<200*200;k++) connected[k].clear();

    int lastBed = 0;
    int bed = 0;
    REP(j,H)
    {
      REP(i,W)
      {
        lastBed = drain(H,W,j,i, bed);
        if(lastBed == bed)
        {
          lastBed = bed;
          bed++;
        }
      }
    }



    cout << "Case #"<<C+1<<":"<<endl;
    fout << "Case #"<<C+1<<":"<<endl;

    REP(j,H)
    {
      REP(i,W)
      {
        cout<<(char)(water[j][i] + 'a')<<" ";
        fout<<(char)(water[j][i] + 'a')<<" ";
      }
      cout << endl;
      fout << endl;
    }

  }

//  int x = 1;
//  for(int i=0;i<19;i++)
//  {
//    x = (x * 26) % 10000;
//  }
//
//  cout << x<<endl;

}
