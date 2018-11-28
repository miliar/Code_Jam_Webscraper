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


/* My ACM ICPC team's library. */

const int dim=11;
struct mat { ll t[dim][dim]; };
int d; /* wlasciwy rozmiar macierzy */

mat operator* (mat a,mat b)
{
  mat c;
  REP(i,d) REP(j,d)
  {
    c.t[i][j]=0;
    REP(k,d)
    {
      c.t[i][j]+=a.t[i][k]*b.t[k][j];
    }
  }
  return c;
}

mat jeden;

mat pot(mat x,int n)
{
	mat a(jeden),b(x);
	while (n>0)
		if (n%2) { a=a*b; n--; }
		else { b=b*b; n/=2; }
	return a;
}

int ILE;
int r,k,n;
int t[20];

int main()
{
  scanf("%d",&ILE);
  FOR(iii,1,ILE)
  {
    printf("Case #%d: ",iii);
    scanf("%d%d%d",&r,&k,&n);
    REP(i,n) scanf("%d",t+i);
    d=n+1;
    REP(i,d) REP(j,d) jeden.t[i][j]=0; REP(i,d) jeden.t[i][i]=1;
    mat M;
    REP(i,d) REP(j,d) M.t[i][j]=0;
    REP(i,n)
    {
      int sum=0;
      int j=0;
      while (j<n)
      {
        sum+=t[(i+j)%n];
        if (sum>k) break;
        j++;
      }
      if (j<n) sum-=t[(i+j)%n];
      M.t[(i+j)%n][i]=1;
      M.t[n][i]=sum;
    }
    M.t[n][n]=1;
//    REP(i,n+1) { REP(j,n+1) printf("%lld ",M.t[i][j]); puts(""); }
    mat N=pot(M,r);
    printf("%lld\n",N.t[n][0]);
  }
  return 0;
}
