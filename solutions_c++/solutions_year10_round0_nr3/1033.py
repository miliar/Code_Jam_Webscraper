#include<iostream>
using namespace std;
int countbit(int a){return a?1+countbit(a&(a-1)):0;}
int d[2001];
int cishu[1100000];
__int64 renshu[1100000];
int main()
{
	freopen("C-Large.in","r",stdin);
	freopen("C-Large.out","w",stdout);
	int cs,css,r,rr,i,j,n,k,size,go,st,ed;
	__int64 tsum,sum;
	scanf("%d",&cs);
	for(css=1;css<=cs;css++)
	{
		scanf("%d%d%d",&r,&k,&n);
		memset(renshu,0,sizeof(renshu));
		memset(cishu,0,sizeof(cishu));
		for(i=1;i<=n;i++)
		{
			scanf("%d",&d[i]);
			d[i+n]=d[i];
		}
		st=ed=0;
		for(sum=sum=0,rr=1;rr<=r;rr++)
		{
			st=ed+1;
			if(st>n)st=1;
			for(tsum=0,j=0;j<n;j++)
				if(tsum+d[st+j]>k)break;
				else tsum+=d[st+j];
			sum+=tsum;
			ed=st+j-1;
			if(ed>n)ed-=n;
			if(cishu[st*1000+ed])
			{

				sum=(r-cishu[st*1000+ed])/(rr-cishu[st*1000+ed])*(sum-renshu[st*1000+ed])+renshu[st*1000+ed];
				r-=cishu[st*1000+ed];
				r-=r/(rr-cishu[st*1000+ed])*(rr-cishu[st*1000+ed]);
				for(rr=1;rr<=r;rr++)
				{
					st=ed+1;
					if(st>n)st=1;
					for(tsum=0,j=0;j<n;j++)
						if(tsum+d[st+j]>k)break;
						else tsum+=d[st+j];
					ed=st+j-1;
					if(ed>n)ed-=n;
					sum+=tsum;
				}
				break;
			}
			else
			{
				cishu[st*1000+ed]=rr;
				renshu[st*1000+ed]=sum;
			}
		}
		printf("Case #%d: %I64d\n",css,sum);
	}
	return 0;
 }
