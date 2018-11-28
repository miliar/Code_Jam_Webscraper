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

int ILE;

int n,q;
char t[30][30];

#define SR 1000
#define MAX 2000

int d[22][22][MAX+10];

vector<pair<PII,int> > kol;

int x[]={-1,1,0,0};
int y[]={0,0,-1,1};
inline bool ins(int g,int h) { return g>=0 && g<h; }

void bfs()
{
  REP(i,n) REP(j,n) REP(k,MAX) d[i][j][k]=INFTY;
  kol.clear();
  REP(i,n) REP(j,n) if (isdigit(t[i][j])) { d[i][j][SR]=0; kol.PB(MP(MP(i,j),SR)); }
  REP(ii,SIZE(kol))
  {
    PII p=kol[ii].FI; int u=kol[ii].SE;
//    assert((p.FI-p.SE)%2==0);
    REP(z,4)
    {
      int a1=p.FI+x[z], b1=p.SE+y[z];
      if (!ins(a1,n) || !ins(b1,n)) continue;
      int znak=(t[a1][b1]=='+' ? 1 : -1);
      REP(k,4)
      {
        int a2=a1+x[k], b2=b1+y[k];
        if (!ins(a2,n) || !ins(b2,n)) continue;
        int ni=a2,nj=b2,ns=u+znak*(t[p.FI][p.SE]-'0');
        if (ns>=0 && ns<MAX && d[ni][nj][ns]>d[p.FI][p.SE][u]+1)
        {
          d[ni][nj][ns]=d[p.FI][p.SE][u]+1;
          kol.PB(MP(MP(ni,nj),ns));
        }
      }
    }
  }
}

vector<PII> akt,akt1;
string w;

void pisz(vector<PII> xx) { printf("v: "); REP(i,SIZE(xx)) printf("(%d,%d) ",xx[i].FI,xx[i].SE); puts(""); }

void doit(int len,int A)
{
  assert(!akt.empty());
  if (!len)
  {
    assert(A==SR);
    return;
  }

  vector<pair<string,PII> > pom;
  REP(ii,SIZE(akt))
  {
    int a=akt[ii].FI,b=akt[ii].SE;
    REP(z,4)
    {
      int a1=a+x[z], b1=b+y[z];
      if (!ins(a1,n) || !ins(b1,n)) continue;
      REP(k,4)
      {
        int a2=a1+x[k], b2=b1+y[k];
        if (!ins(a2,n) || !ins(b2,n)) continue;
        int znak=(t[a1][b1]=='+' ? 1 : -1), cyfra=(t[a2][b2]-'0');
        string ss; ss+=t[a1][b1]; ss+=t[a2][b2];
        int u=A-znak*cyfra;
        if (u>=0 && u<MAX && d[a2][b2][u]==len-1) pom.PB(MP(ss,MP(a2,b2)));
      }
    }
  }
  assert(!pom.empty());
  sort(ALL(pom));
  string ss=pom[0].FI;
  w+=ss;
  int znak=(ss[0]=='+' ? 1 : -1), cyfra=(ss[1]-'0');
  A-=znak*cyfra;
  akt.clear();
  REP(i,SIZE(pom)) if (pom[i].FI==ss) akt.PB(pom[i].SE);
  sort(ALL(akt)); akt.erase(unique(ALL(akt)),akt.end());
  doit(len-1,A);
}

int main()
{
  scanf("%d",&ILE);
  FOR(LICZ,1,ILE)
  {
    printf("Case #%d:\n",LICZ);
    scanf("%d%d",&n,&q);
    REP(i,n) scanf("%s",t[i]);
    bfs();
    while (q--)
    {
      int a;
      scanf("%d",&a);
      a+=SR;
      int best=INFTY;
      REP(i,n) REP(j,n) best=min(best,d[i][j][a-(t[i][j]-'0')]);
      akt.clear();
      int b1=100;
      REP(i,n) REP(j,n) if (d[i][j][a-(t[i][j]-'0')]==best) b1=min(b1,t[i][j]-'0');
      REP(i,n) REP(j,n) if (d[i][j][a-(t[i][j]-'0')]==best && b1==(t[i][j]-'0')) akt.PB(MP(i,j));
      w=""; w+=char('0'+b1);
      doit(best,a-b1);
      puts(w.c_str());
    }
  }
  return 0;
}
