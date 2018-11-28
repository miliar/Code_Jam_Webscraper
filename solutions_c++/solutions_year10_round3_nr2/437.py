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
typedef long long LL;
const int inf=0x3f3f3f3f;
const LL infLL=0x3f3f3f3f3f3f3f3fLL;
const double eps=1e-7;
template<class T> inline void checkmin(T &a,const T &b) {if (b<a) a=b;}
template<class T> inline void checkmax(T &a,const T &b) {if (b>a) a=b;}

int T,l,p,c;

int main()
{
#ifndef ONLINE_JUDGE
	freopen("B-small-attempt1.in","r",stdin);
	freopen("B.out","w",stdout);
#endif
	scanf("%d",&T);
	for (int t=1;t<=T;++t) {
		scanf("%d%d%d",&l,&p,&c);
		int ans=0;
		int rate=(int)ceil((double)p/(double)l-eps);
		while (rate>c) {
			++ans;
			rate=(int)ceil(sqrt((double)rate)-eps);
		}
		printf("Case #%d: %d\n",t,ans);
	}

}
