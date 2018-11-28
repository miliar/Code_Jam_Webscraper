#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <cstring>
#include <string>
#include <vector>
#include <set>
#include <map>
using namespace std;

char a[120][120];
int len[120];

int main()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int t,tt;
	int i,j,u,k;
	int hor,ver;
	scanf("%d",&t);
	for (tt=0; tt<t; ++tt)
	{
		scanf("%d",&k);
		gets(a[0]);
		memset(a,' ',sizeof(a));
		for (i=0; i<2*k-1; ++i)
		{
			gets(a[i]);
			len[i]=strlen(a[i]);
		}
		hor=0;
		for (i=0; i<2*k-1; ++i)
		{
			for (u=0; u<2*k-1; ++u)
			{
				for (j=0; j<len[u]; ++j)
					if (a[u][j]!=' ' && 2*i-u>=0 && 2*i-u<2*k-1 && len[2*i-u]>=j && 
						a[2*i-u][j]!=' ' && a[u][j]!=a[2*i-u][j])
						break;
				if (j<len[u]) break;
			}
			if (u==2*k-1 && abs(i-k+1)<abs(hor-k+1))
			{
				hor=i;
			}
		}
		ver=0;
		for (i=0; i<2*k-1; ++i)
		{
			for (u=0; u<2*k-1; ++u)
			{
				for (j=0; j<len[u]; ++j)
					if (a[j][u]!=' ' && 2*i-u>=0 && 2*i-u<2*k-1 && len[2*i-u]>j && 
						a[j][2*i-u]!=' ' && a[j][u]!=a[j][2*i-u])
						break;
				if (j<len[u]) break;
			}
			if (u==2*k-1 && abs(i-k+1)<abs(ver-k+1))
			{
				ver=i;
			}
		}
		int nsize=k+abs(ver-k+1)+abs(hor-k+1);
		printf("Case #%d: %d\n",tt+1,nsize*nsize-k*k);
	}
	return 0;
}