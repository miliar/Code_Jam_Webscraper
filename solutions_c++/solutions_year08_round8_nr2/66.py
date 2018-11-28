#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <deque>
#include <list>
#include <map>
#include <set>
using namespace std;
#define all(a) (a).begin(),(a).end()
#define mset(a,v) memset(a,v,sizeof(a))
#define pb push_back
#define mp make_pair
#define sz(a) (int)(a).size()
#define rep(i,n) for(i=0; i<n; ++i)
#define forr(i,a,b) for(i=a; i<=b; ++i)
#define ford(i,a,b) for(i=a; i>=b; --i)
#define X first
#define Y second
template<class T> inline void smin(T& a, const T& b) { if(a>b) a=b; }
template<class T> inline void smax(T& a, const T& b) { if(a<b) a=b; }
template<class T> T gcd(T a, T b) { return (b!=0) ? gcd(b,a%b) : a; }
typedef long long ll;
typedef vector<int> VI;
typedef pair<int,int> PII;

int i,j,n, i1,i2,i3, ans, U,N;
string c[400];
int a[400],b[400], d[10001];
bool r[400][400];
VI y;

int main()
{
	freopen("b-small-attempt0.in","r",stdin);//large-small-attempt0
	freopen("b-small.out","w",stdout);
	scanf("%d",&N);
	rep(U,N)
	{
    ans=-1;
		cin>>n;
		rep(i,n) cin>>c[i]>>a[i]>>b[i];
		rep(i,n) rep(j,n) r[i][j]=(c[i]==c[j]);
		rep(i1,n) forr(i2,i1,n-1) forr(i3,i2,n-1)
		{
      y.clear();
      mset(d,-1);
      rep(i,n) if(r[i][i1] || r[i][i2] || r[i][i3]) y.pb(i);
      d[0]=0;
      forr(j,1,10000) rep(i,sz(y)) if(a[y[i]]<=j && j<=b[y[i]])
      {
        if(d[a[y[i]]-1]>=0)
        {
          if(d[j]==-1 || d[j]>d[a[y[i]]-1]+1) d[j]=d[a[y[i]]-1]+1;
        }
      }
 //     cout<<d[10000]<<endl;
      if(d[10000]>0)
      {
        if(ans==-1) ans=d[10000];
        else smin(ans, d[10000]);
      }
    }
		printf("Case #%d: ",U+1);
		if(ans==-1) printf("IMPOSSIBLE\n");
		else printf("%d\n",ans);
	}
	return 0;
}
