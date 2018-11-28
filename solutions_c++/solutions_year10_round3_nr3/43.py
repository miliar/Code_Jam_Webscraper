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

int ILE;

int n,m;
int t[1000][1000];

void odczyt()
{
  scanf("%d%d",&n,&m);
  REP(i,n)
  {
    char st[1000];
    scanf("%s",st);
    int poz=0;
    REP(k,m)
    {
      int x=(isdigit(st[k]) ? (st[k]-'0') : (st[k]-'A'+10));
      FORD(j,3,0) { t[i][poz]=((x&(1<<j)) >> j); poz++; }
    }
  }
//  puts(""); REP(i,n) { REP(j,m) printf("%d",t[i][j]); puts(""); }
}

int tab[1000][1000];
int dol[1000][1000];
int prawo[1000][1000];

inline bool ins(int g,int h) { return g>=0 && g<h; }

void dp()
{
  REP(i,n)
  {
    FORD(j,m-1,0) { prawo[i][j]=1; if (j+1<m && t[i][j]!=t[i][j+1]) prawo[i][j]=prawo[i][j+1]+1; }
  }
  REP(j,m)
  {
    FORD(i,n-1,0) { dol[i][j]=1; if (i+1<n && t[i][j]!=t[i+1][j]) dol[i][j]=dol[i+1][j]+1; }
  }
  FOR(i,0,n) FOR(j,0,m) tab[i][j]=0;
  FORD(i,n-1,0) FORD(j,m-1,0)
  {
    tab[i][j]=min(dol[i][j],prawo[i][j]);
    if (ins(i+1,n) && ins(j+1,m) && t[i+1][j+1]==t[i][j]) tab[i][j]=min(tab[i][j],tab[i+1][j+1]+1); else tab[i][j]=min(tab[i][j],1);
  }
}

int a[300000];
int N;

PII drz[4*300000];
int ile;

inline void insert(int x,int arg)
{
  assert(x<N);
  int v=ile+x;
  drz[v].FI=min(drz[v].FI,arg);
  while (v!=1)
  {
    v/=2;
    drz[v]=max(drz[2*v],drz[2*v+1]);
  }
}

void doit()
{
  REP(i,n) REP(j,m) a[i*m+j]=tab[i][j];
  N=n*m;
  ile=1;
  while (ile<N) ile*=2;
  FOR(i,1,2*ile-1) drz[i]=MP(0,0);
  REP(i,N) drz[ile+i]=MP(a[i],-i);
  FORD(i,ile-1,1) drz[i]=max(drz[2*i],drz[2*i+1]);

  vector<PII> wyn;
  int aa=-1,bb=0;
  int suma=0;
  while (1)
  {
    PII p=drz[1];
    if (p.FI==0)
    {
      wyn.PB(MP(aa,bb));
      break;
    }
    if (p.FI==aa) bb++;
    else { if (aa!=-1) wyn.PB(MP(aa,bb)); aa=p.FI; bb=1; }

    int i=(-p.SE)/m, j=(-p.SE)%m;
    suma+=sqr(aa);
//    printf("%d %d %d\n",i,j,aa);
    REP(k,aa) REP(l,aa) insert((i+k)*m+(j+l),0);
//    printf("(%d,%d):  ",i,j);
    FOR(k,-aa+1,aa-1) FOR(l,-aa+1,-1)
    {
      int x=i+k, y=j+l;
//      printf("(%d,%d) ",x,y);
      if (!ins(x,n) || !ins(y,m)) continue;
      insert(x*m+y, k>=0 ? -l : max(-k,-l));
    }
    FOR(k,-aa+1,aa-1) FOR(l,-aa+1,-1)
    {
      int x=i+l, y=j+k;
//      printf("(%d,%d) ",x,y);
      if (!ins(x,n) || !ins(y,m)) continue;
      insert(x*m+y, k>=0 ? -l : max(-k,-l));
    }
//    puts("");
  }
  assert(suma==n*m);

  printf("%d\n",SIZE(wyn));
  REP(i,SIZE(wyn)) printf("%d %d\n",wyn[i].FI,wyn[i].SE);
}

int main()
{
  scanf("%d",&ILE);
  FOR(iii,1,ILE)
  {
    printf("Case #%d: ",iii);
    odczyt();
    dp();
    doit();
  }
  return 0;
}
