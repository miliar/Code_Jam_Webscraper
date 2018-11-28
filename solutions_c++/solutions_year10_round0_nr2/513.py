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
const int N=51;
int t,T,n;
LL val[N];
LL yt[N];

LL gcd(LL a,LL b)
{return b==0?a:gcd(b,a%b);}

void pusu()
{
	for (scanf("%d",&T),t=1;t<=T;++t) {
		scanf("%d",&n);
		LL last,cur,ans;
		for (int i=1;i<=n;++i) scanf("%I64d",&yt[i]);
		sort(yt+1,yt+n+1);
		for (int i=1;i<n;++i) val[i]=yt[i+1]-yt[i];
		LL d=val[1];
		for (int i=2;i<n;++i) d=gcd(d,val[i]);
		ans=-yt[n];
		ans%=d;
		ans+=d*(ans<0);
		printf("Case #%d: %I64d\n",t,ans);
	}
}

int main()
{
#ifndef ONLINE_JUDGE
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
#endif
	pusu();
}