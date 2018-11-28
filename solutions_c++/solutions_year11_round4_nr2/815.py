#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <cmath>
using namespace std;


int a[11][11];
int R,C,D;

//int sum[11][11][11][11];

bool test(int x,int y,int size)
{
	double sumx = 0;
	double sumy = 0;

	for(int i=x;i<x+size;i++)
	{
		for(int j=y;j<y+size;j++)
		{
			if(i==x && j==y) continue;
			if(i==x && j==y+size-1) continue;
			if(i==x+size-1 && j==y) continue;
			if(i==x+size-1 && j==y+size-1) continue;
			sumx += (i-x-(size-1)/2.0) * a[i][j];
			sumy += (j-y-(size-1)/2.0) * a[i][j];
		}
	}
	if (sumx==0 && sumy==0)
		return true;
	else
		return false;
}
int main()
{
	int T;
	scanf("%d",&T);
	for(int Ti = 0;Ti <T ;Ti ++)
	{
		scanf("%d%d%d",&R,&C,&D);
		for(int i=0;i<R;i++)
		{
			char str[100];
			scanf("%s",str);
			for(int j=0;j<C;j++)
			{
				a[i][j] = str[j]-'0';
			}
		}
		int result = 0;
		for(int size=max(R,C);size>=3; size--)
		{
			for(int i=0;i<=R-size;i++)
			{
				for(int j=0;j<=C-size;j++)
				{
					if(test(i,j,size))
					{
						result = size;
						goto scat;
					}
				}
			}
			
		}
scat:	
		;

		printf("Case #%d: ",Ti+1);
		if(result) 
			printf("%d\n",result);
		else
			printf("IMPOSSIBLE\n");

	}
	return 0;
}