#include <iostream>
#include <string>
#include <algorithm>
#include <cstring>
#include <stdlib.h>
#include <cmath>
using namespace std;

long long tablex[15];
double table[15][15];
double tablecut[15][15];
bool check(int n)
{
	int flag=0;
	double len=double(n-1)/2;
	double w=0.0;
	for(int i=0;i<n;i++)
	{
		for(int j=0;j<n;j++)
		{
			if((i==0)&&(j==0))
				continue;
			if((i==0)&&(j==(n-1)))
				continue;
			if((i==(n-1))&&(j==0))
				continue;
			if((i==(n-1))&&(j==(n-1)))
				continue;
			w=w+tablecut[i][j]*len;
		}
		len=len-1.0;
	}
	if((w > 0.0000001)||(w < -0.0000001))
		return false;
	w=0.0;
	len=double(n-1)/2;
	for(int j=0;j<n;j++)
	{
		for(int i=0;i<n;i++)
		{
			if((i==0)&&(j==0))
				continue;
			if((i==0)&&(j==(n-1)))
				continue;
			if((i==(n-1))&&(j==0))
				continue;
			if((i==(n-1))&&(j==(n-1)))
				continue;
			w=w+tablecut[i][j]*len;
		}
		len=len-1.0;
	}
	if((w > 0.0000001)||(w < -0.0000001))
		return false;
	return true;
}

int main()
{
	freopen("e:\\B-small.in", "r", stdin);	freopen("e:\\B-small.out", "w", stdout);
	int T;
	scanf("%d",&T);
	for(int i=0;i<T;i++)
	{
		int R,C;
		double D;
		scanf("%d%d%lf",&R,&C,&D);
		for(int j=0;j<R;j++)
			scanf("%lld",&tablex[j]);
		for(int k=0;k<R;k++)
		{
			for(int j=0;j<C;j++)
			{
				table[k][j]=double(tablex[k]%10);
				tablex[k]/=10;
			}
		}
		int big=R;
		if(big < C)
			big=C;
		int res=0;
		int flag=0;
		for(int j=big;j>2;j--)
		{
			for(int k=0;k<=(R-j);k++)
			{
				for(int l=0;l<=(C-j);l++)
				{
					for(int m=0;m<j;m++)
					{
						for(int n=0;n<j;n++)
						{
							tablecut[m][n]=table[k+m][l+n];
						}
					}
					if(check(j))
					{
						res=j;
						flag=1;
						break;
					}
				}
				if(flag == 1)
					break;
			}
			if(flag == 1)
				break;
		}
		if(res != 0)
			printf("Case #%d: %d\n",i+1,res);
		else
			printf("Case #%d: IMPOSSIBLE\n",i+1);
		
	}
	return 0;
}