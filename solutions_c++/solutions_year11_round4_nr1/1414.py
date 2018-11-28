#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<fstream>

using namespace std;

#define MAXN 1000

struct Node
{
	double len,w;	
}walkWay[MAXN];

int m;
double n,S,R,T,res,cnt;

bool cmp(Node a,Node b)
{
	return a.w<b.w;
}

void solve()
{
	int i,j;
	double t;
	res=0.0;
	n-=cnt;
	if(n/R<=T)
	{
		res+=n/R;
		T-=n/R;
	}
	else
	{
		res+=T+(n-T*R)/S;
		T=0;
	}
	sort(walkWay,walkWay+m,cmp);
	for(i=0;i<m;i++)
	{
		t=walkWay[i].len/(walkWay[i].w+R);
		if(T>=t)
		{
			res+=t;			
			T-=t;
		}
		else
		{
			res+=T+(walkWay[i].len-T*(walkWay[i].w+R))/(walkWay[i].w+S);
			T=0;
		}	
	}
}

int main()
{
	int ct,text;
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&text);
	for(ct=1;ct<=text;ct++)
	{
		int i;
		cnt=0.0;
		scanf("%lf%lf%lf%lf%d",&n,&S,&R,&T,&m);
		for(i=0;i<m;i++)
		{
			double s,t;
			scanf("%lf%lf%lf",&s,&t,&walkWay[i].w);
			walkWay[i].len=t-s;
			cnt+=walkWay[i].len;
		}
		solve();
		printf("Case #%d: %.6lf\n",ct,res);
	}
	return 0;
}
