#include <string.h>
#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <assert.h>
#include <iostream>
#include <sstream>
#include <map>
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
#define fill(x,y) memset((x),(y),sizeof(x))
#define rep(x,l,r) for ((x)=(l);(x)<=(r);++(x))
#define repd(x,r,l) for ((x)=(r);(x)>=(l);--(x))

//using namespace std;
using std::pair;
using std::make_pair;
using std::cin;
using std::cout;
using std::endl;
using std::stringstream;
using std::iostream;
using std::sort;
typedef long long LL;
const int inf=0x3f3f3f3f;
const LL infLL=0x3f3f3f3f3f3f3f3fLL;
const double eps=1e-7;
template<class T> inline void checkmin(T &a,const T &b) {if (b<a) a=b;}
template<class T> inline void checkmax(T &a,const T &b) {if (b>a) a=b;}

const int N=2005;

int t,T,r,R,n;
LL s[N][11];
int cap,g[N];

int main()
{
#ifndef ONLINE_JUDGE
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
#endif
	for (scanf("%d",&T),t=1;t<=T;++t) {
		scanf("%d%d%d",&R,&cap,&n);
		for (int i=0;i<n;++i) scanf("%d",&g[i]);
		memcpy(g+n,g,n<<2);
		for (int i=0;i<n+n;++i) s[i][0]=g[i];
		for (int k=1;k<=10;++k) for (int i=0;i<n+n;++i) {
			s[i][k]=s[i][k-1];
			if (i+pow(k-1)<n+n) s[i][k]+=s[i+pow(k-1)][k-1];
		}
		int cur=0;
		LL ans=0;
		for (r=0;r<R;++r) {
			int rem=cap,rnum=n;
			for (int k=10;k>=0;--k) if (pow(k)<=rnum && s[cur][k]<=rem) {
				rem-=s[cur][k];
				rnum-=pow(k);
				cur+=pow(k);
				cur%=n;
			}
			ans+=cap-rem;
		}
		printf("Case #%d: %I64d\n",t,ans);
	}
}