#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

int v,m;
struct nod
{
	int g,c;
	int m1,m0,c1,c0;
}node[10001];

void solve(int ind)
{
	for(int i=(m-1)/2;i>=1;i--)
	{
		if(node[i].g==1)
		{
			if(node[i*2].c1==1&&node[i*2+1].c1==1) 
			{
				if(node[i].c1==1) 
					node[i].m1=min(node[i].m1,node[i*2].m1+node[i*2+1].m1);
				else {node[i].m1=node[i*2].m1+node[i*2+1].m1;node[i].c1=1;}
			}
		}
		if(node[i].g==0)
		{	
			if(node[i*2].c1==1&&node[i*2+1].c0==1) 
			{
				if(node[i].c1==1) 
					node[i].m1=min(node[i].m1,node[i*2].m1+node[i*2+1].m0);
				else {node[i].m1=node[i*2].m1+node[i*2+1].m0;node[i].c1=1;}
			}
			if(node[i*2+1].c1==1&&node[i*2].c0==1) 
			{
				if(node[i].c1==1) 
					node[i].m1=min(node[i].m1,node[i*2+1].m1+node[i*2].m0);
				else {node[i].m1=node[i*2+1].m1+node[i*2].m0;node[i].c1=1;}
			}
			if(node[i*2+1].c1&&node[i*2].c1)
			{
				if(node[i].c1)
					node[i].m1=min(node[i].m1,node[i*2].m1+node[i*2+1].m1);
				else {node[i].m1=node[i*2].m1+node[i*2+1].m1;node[i].c1=1;}
			}
		}
		if(node[i].g==0&&node[i].c==1)
		{
			if(node[i*2].c1==1&&node[i*2+1].c1==1) 
			{
				if(node[i].c1==1) 
					node[i].m1=min(node[i].m1,node[i*2].m1+node[i*2+1].m1+1);
				else {node[i].m1=node[i*2].m1+node[i*2+1].m1+1;node[i].c1=1;}
			}
		}
		if(node[i].g==1&&node[i].c==1)
		{	
			if(node[i*2].c1==1&&node[i*2+1].c0==1) 
			{
				if(node[i].c1==1) 
					node[i].m1=min(node[i].m1,node[i*2].m1+node[i*2+1].m0+1);
				else {node[i].m1=node[i*2].m1+node[i*2+1].m0+1;node[i].c1=1;}
			}
			if(node[i*2+1].c1==1&&node[i*2].c0==1) 
			{
				if(node[i].c1==1) 
					node[i].m1=min(node[i].m1,node[i*2+1].m1+node[i*2].m0+1);
				else {node[i].m1=node[i*2+1].m1+node[i*2].m0+1;node[i].c1=1;}
			}
			if(node[i*2+1].c1&&node[i*2].c1)
			{
				if(node[i].c1)
					node[i].m1=min(node[i].m1,node[i*2].m1+node[i*2+1].m1+1);
				else {node[i].m1=node[i*2].m1+node[i*2+1].m1+1;node[i].c1=1;}
			}
		}
		if(node[i].g==0)
		{
			if(node[i*2].c0==1&&node[i*2+1].c0==1)
			{
				if(node[i].c0)
					node[i].m0=min(node[i].m0,node[i*2].m0+node[i*2+1].m0);
				else {node[i].c0=1;node[i].m0=node[i*2].m0+node[i*2+1].m0;}
			}
		}
		if(node[i].g==1)
		{
			if(node[i*2].c0==1&&node[i*2+1].c0==1)
			{
				if(node[i].c0)
					node[i].m0=min(node[i].m0,node[i*2].m0+node[i*2+1].m0);
				else {node[i].c0=1;node[i].m0=node[i*2].m0+node[i*2+1].m0;}
			}
			if(node[i*2].c1==1&&node[i*2+1].c0==1)
			{
				if(node[i].c0)
					node[i].m0=min(node[i].m0,node[i*2].m1+node[i*2+1].m0);
				else {node[i].c0=1;node[i].m0=node[i*2].m1+node[i*2+1].m0;}
			}
			if(node[i*2].c0==1&&node[i*2+1].c1==1)
			{
				if(node[i].c0)
					node[i].m0=min(node[i].m0,node[i*2].m0+node[i*2+1].m1);
				else {node[i].c0=1;node[i].m0=node[i*2].m0+node[i*2+1].m1;}
			}
		}
		if(node[i].g==0&&node[i].c==1)
		{
			if(node[i*2].c0==1&&node[i*2+1].c0==1)
			{
				if(node[i].c0)
					node[i].m0=min(node[i].m0,node[i*2].m0+node[i*2+1].m0+1);
				else {node[i].c0=1;node[i].m0=node[i*2].m0+node[i*2+1].m0+1;}
			}
			if(node[i*2].c1==1&&node[i*2+1].c0==1)
			{
				if(node[i].c0)
					node[i].m0=min(node[i].m0,node[i*2].m1+node[i*2+1].m0+1);
				else {node[i].c0=1;node[i].m0=node[i*2].m1+node[i*2+1].m0+1;}
			}
			if(node[i*2].c0==1&&node[i*2+1].c1==1)
			{
				if(node[i].c0)
					node[i].m0=min(node[i].m0,node[i*2].m0+node[i*2+1].m1+1);
				else {node[i].c0=1;node[i].m0=node[i*2].m0+node[i*2+1].m1+1;}
			}
		}
		if(node[i].g==1&&node[i].c==1)
		{
			if(node[i*2].c0==1&&node[i*2+1].c0==1)
			{
				if(node[i].c0)
					node[i].m0=min(node[i].m0,node[i*2].m0+node[i*2+1].m0+1);
				else {node[i].c0=1;node[i].m0=node[i*2].m0+node[i*2+1].m0+1;}
			}
		}
	}
//	for(int i=1;i<=m;i++)
//		printf("%d c0=%d c1=%d m0=%d m1=%d\n",i,node[i].c0,node[i].c1,node[i].m0,node[i].m1);
	if((v==1&&node[1].c1==0)||(v==0&&node[1].c0==0)) {printf("Case #%d: IMPOSSIBLE\n",ind);return;}
	if(v==1) {printf("Case #%d: %d\n",ind,node[1].m1);return;}
	if(v==0) {printf("Case #%d: %d\n",ind,node[1].m0);return;}
}

void read(int ind)
{
	for(int i=0;i<10001;i++)
	{
		node[i].g=0;
		node[i].c=0;
		node[i].m0=node[i].m1=node[i].c0=node[i].c1=0;
	}
	scanf("%d %d",&m,&v);
	int x;
	for(int i=1;i<=(m-1)/2;i++)
	{
		scanf("%d %d",&node[i].g,&node[i].c);
	}
	for(int i=(m+1)/2;i<=m;i++)
	{
		scanf("%d",&x);
		if(x==0) {node[i].c0=1;}
		if(x==1) {node[i].c1=1;}
	}
	solve(ind);
}

int main()
{
	int nt;
	scanf("%d",&nt);
	for(int i=1;i<=nt;i++) 
		read(i);
	return 0;
}
