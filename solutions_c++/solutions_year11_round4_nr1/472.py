//#include<iostream>
#include<cstdio>
#include<cctype>
#include<cmath>
#include<cstdlib>
#include<algorithm>
#include<vector>
#include<string>
#include<list>
#include<deque>
#include<map>
#include<set>
#include<queue>
#include<stack>
#include<utility>
#include<sstream>
#include<cstring>
#include<numeric>
#include<cassert>
using namespace std;

#define FOR(I,A,B) for(int I=(A);I<=(B);I++)
#define FORD(I,A,B) for(int I=(A);I>=(B);I--)
#define REP(I,N) for(int I=0;I<(N);I++)
#define ALL(X) (X).begin(),(X).end()
#define PB push_back
#define MP make_pair
#define FI first
#define SE second
#define INFTY 100000000
#define VAR(V,init) __typeof(init) V=(init)
#define FORE(I,C) for(VAR(I,(C).begin());I!=(C).end();I++)
#define SIZE(x) ((int)(x).size())

typedef vector<int> VI;
typedef pair<int,int> PII;
typedef long long ll;
typedef vector<string> VS;

ll nwd(ll a,ll b) { return !b?a:nwd(b,a%b); }
inline int CEIL(int a,int b) { return a%b ? a/b+1 : a/b; }
template <class T> inline T sqr(const T&a) { return a*a; }

VS parse(string s)
{
  string a;
  VS wyn;
  REP(i,(int)s.size())
    if (s[i]!=' ') a+=s[i];
    else if (!a.empty()) { wyn.PB(a); a=""; }
  if (!a.empty()) wyn.PB(a);
  return wyn;
}

int toi(char ch) { return int(ch)-int('0'); }

int chg(char ch) { return int(ch)-int('a'); }

int los(int m)
{
  return (int)((double)m*(rand()/(RAND_MAX+1.0)));
}

void wypisz(PII p)
{
  printf("(%d %d)\n",p.FI,p.SE);
}
void wypisz(VI t)
{
  REP(i,SIZE(t)) printf("%d ",t[i]); puts("");
}
void wypisz(vector<PII> t)
{
  REP(i,SIZE(t)) printf("(%d %d) ",t[i].FI,t[i].SE); puts("");
}
void wypisz(VS t)
{
  REP(i,SIZE(t)) printf("%s\n",t[i].c_str());
}
void wypisz(vector<VI> t)
{
  REP(i,SIZE(t)) wypisz(t[i]);
}


int ILE;

int X,S,R,T,N;
int b,e,w;

VI t;

void doit()
{
  scanf("%d%d%d%d%d",&X,&S,&R,&T,&N);
  int a=0;
  t.clear();
  while (N--)
  {
    scanf("%d%d%d",&b,&e,&w);
    while (a<b) { a++; t.PB(0); }
    while (a<e) { a++; t.PB(w); }
  }
  while (a<X) { a++; t.PB(0); }
  assert(SIZE(t)==X);

  sort(ALL(t)); //reverse(ALL(t));
  double wyn=0;
  double czas=T;
  REP(i,SIZE(t))
  {
    if (czas<1e-9)
    {
      wyn+=1.0/double(t[i]+S);
      continue;
    }
    double u=1.0/double(t[i]+R);
    if (u<=czas)
    {
      czas-=u;
      wyn+=1.0/double(t[i]+R);
    } else
    {
      double len=1.0-czas*double(t[i]+R);
      wyn+=czas;
      czas=0.0;
      wyn+=len/double(t[i]+S);
    }
  }
  printf("%.6lf\n",wyn);
}

int main()
{
  scanf("%d",&ILE);
  FOR(iii,1,ILE)
  {
    printf("Case #%d: ",iii);
    fprintf(stderr,"Case #%d: \n",iii);
    doit();
  }
  return 0;
}
