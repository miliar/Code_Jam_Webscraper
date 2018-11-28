#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cassert>
#include <algorithm>
#include <set>
#include <map>
#include <string>
#pragma warning (disable:4996)


//struct D{int s,e;
//	bool friend operator < (const D &p,const D &q)
//	{
//		if(p.s!=q.s) return p.s<q.s;
//		return p.e<q.e;
//	}
//};


int ans,num[102][102],k,neigh[10002][2],v[100002];
char a[102][102];

void process(int level)
{
	if(level>k)
	{
		++ans;
	}
	else
	{
		if(!v[neigh[level][0]])
		{
			v[neigh[level][0]]=1;
			process(level+1);
			v[neigh[level][0]]=0;
		}
		if(!v[neigh[level][1]])
		{
			v[neigh[level][1]]=1;
			process(level+1);
			v[neigh[level][1]]=0;
		}
	}
}

int main()
{
	int t,T=0;
	int i,j,n,m;

	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	for(scanf("%d",&t);t--;)
	{
		scanf("%d%d",&n,&m);
		k=0;
		for(i=1;i<=n;++i)
		{
			scanf("%s",&a[i][1]);
			for(j=1;j<=m;++j) num[i][j]=++k;
		}
		for(j=1;j<=m;++j) num[0][j]=num[n][j], num[n+1][j]=num[1][j];
		for(j=1;j<=n;++j) num[j][0]=num[j][m], num[j][m+1]=num[j][1];
		num[0][0]=num[n][m];
		num[n+1][m+1]=num[1][1];
		num[0][m+1]=num[n][1];
		num[n+1][0]=num[1][m];
		
		for(i=1;i<=n;++i)
			for(j=1;j<=m;++j)
				if(a[i][j]=='-')
					neigh[num[i][j]][0]=num[i][j-1],
					neigh[num[i][j]][1]=num[i][j+1];
				else if(a[i][j]=='|')
					neigh[num[i][j]][0]=num[i-1][j],
					neigh[num[i][j]][1]=num[i+1][j];
				else if(a[i][j]=='/')
					neigh[num[i][j]][0]=num[i-1][j+1],
					neigh[num[i][j]][1]=num[i+1][j-1];
				else
					neigh[num[i][j]][0]=num[i-1][j-1],
					neigh[num[i][j]][1]=num[i+1][j+1];
		ans=0;
		process(1);

		printf("Case #%d: %d\n",++T,ans);
	}
	return 0;
}
