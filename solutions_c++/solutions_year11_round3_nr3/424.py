#include <iostream>
#include <string>
#include <algorithm>
#include <cstring>
#include <stdlib.h>
#include <cmath>
using namespace std;


int fre[200];
bool check(int one,int two)
{
	int c=1;
	if(one < two)
		c=(two%one);
	else
		c=(one%two);
	if(c == 0)
		return true;
	else
		return false;
}

int main()
{
	freopen("e:\\C-large.in", "r", stdin);	freopen("e:\\C-large.out", "w", stdout);
	int T;
	scanf("%d",&T);
	for(int i=0;i<T;i++)
	{
		int n,l,h;
		int res=-1;
		scanf("%d%d%d",&n,&l,&h);
		for(int j=0;j<n;j++)
		{
			scanf("%d",&fre[j]);
		}
		for(int j=l;j<=h;j++)
		{
			int flag=0;
			for(int k=0;k<n;k++)
			{
				if(!check(j,fre[k]))
				{
					flag=1;
					break;
				}
			}
			if(flag == 0)
			{
				res=j;
				break;
			}
		}
		printf("Case #%d: ",i+1);
		if(res == -1)
			printf("NO\n");
		else
			printf("%d\n",res);
		
	}
	return 0;
}