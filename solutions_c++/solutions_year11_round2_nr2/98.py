#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>

using namespace std;

const int maxn=210;
const double eps=1e-10;

int wei[maxn],cnt[maxn];

int main()
{
	int cas=1;
	freopen("B-large.in","r",stdin);
	freopen("outBLB.txt","w",stdout);
	int T;scanf("%d",&T);
	while(T--)
	{
		int i,j;
		int C,D;scanf("%d%d",&C,&D);
		for(i=0;i<C;++i)
			scanf("%d%d",wei+i,cnt+i);
		double head=0,tail=1e13,mid=(head+tail)/2;
		double l,r;
		for(int ii=0;ii<80&&tail-head>1e-8;++ii)
		{
			int f=0;
			l=wei[0]-mid;
			r=l+(double)(cnt[0]-1)*D;
			if(r-wei[0]-mid>eps) f=1;
			r+=D;
			for(i=1;i<C&&!f;++i)
			{
				double ll=wei[i]-mid;
				if(r-ll>eps) ll=r;
				double rr=ll+(double)(cnt[i]-1)*D;
				if(rr-wei[i]-mid>eps) f=1;
				rr+=D;
				l=ll,r=rr;
			}
			if(f) head=mid;
			else tail=mid;
			mid=(head+tail)/2;
		}
		printf("Case #%d: %.8f\n",cas++,mid);
	}
}