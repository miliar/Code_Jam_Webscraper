#include<iostream>
#include<algorithm>
struct W
{
	int pl,need;
}d[2000];
int point[1026][12],piaojia[2000];
bool maile[2000];
bool cmp(const W &a,const W &b)
{
	return a.need>b.need;
}
int main()
{
	int T,cs,i,j,k,n,r,pt,ct,last,ans;
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-small-attempt0.out","w",stdout);
//	freopen("B-Large.in","r",stdin);
//	freopen("B-Large.out","w",stdout);
	scanf("%d",&T);
	for(cs=1;cs<=T;cs++)
	{
		memset(maile,0,sizeof(maile));
		scanf("%d",&r);
		last=r-1;
		n=1<<r;
		for(i=0;i<n;i++)
		{
			scanf("%d",&d[i].need);
			if(d[i].need>r)d[i].need=r;
			d[i].need=r-d[i].need;
			d[i].pl=i;
		}
		for(i=0;i<n-1;i++)
			scanf("%d",&piaojia[i]);
		pt=2;
		for(ct=i=0;i<r;i++)
		{
			for(j=0;j<n;j+=pt)
			{
				for(k=0;k<pt;k++)
					point[k+j][i]=ct;
				ct++;
			}
			pt*=2;
		}
		std::sort(d,d+n,cmp);
		for(ans=i=0;i<n;i++)
		{
			for(j=last;d[i].need&&j>=0;j--)
				if(maile[point[d[i].pl][j]])d[i].need--;
				else
				{
					d[i].need--;
					ans+=piaojia[point[d[i].pl][j]];
					maile[point[d[i].pl][j]]=true;
//					printf("aa %d\n",piaojia[point[d[i].pl][j]]);
				}
		}
//		for(i=0;i<n;i++)
		printf("Case #%d: %d\n",cs,ans);
	}
	return 0;
}
