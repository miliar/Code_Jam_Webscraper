#include<stdio.h>
#include<string.h>
int room[10][10],n,f[10],u[10],v[10],g[10][10],set[10],k,e,cr[10],res,o[10];
bool vis[10];
void lzs(int c,int r)
{
	int i;
	if(c==n+1)
	{
		int j,h;
		for(i=0;i<e;i++)
		{
			h=0;
			memset(vis,false,sizeof(vis));
			for(j=0;j<f[i];j++)
				if(!vis[o[room[i][j]]])
				{
					h++;
					vis[o[room[i][j]]]=true;
				}
			if(h<r)break;
		}
		if(i==e&&res<r)
		{
			for(i=1;i<=n;i++)cr[i]=o[i];
			res=r;
		}
		return ;	
	}
	for(i=1;i<=r+1;i++)
	{
		o[c]=i;
		if(i==r+1)lzs(c+1,r+1);
		else lzs(c+1,r);
	}
}
int main()
{
	int t,flag,ca=1,i,j,h,l,m;
	scanf("%d",&t);
	while(t--)
	{
		printf("Case #%d: ",ca++);
		scanf("%d%d",&n,&m);
		for(i=0;i<m;i++)
			scanf("%d",u+i);
		for(i=0;i<m;i++)
			scanf("%d",v+i);
		memset(g,0,sizeof(g));
		for(i=0;i<m;i++)
			g[u[i]][v[i]]=g[v[i]][u[i]]=1;
		for(i=1;i<n;i++)g[i][i+1]=g[i+1][i]=1;
		g[n][1]=g[1][n]=1;
		/*for(i=1;i<=n;i++)
		{
			for(j=1;j<=n;j++)
				printf("%d ",g[i][j]);
			puts("");
		}*/
		l=(1<<n)-1;
		e=0;
		for(i=0;i<l;i++)
		{
			k=0;
			for(j=0;j<n;j++)
				if(i&(1<<j))
			{
				set[k++]=j+1;
			}
			if(k>=3)
			{
				flag=0;
				for(j=0;j<k-1;j++)
					if(!g[set[j]][set[j+1]])flag=1;
				if(!g[set[k-1]][set[0]])flag=1;
				//printf("f1:%d \n",flag);
				if(flag)continue;
				for(j=0;j<k;j++)
					for(h=0;h<k;h++)
						if(h-j!=1&&j-h!=1&&(j!=0||h!=k-1)&&(j!=k-1||h!=0)&&g[set[j]][set[h]]){flag=1;j=h=k;}
				//printf("f2:%d \n",flag);
				if(flag)continue;
				f[e]=k;
				for(j=0;j<k;j++)room[e][j]=set[j];
				e++;
			}
		}/*
		printf("e:%d \n",e);
		for(i=0;i<e;i++)
		{
			printf("room %d : ",i);
			for(j=0;j<f[i];j++)
				printf("%d ",room[i][j]);
			puts("");
		}*/
		res=0;
		lzs(1,0);
		printf("%d\n",res);
		for(i=1;i<n;i++)printf("%d ",cr[i]);
		printf("%d\n",cr[i]);
	}
}
