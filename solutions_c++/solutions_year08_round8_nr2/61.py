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

int ILE;
int n;
map<string,int> mapa;
#define MX 10000

pair<int,PII> t[400];

int main()
{
  scanf("%d",&ILE);
  FOR(LICZ,1,ILE)
  {
    printf("Case #%d: ",LICZ);
    scanf("%d",&n);
    mapa.clear();
    int ile=0;
    REP(i,n)
    {
      char st[100];
      int a,b;
      scanf("%s%d%d",st,&a,&b);
      string s(st);
      int x=-1;
      if (mapa.count(s)) x=mapa[s]; else x=(mapa[s]=ile++);
      a--; b--;
      t[i]=MP(x,MP(a,b));
    }
    int wyn=1000;
    REP(mask,(1<<n)) if (mask)
    {
      set<int> zb;
      vector<PII> tab;
      REP(i,n) if (mask&(1<<i)) { zb.insert(t[i].FI); tab.PB(t[i].SE); }
      if (SIZE(zb)>3) continue;
      sort(ALL(tab));
      if (tab[0].FI!=0) continue;
      int mx=tab[0].SE;
      bool ok=1;
      REP(i,SIZE(tab)) { if (tab[i].FI>mx+1) { ok=0; break; } mx=max(mx,tab[i].SE); }
      if (mx!=MX-1 || !ok) continue;
      wyn=min(wyn,SIZE(tab));
    }
    if (wyn==1000) puts("IMPOSSIBLE"); else printf("%d\n",wyn);
  }
  return 0;
}
