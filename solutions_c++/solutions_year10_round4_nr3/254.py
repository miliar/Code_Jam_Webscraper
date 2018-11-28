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

int ILE;
int r;
#define M 400
int t[M][M];
int t1[M][M];

int main()
{
  scanf("%d",&ILE);
  FOR(iii,1,ILE)
  {
    printf("Case #%d: ",iii);
    scanf("%d",&r);
    REP(i,M) REP(j,M) t[i][j]=0;
    while (r--)
    {
      int a,b,c,d;
      scanf("%d%d%d%d",&a,&b,&c,&d);
      FOR(i,a,c) FOR(j,b,d) t[i][j]=1;
    }
    int wyn=0;
    while (1)
    {
      REP(i,M) REP(j,M) t1[i][j]=0;
      bool jest=0;
      wyn++;
      REP(i,M) REP(j,M)
        if (t[i][j])
        {
          if (i>0 && t[i-1][j] || j>0 && t[i][j-1]) { t1[i][j]=1; jest=1; }
        } else
        {
          if (i>0 && j>0 && t[i-1][j] && t[i][j-1]) { t1[i][j]=1; jest=1; }
        }
      if (!jest) break;
      REP(i,M) REP(j,M) t[i][j]=t1[i][j];
    }
    printf("%d\n",wyn);
  }
  return 0;
}
