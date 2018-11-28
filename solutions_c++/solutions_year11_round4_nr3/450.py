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
int n;

int ile[1010];

int p[1010];
int dz[1010];

inline int doit(VI t)
{
  FOR(i,1,1000) ile[i]=0;
  int wyn=0;

  REP(ii,SIZE(t))
  {
    int m=t[ii];
    if (m==1) { if (!ii) wyn++; continue; }
    VI pom;
    while (m>1)
    {
      pom.PB(dz[m]);
      m/=dz[m];
    }
    sort(ALL(pom));
    //REP(i,SIZE(pom)) printf("%d ",pom[i]); puts("");
    int i=0;
    int ok=0;
    while (i<SIZE(pom))
    {
      int i0=i;
      while (i0<SIZE(pom) && pom[i]==pom[i0])
      {
        i0++;
      }
      if (ile[pom[i]]<i0-i) ok=1;
      ile[pom[i]]=max(ile[pom[i]],i0-i);
      i=i0;
    }
    wyn+=ok;
  }
  return wyn;
}

int main()
{
  FOR(i,2,1000) p[i]=1;
  FOR(i,2,1000) if (p[i])
  {
    dz[i]=i;
    int j=i*i;
    while (j<1000) { p[j]=0; if (!dz[j]) dz[j]=i; j+=i; }
  }

  scanf("%d",&ILE);
  FOR(iii,1,ILE)
  {
    printf("Case #%d: ",iii);
    fprintf(stderr,"Case #%d: \n",iii);
    scanf("%d",&n);
    VI t;
    FOR(i,1,n) t.PB(i);
    //int a=doit(t);
    int a=1;
    FOR(i,2,n) if (p[i])
    {
      int j=i;
      while (j<=n)
      {
        a++;
        j*=i;
      }
    }
    int b=0;
    FOR(i,2,n) if (p[i]) b++;
    //reverse(ALL(t));
    //int b=doit(t);
    printf("%d\n",a-max(b,1));
  }
  return 0;
}
