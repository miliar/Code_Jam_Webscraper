#include <cstdio>
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <map>
#include <sstream>
#include <cstring>
#include <cmath>

using namespace std;

const int nmax=(1<<10);
int see[nmax];
int q[nmax];
int pr[nmax];
int ans[nmax][11];

void dfsDP(int v,int end,int end2)
{
	int i,j;
	for(i=0;i<=10;i++) ans[v][i]=1000000000;
	if (v>=end)
	{
		int s=max(see[v+v+1-end2],see[v+v+2-end2]);
		ans[v][s]=0;
		if (s>0) ans[v][s-1]=pr[v];
	} else
	{
		dfsDP(v+v+1,end,end2);
		dfsDP(v+v+2,end,end2);
		for(i=0;i<=10;i++)
			for(j=0;j<=10;j++) ans[v][max(i,j)]=min(ans[v][max(i,j)],ans[v+v+1][i]+ans[v+v+2][j]);
		for(i=1;i<=10;i++) ans[v][i-1]=min(ans[v][i-1],ans[v][i]+pr[v]);
	}
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int T,t,i,j,k,n;
	cin>>T;
	for(t=1;t<=T;t++)
	{
		cin>>n;
		int x=1<<n;

		for(i=0;i<x;i++) 
		{
			cin>>see[i];
			see[i]=n-see[i];
		}

		for(i=n-1;i>=0;i--)
		{
			int off=(1<<i)-1;
			for(j=0;j<(1<<i);j++) 
			{
				cin>>pr[off+j];
			}
		}

		dfsDP(0,(1<<(n-1))-1,(1<<n)-1);
		printf("Case #%d: %d\n",t,ans[0][0]);
	}

	return 0;
}