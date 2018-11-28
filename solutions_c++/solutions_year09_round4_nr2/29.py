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

int n,m,f;
char t[100][100];

int tab[52][52][52][52];

//int MX;

inline bool free(int i,int a,int b,int j)
{
  return t[i][j]=='.' || a<=j && j<=b;
}

int skok[52][52];

int doit(int i,int a,int b,int j)
{
  int &w=tab[i][a][b][j];
  if (w>=0) return w;
  if (i==n-1) return w=0;
  w=INFTY;
  
  int l=j,r=j;
  while (l>0 && t[i+1][l-1]=='#' && free(i,a,b,l-1)) l--;
  while (r<m-1 && t[i+1][r+1]=='#' && free(i,a,b,r+1)) r++;
  // skok w lewo
  if (l>0 && free(i,a,b,l-1) && t[i+1][l-1]=='.')
  {
    if (skok[i][l-1]<=f) w=min(w,doit(i+skok[i][l-1],1,0,l-1));
  }
  // skok w prawo
  if (r<m-1 && free(i,a,b,r+1) && t[i+1][r+1]=='.')
  {
    if (skok[i][r+1]<=f) w=min(w,doit(i+skok[i][r+1], 1,0, r+1));
  }
  FOR(a1,l,r) FOR(b1,a1,r)
  {
    if (a1==l && b1==r) continue;
    if (a1!=l && skok[i+1][a1]<=f-1)
    {
      int pocz=a1,kon=b1;
      if (skok[i+1][a1]>0) { pocz=1; kon=0; }
      w=min(w,b1-a1+1 + doit(i+1+skok[i+1][a1], pocz, kon, a1));
    }
    if (b1!=r && skok[i+1][b1]<=f-1)
    {
      int pocz=a1,kon=b1;
      if (skok[i+1][b1]>0) { pocz=1; kon=0; }
      w=min(w,b1-a1+1 + doit(i+1+skok[i+1][b1], pocz, kon, b1));
    }
  }
  return w;
}

void prec()
{
  REP(j,m) skok[n-1][j]=0;
  FORD(i,n-2,0) REP(j,m) if (t[i+1][j]=='#') skok[i][j]=0; else skok[i][j]=skok[i+1][j]+1;
//  REP(i,n) { REP(j,m) printf("%d ",skok[i][j]); puts(""); }
}

int main()
{
  scanf("%d",&ILE);
  FOR(LICZ,1,ILE)
  {
    printf("Case #%d: ",LICZ);
    scanf("%d%d%d",&n,&m,&f);
    REP(i,n) scanf("%s",t[i]);
    REP(i,n) { t[i][m]='#'; t[i][m+1]='\0'; } // just in case
//    MX=2*n;
    REP(i,50) REP(j,51) REP(k,51) REP(l,50) tab[i][j][k][l]=-1;
    prec();
    int w=doit(0,1,0,0);
    if (w>=INFTY) puts("No"); else printf("Yes %d\n",w);
  }
  return 0;
}
