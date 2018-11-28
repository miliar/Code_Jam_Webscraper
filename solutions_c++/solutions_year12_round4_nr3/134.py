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

int x[2010];
int n;
int w[2010];

void doit()
{
  FOR(i,1,n-1) if (x[i]<=i) { puts("Impossible"); return; }
  FOR(i,1,n-1) FOR(j,i+1,x[i]-1) if (x[j]>x[i]) { puts("Impossible"); return; }

  w[n]=w[n+1]=1000000000;
  x[n]=n+1;
  vector<PII> kol;
  kol.PB(MP(1,n));
  REP(iii,SIZE(kol))
  {
    int pocz=kol[iii].FI,kto=kol[iii].SE;
    int nas=x[kto];
    VI pom;
    FOR(i,pocz,kto-1) if (x[i]==kto) pom.PB(i);
    if (pom.empty()) { puts("Impossible"); fprintf(stderr,"Error 1\n"); return; }
    int p=pom[0];
    long double A=(long double)(w[nas]-w[kto])/(nas-kto);
    long double B=kto-p;
    long double C=w[kto]-A*B;
    if (C-int(floorl(C))<1e-9) C-=1.0;
    if (C<-0.5) { fprintf(stderr,"UJEMNE!!!"); return; }
    int h=int(floorl(C));
    int pop=pocz;
    REP(i,SIZE(pom))
    {
      w[pom[i]]=h;
      if (pom[i]-pop) kol.PB(MP(pop,pom[i]));
      pop=pom[i]+1;
    }
  }
  FOR(i,1,n) printf("%d ",w[i]); puts("");
}

int main()
{
  scanf("%d",&ILE);
  FOR(iii,1,ILE)
  {
    printf("Case #%d: ",iii);
    fprintf(stderr,"Case #%d: \n",iii);
    scanf("%d",&n);
    REP(i,n-1) scanf("%d",x+i+1);
    doit();
  }
  return 0;
}
