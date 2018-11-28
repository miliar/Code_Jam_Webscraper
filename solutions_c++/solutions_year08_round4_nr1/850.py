#include <iostream>
using namespace std;

int M,V,T;

struct node
{
	int type;
	int value;
	int change;
	int tt;
	int v[2];
};

node nodes[101000];

void input()
{
	int G,C;
	scanf("%d%d",&M,&V);
	++T;
	for(int i=1;i<=(M-1)/2;++i)
	{
		scanf("%d%d",&G,&C);
		nodes[i].type=1;
		nodes[i].change=C;
		nodes[i].value=G;
	}
	for(int i=((M-1)/2)+1;i<=M;++i)
	{
		scanf("%d",&C);
		nodes[i].type=0;
		nodes[i].value=C;
	}
}

void subwork(int n)
{
	int a,b,c;
	if(nodes[n].tt==T) return;
	if(nodes[n].type==0)
	{
		c=nodes[n].value;
		nodes[n].v[c]=0;
		nodes[n].v[!c]=-1;
		nodes[n].tt=T;
		return;
	}
	subwork(2*n);
	subwork(2*n+1);
	if(nodes[n].value)
	{
		if(nodes[2*n].v[1]<0||nodes[2*n+1].v[1]<0)
			nodes[n].v[1]=-1;
		else
		{
			nodes[n].v[1]=nodes[2*n].v[1]+nodes[2*n+1].v[1];
		}
		nodes[n].v[0]=-1;
		for(int i=0;i<2;++i)
			for(int j=0;j<2;++j)
			{
				if(j==i&&j==1) continue;
				if(nodes[2*n].v[i]<0||nodes[2*n+1].v[j]<0)
					c=-1;
				else c=nodes[2*n].v[i]+nodes[2*n+1].v[j];
				if(c<0) continue;
				if(nodes[n].v[0]<0||nodes[n].v[0]>c)
					nodes[n].v[0]=c;
			}
	}
	else
	{
		if(nodes[2*n].v[0]<0||nodes[2*n+1].v[0]<0)
			nodes[n].v[0]=-1;
		else
		{
			nodes[n].v[0]=nodes[2*n].v[0]+nodes[2*n+1].v[0];
		}
		nodes[n].v[1]=-1;
		for(int i=0;i<2;++i)
			for(int j=0;j<2;++j)
			{
				if(j==i&&j==0) continue;
				if(nodes[2*n].v[i]<0||nodes[2*n+1].v[j]<0)
					c=-1;
				else c=nodes[2*n].v[i]+nodes[2*n+1].v[j];
				if(c<0) continue;
				if(nodes[n].v[1]<0||nodes[n].v[1]>c)
					nodes[n].v[1]=c;
			}
	}
	
	
	if(nodes[n].change==1)
	{
		a=nodes[n].v[0];
		b=nodes[n].v[1];
		if(!nodes[n].value)
		{
			if(nodes[2*n].v[1]<0||nodes[2*n+1].v[1]<0)
				nodes[n].v[1]=-1;
			else
			{
				nodes[n].v[1]=nodes[2*n].v[1]+nodes[2*n+1].v[1]+1;
			}
			nodes[n].v[0]=-1;
			for(int i=0;i<2;++i)
				for(int j=0;j<2;++j)
				{
					if(j==i&&j==1) continue;
					if(nodes[2*n].v[i]<0||nodes[2*n+1].v[j]<0)
						c=-1;
					else c=nodes[2*n].v[i]+nodes[2*n+1].v[j]+1;
					if(c<0) continue;
					if(nodes[n].v[0]<0||nodes[n].v[0]>c)
						nodes[n].v[0]=c;
				}
		}
		else
		{
			if(nodes[2*n].v[0]<0||nodes[2*n+1].v[0]<0)
				nodes[n].v[0]=-1;
			else
			{
				nodes[n].v[0]=nodes[2*n].v[0]+nodes[2*n+1].v[0]+1;
			}
			nodes[n].v[1]=-1;
			for(int i=0;i<2;++i)
				for(int j=0;j<2;++j)
				{
					if(j==i&&j==0) continue;
					if(nodes[2*n].v[i]<0||nodes[2*n+1].v[j]<0)
						c=-1;
					else c=nodes[2*n].v[i]+nodes[2*n+1].v[j]+1;
					if(c<0) continue;
					if(nodes[n].v[1]<0||nodes[n].v[1]>c)
						nodes[n].v[1]=c;
				}
		}
		if((a>=0&&a<nodes[n].v[0])||nodes[n].v[0]<0) nodes[n].v[0]=a;
		if((b>=0&&b<nodes[n].v[1])||nodes[n].v[1]<0) nodes[n].v[1]=b;
	}
	nodes[n].tt=T;
}

void work()
{
	subwork(1);
	if(nodes[1].v[V]<0)
		printf("IMPOSSIBLE\n");
	else printf("%d\n",nodes[1].v[V]);
}

int main()
{
	int n;
	scanf("%d",&n);
	T=0;
	for(int i=0;i<n;++i)
	{
		input();
		printf("Case #%d: ",i+1);
		work();
	}
	return 0;
}
