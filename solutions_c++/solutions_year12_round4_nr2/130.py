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
#define INFTY 1000000000
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
int n,X,Y;
PII r[1010];

int x[1010],y[1010],xw[1010],yw[1010];

inline int ABS(int a) { return a<0 ? -a : a; }

inline bool dobry(int j)
{
  REP(i,j)
  {
    if (ABS(x[j]-x[i])+ABS(y[j]-y[i])<r[i].FI+r[j].FI) return false;
  }
  return true;
}

void doit()
{
  x[0]=y[0]=0;
  FOR(i,1,n-1)
  {
    VI kand;
    kand.PB(-r[i].FI);
    //kand.PB(0); kand.PB(X-r[i].FI);
    REP(j,i) kand.PB(min(X-r[i].FI, x[j]+r[j].FI));
    sort(ALL(kand)); kand.erase(unique(ALL(kand)),kand.end());

    //REP(a,SIZE(kand)) printf("%d ",kand[a]); puts("");

    int best=Y+1,gdzie=-1;
    REP(a,SIZE(kand))
    {
      int co=kand[a]+r[i].FI,w=-r[i].FI;
      REP(j,i)
        if ((kand[a]>x[j]-r[j].FI && kand[a]<x[j]+r[j].FI) ||
            (co>x[j]-r[j].FI && co<x[j]+r[j].FI) ||
            (kand[a]+2*r[i].FI>x[j]-r[j].FI && kand[a]+2*r[i].FI<x[j]+r[j].FI))
          w=max(w,y[j]+r[j].FI);
      if (w<=best) { best=w; gdzie=co; }
    }
    x[i]=gdzie; y[i]=best+r[i].FI;
    //assert(y[i]<=Y);
    //assert(x[i]<=X);
  }
  REP(i,n) assert(dobry(i));
}

int main()
{
  scanf("%d",&ILE);
  FOR(iii,1,ILE)
  {
    printf("Case #%d: ",iii);
    fprintf(stderr,"Case #%d: \n",iii);
    scanf("%d%d%d",&n,&X,&Y);
    REP(i,n) { scanf("%d",&(r[i].FI)); r[i].SE=i; }
    sort(r,r+n);
    reverse(r,r+n);
    REP(i,n) x[i]=y[i]=-1;

    doit();

    REP(i,n) { xw[r[i].SE]=x[i]; yw[r[i].SE]=y[i]; }
    REP(i,n) printf("%d.0 %d.0 ",xw[i],yw[i]); puts("");
  }
  return 0;
}
