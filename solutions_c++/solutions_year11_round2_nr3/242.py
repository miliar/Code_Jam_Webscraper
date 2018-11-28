#include <stdio.h>
#include <algorithm>

struct D{int s,e;
	bool friend operator < (const D &p,const D &q)
	{
		if(p.s!=q.s) return p.s<q.s;
		if((p.s<p.e)!=(q.s<q.e)) return p.s>p.e;
		return p.e>q.e;
	}
}a[10010];
int cash[2002][2002],color[2002],q[100001],list[2002],rest[2002];
bool visit[10010],used[2002];

int main()
{
	int t,T=0,i,j,k,n,m,ans,now,front,rear;

	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	for(scanf("%d",&t);t--;)
	{
		scanf("%d%d",&n,&m);
		for(i=1;i<=m;++i) scanf("%d",&a[i].s);
		for(i=1;i<=m;++i) scanf("%d",&a[i].e);
		for(i=1;i<=n;++i)
		{
			++m; a[m].s=i;
			a[m].e=i+1;
		} a[m].e=1;

		for(k=m,i=1;i<=k;++i)
		{
			++m; a[m].s=a[i].e; a[m].e=a[i].s;
		}
		a[m+1].s=0;

		std::sort(a+1,a+m+1);

		ans=n;
		for(i=1;i<=m;++i) cash[a[i].s][a[i].e]=i;
		for(i=1;i<=m;++i) visit[i]=false;
		for(i=1;i<=m;++i) if(!visit[i])
		{

			now=i;
			k=0;
			while(1)
			{
				++k;
				visit[now]=true;
				j=cash[a[now].e][a[now].s]+1;
				if(a[j].s==a[now].e) now=j; else {k=10000;break;}
				if(now==i) break;
			}
			if(k<ans) ans=k;
		}
		// ###########
		for(i=1;i<=m;++i) visit[i]=false;
		// ###########

		for(i=1;i<=n;++i) color[i]=0;

		front=0;rear=1; q[1]=m;
		while(front!=rear)
		{
			++front;
			i=q[front];
			if(visit[i]) continue;

			now=i;
			k=0;
			
			while(1)
			{
				list[++k]=a[now].s;
				visit[now]=true;
				if(!visit[cash[a[now].e][a[now].s]]) q[++rear]=cash[a[now].e][a[now].s];
				j=cash[a[now].e][a[now].s]+1;
				if(a[j].s==a[now].e) now=j; else {k=10000;break;}
				if(now==i) break;
			}
			if(k<10000)
			{
				for(i=1;i<=ans;++i) used[i]=false;
				for(i=1;i<=k;++i) if(color[list[i]]) used[color[list[i]]]=true;
				j=0;
				for(i=1;i<=ans;++i) if(!used[i]) rest[++j]=i;

				list[0]=list[k]; list[k+1]=list[1];
				for(i=1;i<=k;++i) if(!color[list[i]])
				{
					if(j) color[list[i]]=rest[j], --j;
					/*else
					{
						if(color[list[i-1]]!=1 && color[list[i+1]]!=1) color[list[i]]=1;
						else if(color[list[i-1]]!=2 && color[list[i+1]]!=2) color[list[i]]=2;
						else color[list[i]]=3;
					}*/
				}
			}
		}


		printf("Case #%d: %d\n",++T,ans);
		for(i=1;i<=n;++i)
		{
			if(color[i]>ans) color[i]=1;
			if(!color[i]) color[i]=1;
			printf("%d ",color[i]);
		}
		printf("\n");
	}
	return 0;
}
