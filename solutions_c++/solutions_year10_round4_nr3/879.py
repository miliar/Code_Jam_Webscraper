

#include "stdafx.h"
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <math.h>
#include <stdlib.h>
#include <string.h>
#include <string>
#include <map>
#include <vector>
#include <queue>
using namespace std;


int ditu[200][200];

int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("1.out","w",stdout);
	int t,n,k;
	long long zb;
	scanf("%d",&t);
	for(int x=1;x<=t;++x)
	{
		memset(ditu,0,sizeof(ditu));
		scanf("%d",&n);
		int x1,x2,y1,y2;
		int cnt =0;
		while(n--)
		{
			scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
			if(x1>x2) swap(x1,x2);
			if(y1>y2) swap(y1,y2);
			for(int i=x1;i<=x2;++i)
				for(int j=y1;j<=y2;++j)
				{
					if(ditu[i][j] == 0)
					{
						ditu[i][j] = 1;
						cnt++;
					}
				}
		}
		int ct1=1;
		while(cnt!=0)
		{
			for(int i=100;i>=1;--i)
				for(int j=100;j>=1;--j)
				{
					if(ditu[i][j] != 0)
					{
						if(ditu[i-1][j+1] != 0)
						{
							if(ditu[i][j+1] == 0) cnt++;
							ditu[i][j+1] = ct1;
						}

						if(ditu[i-1][j] == 0 && ditu[i][j-1] == 0) 
						{
							cnt -- ;
							ditu[i][j] = 0;
						}
					}
				}
			ct1++;
		}
		printf("Case #%d: %d\n",x,ct1-1);
	}
	return 0;
}

