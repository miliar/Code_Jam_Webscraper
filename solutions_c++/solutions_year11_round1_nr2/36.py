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
typedef vector<PII> VPII;

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

int n,m;
VS t;
string s;
char st[100];


map<string,VPII> mapa,mapa1;

void doit()
{
  mapa.clear(); mapa1.clear();
  REP(i,SIZE(t))
  {
    string u;
    REP(j,SIZE(t[i])) u+='.';
    mapa[u].PB(MP(i,0));
  }
  REP(lit,SIZE(s))
  {
    mapa1.clear();
    char ch=s[lit];
    FORE(it,mapa)
    {
      string u=(*it).FI;
      VPII pom=(*it).SE;
      if (SIZE(pom)==1) { mapa1[u]=pom; continue; }
      bool czy=0;
      REP(i,SIZE(pom))
      {
        int nr=pom[i].FI;
        int ile=0;
        REP(j,SIZE(t[nr])) if (t[nr][j]==ch) { ile++; }
        if (ile) { czy=1; break; }
      }
      if (!czy) { mapa1[u]=pom; continue; }
      REP(i,SIZE(pom))
      {
        string v=u;
        int nr=pom[i].FI;
        assert(SIZE(t[nr])==SIZE(u));
        int ile=0;
        REP(j,SIZE(t[nr])) if (t[nr][j]==ch) { v[j]=ch; ile++; }
        if (!ile) pom[i].SE++;
        mapa1[v].PB(pom[i]);
      }
    }
    mapa=mapa1;
  }

  PII best=MP(-1,-1);
  FORE(it,mapa) REP(i,SIZE((*it).SE)) best=max(best,MP((*it).SE[i].SE,-(*it).SE[i].FI));
  printf(" %s",t[-best.SE].c_str());
}

int main()
{
  scanf("%d",&ILE);
  FOR(iii,1,ILE)
  {
    printf("Case #%d:",iii);
    fprintf(stderr,"Case #%d: \n",iii);
    scanf("%d%d",&n,&m);
    t.clear();
    REP(i,n)
    {
      scanf("%s",st);
      t.PB(string(st));
    }
    REP(i,m)
    {
      scanf("%s",st);
      s=string(st);
      doit();
    }
    puts("");
  }
  return 0;
}
