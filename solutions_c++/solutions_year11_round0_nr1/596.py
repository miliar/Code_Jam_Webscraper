#include<iostream>
using namespace std;
#define MAXN 105
struct Node
{
	int id,pos;
}job[MAXN];
int job0[MAXN],job1[MAXN];
int kjob0,kjob1;
int main()
{
//	freopen("A-large.in","r",stdin);
//	freopen("A.out","w",stdout);
	int ct,tt=0;
	int i;
	int ok0,ok1,step0,step1,ans,pos0,pos1;
	int n;
	char temp;
	scanf("%d",&ct);
	while(ct--)
	{
		scanf("%d ",&n);
		kjob0=kjob1=ok0=ok1=0;
		for(i=0;i<n;i++)
		{
			if(i==n-1)scanf("%c %d",&temp,&job[i].pos);
			else scanf("%c %d ",&temp,&job[i].pos);
			if(temp=='O'){job[i].id=0;job0[kjob0++]=job[i].pos;}
			else {job[i].id=1;job1[kjob1++]=job[i].pos;}
		}
		ans=0;
		pos0=pos1=1;
		for(i=0;i<n;i++)
		{
			if(kjob0==ok0 && kjob1==ok1)break;
			if(job[i].id==0)
			{
				step0=abs(job0[ok0]-pos0)+1;
				ans+=step0;
				pos0=job0[ok0++];
				if(ok1<kjob1)
				{
					if(abs(job1[ok1]-pos1)<=step0)//说明1号在0号搞定的时候已经走到指定位置
					{
						pos1=job1[ok1];
					}else//说明1号在0号搞定的时候走不到指定位置
					{
						if(pos1<job1[ok1])pos1+=step0;
						else pos1-=step0;
					}
				}
			}
			else
			{
				step1=abs(job1[ok1]-pos1)+1;
				ans+=step1;
				pos1=job1[ok1++];
				if(ok0<kjob0)
				{
					if(abs(job0[ok0]-pos0)<=step1)//说明1号在0号搞定的时候已经走到指定位置
					{
						pos0=job0[ok0];
					}else//说明1号在0号搞定的时候走不到指定位置
					{
						if(pos0<job0[ok0])pos0+=step1;
						else pos0-=step1;
					}
				}
			}
		}
		printf("Case #%d: %d\n",++tt,ans);
	}
	return 0;
}