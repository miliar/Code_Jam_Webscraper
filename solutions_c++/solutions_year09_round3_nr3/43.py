#include <cstdio>
#include <iostream>
#include <string>
#include <cstring>
#include <vector>
#include <set>
#include <iostream>
#include <algorithm>
#include <cmath>

using namespace std;

const int nmax=102;
int num[nmax];
int best[nmax][nmax];

int answer(int l,int r)
{
	if (best[l][r]>-1) return best[l][r];
	int ret=1000000000,i,j;
	for(i=l+1;i<r;i++)
	{
		j=answer(l,i)+answer(i,r)+num[r]-num[l]-2;
		if (j<ret) ret=j;
	}
	return best[l][r]=ret;
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int t,T;
	scanf("%d",&T);
	for(t=1;t<=T;t++)
	{
		int n,m,i,j,k;
		scanf("%d%d",&n,&m);
		for(i=0;i<m;i++) scanf("%d",&num[i]);
		num[m++]=0;
		num[m++]=n+1;
		sort(num,num+m);
		for(i=0;i<m;i++)
		{
			for(j=0;j<m;j++) best[i][j]=-1;
			best[i][i]=0;
			best[i][i+1]=0;
		}
		printf("Case #%d: %d\n",t,answer(0,m-1));
	}

	return 0;
}