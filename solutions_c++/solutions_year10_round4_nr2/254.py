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
int p,n;
int t[2000],koszt[2000];

int tab[2000][100];

void doit()
{
  FOR(i,1,n-1) REP(j,100) tab[i][j]=500000001;
  FORD(i,n-1,n/2)
  {
    int a=2*i-n, b=a+1;
    assert(b<n);
    tab[i][min(t[a],t[b])] = min(tab[i][min(t[a],t[b])], koszt[i]);
    if (min(t[a],t[b])>0)
      tab[i][min(t[a],t[b])-1] = min(tab[i][min(t[a],t[b])-1], 0);
    FORD(j,98,0) tab[i][j]=min(tab[i][j],tab[i][j+1]);
  }

  FORD(i,n/2-1,1)
  {
    int a=2*i, b=2*i+1;
    REP(j,100)
    {
      tab[i][j]=min(tab[i][j], tab[a][j]+tab[b][j]+koszt[i]); // kup
      if (j<99) tab[i][j]=min(tab[i][j], tab[a][j+1]+tab[b][j+1]); // nie kup
    }
    FORD(j,98,0) tab[i][j]=min(tab[i][j],tab[i][j+1]);
  }
  printf("%d\n",tab[1][0]);
}

int main()
{
  scanf("%d",&ILE);
  FOR(iii,1,ILE)
  {
    printf("Case #%d: ",iii);
    scanf("%d",&p);
    n=(1<<p);
    REP(i,n) { scanf("%d",t+i); t[i]=min(t[i],50); }
    FORD(q,p-1,0)
      FOR(i,(1<<q),2*(1<<q)-1) scanf("%d",koszt+i);
    doit();
  }
  return 0;
}
