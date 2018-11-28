/* Jakub Radoszewski (jakubr) */

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

int ILE;
int n;
PII drz[200000];

VI doit(int v)
{
  VI w; REP(i,2) w.PB(INFTY);
  PII p=drz[v];
  if (p.SE==-1)
  {
    w[p.FI]=0;
    return w;
  }
  VI l=doit(2*v),r=doit(2*v+1);
  REP(br,2)
  {
    if (br!=p.FI && !p.SE) continue;
    int cost=0;
    if (br!=p.FI) cost=1;
    if (br==1)
    {
      REP(e,2) REP(f,2) w[e&&f]=min(w[e&&f],l[e]+r[f]+cost);
    } else
    {
      REP(e,2) REP(f,2) w[e||f]=min(w[e||f],l[e]+r[f]+cost);
    }
  }
  return w;
}

int v;

int main()
{
  scanf("%d",&ILE);
  FOR(LICZ,1,ILE)
  {
    printf("Case #%d:",LICZ);
    scanf("%d%d",&n,&v);
    int j=1;
    FOR(i,1,(n-1)/2)
    {
      int a,b;
      scanf("%d%d",&a,&b);
      drz[i]=MP(a,b);
      j=i;
    }
    FOR(i,1,(n+1)/2)
    {
      int a;
      scanf("%d",&a);
      drz[i+j]=MP(a,-1);
    }
    VI w=doit(1);
    if (w[v]>=INFTY) puts(" IMPOSSIBLE"); else printf(" %d\n",w[v]);
  }
  return 0;
}
