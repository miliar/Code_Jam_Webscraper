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
int n,m;
char st[1010];
int t[510][510];
int t1[510][510];

inline int daj(int a,int b,int c,int d)
{
  assert(c>=0 && d>=0 && c<n && d<m);
  return t1[c][d] - (a<=0 ? 0 : t1[a-1][d]) - (b<=0 ? 0 : t1[c][b-1]) + ((a<=0 || b<=0) ? 0 : t1[a-1][b-1]);
}

void dp()
{
  REP(i,n) REP(j,m) t1[i][j]=t[i][j];
  REP(i,n) FOR(j,1,m-1) t1[i][j]+=t1[i][j-1];
  REP(j,m) FOR(i,1,n-1) t1[i][j]+=t1[i-1][j];
  //REP(i,n) { REP(j,m) printf("%d ",t1[i][j]); puts(""); }
}

inline bool rowno(int a,int b,int c,int d,int kp,int dx,int dy)
{
  dx-=-kp*t[a][b]-kp*t[a][d]+kp*t[c][b]+kp*t[c][d];
  dy-=-kp*t[a][b]-kp*t[c][b]+kp*t[a][d]+kp*t[c][d];
  return !dx && !dy;
}

int main()
{
  scanf("%d",&ILE);
  FOR(iii,1,ILE)
  {
    printf("Case #%d: ",iii);
    fprintf(stderr,"Case #%d: \n",iii);
    int d;
    scanf("%d%d%d",&n,&m,&d);
    REP(i,n)
    {
      scanf("%s",st);
      assert((int)strlen(st)==m);
      REP(j,m) t[i][j]=st[j]-'0';
    }
    dp(); //FOR(i,2,3) FOR(j,3,4) printf("(1 2) (%d %d) %d\n",i,j,daj(1,2,i,j));
    bool ok=0;
    FORD(k,min(n,m),3)
    {
      bool jest=0;
      REP(i,n-k+1) if (!jest) REP(j,m-k+1)
      {
        if (jest) break;
        int dx=0,dy=0;
        REP(a,k) REP(b,k)
        {
          if (a==0 && b==0 || a==k-1 && b==0 || a==0 && b==k-1 || a==k-1 && b==k-1) continue;
          int ii=i+a,jj=j+b;
          int co=-(k-1)+2*a;
          dx+=co*t[ii][jj];
          int co1=-(k-1)+2*b;
          dy+=co1*t[ii][jj];
        }
        if (!dx && !dy) { jest=true; break; }
      }
      if (jest)
      {
        printf("%d\n",k);
        ok=true;
        break;
      }
    }
    if (!ok) puts("IMPOSSIBLE");
  }
  return 0;
}
