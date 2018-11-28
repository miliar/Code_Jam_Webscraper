#include <cstdio>
#include <algorithm>
#include <cstring>
using namespace std;
#define oo 1005
#define inf 100000000
int Test,Case;
int L,P,C;

inline void Readin()
{
	scanf("%d%d%d",&L,&P,&C);
}

inline int val(long long C,long long x)
{
	return (x+C-1)/C;
}

inline int Val(long long x,long long y,long long z)
{
	return max(val(x,y),val(y,z));
}

int Work(long long l,long long r)
{
	long long L=l,R=r;
	if (l*C>=r) return 0;
	/*while (l+1000<r)
	{
		int mid1=l+(r-l)/3,mid2=l+(r-l)/3*2;
		int v1=Val(L,mid1,R),v2=Val(L,mid2,R);
		
		if (v1<v2) r=mid2;
		else l=mid1;
	}*/
	
	while (l+1<r)
	{
		int mid=l+r>>1;
		if (val(L,mid)<=val(mid,R)) l=mid;
		else r=mid;
	}
	
	int best=l;
	for (int i=l+1;i<r;++i)
		if (Val(L,best,R)>Val(L,i,R)) best=i;
	
	if (val(L,best)<val(best,R)) return Work(best,R)+1;
	return Work(L,best)+1;
}

inline void Solve()
{
	printf("%d\n",Work(L,P));

}

int main()
{
	//freopen("B-small-attempt0.in","r",stdin);
	
	for (scanf("%d",&Test);Test--;)
	{
		printf("Case #%d: ",++Case);
		Readin();
		Solve();
	}
	
	return 0;
}
