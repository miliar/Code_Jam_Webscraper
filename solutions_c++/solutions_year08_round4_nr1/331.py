#include<stdio.h>
#include<memory>
int v[10000+16],r[10000+16];
int z[10000+16][2];
int n;
void get(int x,int b,int a)
{
	int now;
	if(b)
	{
		if(z[x+x][1]!=-1&&z[x+x+1][1]!=-1)
			if(z[x][1]==-1||a+z[x+x][1]+z[x+x+1][1]<z[x][1])
				z[x][1]=a+z[x+x][1]+z[x+x+1][1];
		if(z[x+x][0]!=-1)
		{
			if(z[x+x+1][0]==-1&&z[x+x+1][1]==-1)
				now=-1;
			else if(z[x+x+1][0]==-1)
				now=z[x+x+1][1];
			else if(z[x+x+1][1]==-1)
				now=z[x+x+1][0];
			else if(z[x+x+1][0]<z[x+x+1][1])
				now=z[x+x+1][0];
			else
				now=z[x+x+1][1];
			if(now!=-1)
				if(z[x][0]==-1||a+now+z[x+x][0]<z[x][0])
					z[x][0]=a+now+z[x+x][0];
		}
		if(z[x+x+1][0]!=-1)
		{
			if(z[x+x][0]==-1&&z[x+x][1]==-1)
				now=-1;
			else if(z[x+x][0]==-1)
				now=z[x+x][1];
			else if(z[x+x][1]==-1)
				now=z[x+x][0];
			else if(z[x+x][0]<z[x+x][1])
				now=z[x+x][0];
			else
				now=z[x+x][1];
			if(now!=-1)
				if(z[x][0]==-1||a+now+z[x+x+1][0]<z[x][0])
					z[x][0]=a+now+z[x+x+1][0];
		}
	}
	else
	{
		if(z[x+x][0]!=-1&&z[x+x+1][0]!=-1)
			if(z[x][0]==-1||a+z[x+x][0]+z[x+x+1][0]<z[x][0])
				z[x][0]=a+z[x+x][0]+z[x+x+1][0];
		if(z[x+x][1]!=-1)
		{
			if(z[x+x+1][0]==-1&&z[x+x+1][1]==-1)
				now=-1;
			else if(z[x+x+1][0]==-1)
				now=z[x+x+1][1];
			else if(z[x+x+1][1]==-1)
				now=z[x+x+1][0];
			else if(z[x+x+1][0]<z[x+x+1][1])
				now=z[x+x+1][0];
			else
				now=z[x+x+1][1];
			if(now!=-1)
				if(z[x][1]==-1||a+now+z[x+x][1]<z[x][1])
					z[x][1]=a+now+z[x+x][1];
		}
		if(z[x+x+1][1]!=-1)
		{
			if(z[x+x][0]==-1&&z[x+x][1]==-1)
				now=-1;
			else if(z[x+x][0]==-1)
				now=z[x+x][1];
			else if(z[x+x][1]==-1)
				now=z[x+x][0];
			else if(z[x+x][0]<z[x+x][1])
				now=z[x+x][0];
			else
				now=z[x+x][1];
			if(now!=-1)
				if(z[x][1]==-1||a+now+z[x+x+1][1]<z[x][1])
					z[x][1]=a+now+z[x+x+1][1];
		}
	}
}
void tt(int x)
{
	if(x>(n-1)/2)
	{
		z[x][v[x]]=0;
		return;
	}
	tt(x+x);
	tt(x+x+1);
	if(v[x])
	{
		get(x,1,0);
		if(r[x])
			get(x,0,1);
	}
	else
	{
		get(x,0,0);
		if(r[x])
			get(x,1,1);
	}
}


int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int c,o,b,i;
	scanf("%d",&c);
	for(o=1;o<=c;o++)
	{
		scanf("%d%d",&n,&b);
		for(i=1;i<=n;i++)
		{
			scanf("%d",v+i);
			if(i<=(n-1)/2)
				scanf("%d",r+i);
		}
		memset(z,0XFF,sizeof(z));
		tt(1);
		if(z[1][b]==-1)
			printf("Case #%d: IMPOSSIBLE\n",o);
		else
			printf("Case #%d: %d\n",o,z[1][b]);
	}
	return 0;
}