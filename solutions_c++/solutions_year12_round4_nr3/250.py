#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <cmath>
using namespace std;

const int maxn	=	2005;

int height[maxn],peak[maxn],n;

inline bool change(int l)
{
	int mid=peak[l];
	double h=0;
	for (int i=l+1;i<mid;++i){
		double k=(height[i]-height[l])/(double)(i-l);
		h=max(h,k*(mid-l)+height[l]);
	}
	if (height[mid]<=h){
		int delta=(int)floor(h)+1-height[mid];
		for (int i=mid;i<=n;++i) height[i]+=delta;
		return true;
	}
	for (int i=mid+1;i<n;++i){
		double k=(height[i]-height[l])/(double)(i-l);
		h=max(h,k*(mid-l)+height[l]);
	}
	if (height[mid]<h){
		int delta=(int)ceil(h)-height[mid];
		for (int i=mid;i<=n;++i) height[i]+=delta;
		return true;
	}
	return false;
}

inline bool solve(int l,int r)
{
//printf("%d %d	%d\n",l,r,peak[l]);
	if (l+1>=r){
		for (int i=l;i<=r;++i) height[i]=0;
		return true;
	}
	int mid=peak[l];
	for (int i=l;i<mid;++i) if (peak[i]>mid) return false;
	if (!solve(l+1,mid-1) || !solve(mid,r)) return false;
	height[l]=0;
	for (int i=l+1;i<=mid;++i){
		height[l]=max(height[l],height[i]+1);
	}
	for (int i=l;i<mid;++i)
		change(i);
	return true;
}

inline bool solve()
{
	memset(height,0,sizeof(height));
	for (int it=0;it<200000;++it){
		bool fl=false;
		for (int i=0;i<n-1;++i)
		if (change(i)) fl=true;
		if (!fl) return true;
	}
	return false;
}


int main()
{
	freopen("C_small_x.in","r",stdin);
	freopen("C.out","w",stdout);
	
	int T,test=1;
	for (scanf("%d",&T);test<=T;++test){
		scanf("%d",&n);
		for (int i=0;i<n-1;++i){
			scanf("%d",&peak[i]);
			--peak[i];
		}
		if (!solve()) printf("Case #%d: Impossible\n",test);
		else{
			printf("Case #%d:",test);
			for (int i=0;i<n;++i) printf(" %d",height[i]);
			puts("");
		}
	}
	return 0;
}
