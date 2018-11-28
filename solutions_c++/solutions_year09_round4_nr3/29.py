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

/* Pasted (my) code of the Dinic algorithm. */

/* Maksymalny przeplyw metoda prawie Dinica.
 * Zlozonosc: O(V^4), ale nie znam przypadku, zeby nie byla O(V^3).
 *
 * Algorytm wyznacza przeplyw. */

#define MAX_N 300

struct kraw
{
  int c,f; /* przepustowosc, przeplyw */
  int v; /* wierzcholek docelowy */
};

vector<kraw> t[MAX_N];
vector<kraw>::iterator poz[MAX_N];
int n;

/* Minimalny przekroj to krawedzie, laczace po wykonaniu algorytmu
 * wierzcholek o tab[i]>=0 i wierzcholek o tab[i]==-1. */
int tab[MAX_N];

/* dodawanie krawedzi skierowanej z przepustowoscia */
void add_edge(int v1,int v2,int c)
{
  kraw e;
  e.v=v2; e.c=c; e.f=0; t[v1].PB(e);
  e.v=v1; e.c=0; e.f=0; t[v2].PB(e);
}

int c[MAX_N][MAX_N],c0[MAX_N][MAX_N]; /* c0 do odzysku przeplywu */
int v2;

bool bfs(int v)
{
  REP(i,n) tab[i]=-1;
  tab[v]=0;
  int kol[n],p,k;
  kol[0]=v; p=k=0;
  while (p<=k)
  {
    v=kol[p++];
    FORE(it,t[v])
      if (tab[it->v]==-1 && c[v][it->v]>0)
      {
        tab[it->v]=tab[v]+1; kol[++k]=it->v;
      }
  }
  return (tab[v2]!=-1);
}

int dfs(int v,int mi)
{
  int wyn=0,y;
  if (v==v2 || !mi) return mi;
  for (vector<kraw>::iterator &it=poz[v]; it!=t[v].end(); ++it)
  {
    if (tab[v]+1==tab[it->v] && c[v][it->v]) 
    {
      y=dfs(it->v,min(mi,c[v][it->v]));
      c[v][it->v]-=y; c[it->v][v]+=y;
      wyn+=y; mi-=y;
      if (!mi) break;
    }
  }
  return wyn;
}

/* Maksymalny przeplyw */
int maxflow(int pocz,int kon)
{
  int wyn=0;
  v2=kon;
  memset(c,0,sizeof(c));
  REP(i,n) REP(j,SIZE(t[i]))
    c[i][t[i][j].v]+=t[i][j].c;
  REP(i,n) REP(j,n) c0[i][j]=c[i][j];
  while (bfs(pocz))
  {
    REP(i,n) poz[i]=t[i].begin();
    wyn+=dfs(pocz,INFTY);
  }
  /* Odzyskujemy przeplyw */
  REP(i,n) FORE(it,t[i])
  {
    it->f=max(0, min(it->c,c0[i][it->v]-c[i][it->v]));
    c[i][it->v]+=it->f;
  }
  return wyn;
}

int ILE;

int pp[200][100];

int main()
{
  scanf("%d",&ILE);
  FOR(LICZ,1,ILE)
  {
    printf("Case #%d:",LICZ);
    int N,k;
    scanf("%d%d",&N,&k);
    n=2*N+2;
    REP(i,n) t[i].clear();
    REP(i,N) REP(j,k) scanf("%d",pp[i]+j);
    REP(i,N) add_edge(2*N,i,1);
    FOR(i,N,2*N-1) add_edge(i,2*N+1,1);
    REP(i,N) REP(j,N)
    {
      bool ok=1;
      REP(a,k) if (pp[i][a]>=pp[j][a]) { ok=0; break; }
      if (ok) add_edge(i,N+j,1);
    }
    int w=maxflow(2*N,2*N+1);
    printf(" %d\n",N-w);
  }
  return 0;
}
