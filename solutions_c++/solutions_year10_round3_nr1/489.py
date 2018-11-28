#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cstdio>
#include <cassert>
#include <iostream>
#include <sstream>
#include <map>
#include <vector>
#include <set>
#include <algorithm>
#define zbwmqlw
#define min(a,b) ((a)<(b)?(a):(b))
#define max(a,b) ((a)>(b)?(a):(b))
#define pow(x) (1<<(x))
#define powLL(x) ((1LL)<<(LL)(x))
#define sqr(x) ((x)*(x))
#define abs(x) ((x)>0?(x):-(x))
#define lch(x) (((x)<<1)+1)
#define rch(x) (((x)<<1)+2)
#define PI 3.141592653589793238463
#define MP(x,y) make_pair(x,y)
#define PB(x) push_back(x)
#define fill(x,y) memset((x),(y),sizeof(x))
#define orz(x,l,r) for ((x)=(l);(x)<=(r);++(x))
#define sro(x,r,l) for ((x)=(r);(x)>=(l);--(x))

#ifndef NEXT
using namespace std;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;
typedef pair<int,int> PII;
typedef pair<double,double> PDD;
#endif
typedef long long LL;
const int inf=0x3f3f3f3f;
const LL infLL=0x3f3f3f3f3f3f3f3fLL;
const double eps=1e-7;
template<class T> inline void checkmin(T &a,const T &b) {if (b<a) a=b;}
template<class T> inline void checkmax(T &a,const T &b) {if (b>a) a=b;}

const int N=10005;
int c[N];
int T,n;
PII p[N];
int ans;

int query(int p)
{
	int ret=0;
	for (;p<N;p+=p&-p) ret+=c[p];
	return ret;
}
void modify(int p,int v)
{
	for (;p>0;p-=p&-p) c[p]+=v;
}

int main()
{
#ifndef ONLINE_JUDGE
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
#endif
	scanf("%d",&T);
	for (int t=1;t<=T;++t) {
		scanf("%d",&n);
		memset(c,0,sizeof(c));
		for (int i=1;i<=n;++i) scanf("%d%d",&p[i].first,&p[i].second);
		sort(p+1,p+n+1);
		ans=0;
		for (int i=1;i<=n;++i) {
			ans+=query(p[i].second+1);
			modify(p[i].second,1);
		}
		printf("Case #%d: %d\n",t,ans);
	}

}
