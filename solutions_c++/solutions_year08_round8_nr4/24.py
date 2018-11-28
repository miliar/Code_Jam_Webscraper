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

#define MD 30031

int ILE;
int n,k,p;
int t[1010][1<<10];

int main()
{
  scanf("%d",&ILE);
  FOR(LICZ,1,ILE)
  {
    printf("Case #%d: ",LICZ);
    scanf("%d%d%d",&n,&k,&p);
    memset(t,0,sizeof(t));
    int mask0=(1<<k)-1; mask0=mask0<<(p-k);
    t[k-1][mask0]=1;
//    printf("%d\n",mask0);
    FOR(i,k-1,n-2) REP(mask,(1<<p)) if (t[i][mask])
    {
      if (mask&1) { int m0=(mask>>1)+(1<<(p-1)); t[i+1][m0]=(t[i+1][m0]+t[i][mask])%MD; continue; }
      int m0=mask>>1;
      REP(j,p) if (m0&(1<<j))
      {
        int m1=(m0^(1<<j))|(1<<(p-1));
        t[i+1][m1]=(t[i+1][m1]+t[i][mask])%MD;
      }
    }
    printf("%d\n",t[n-1][mask0]%MD);
  }
  return 0;
}
