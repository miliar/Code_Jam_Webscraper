
#include <iostream>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include <string>
#include <cstdio>
#include <algorithm>

using namespace std;

int a[1000];

int main()
{
	int t;
	int n,l,h,i,j;
	freopen("C.out","w",stdout);
	scanf("%d",&t);
	int d = 1;
	while(t--)
	{
		scanf("%d %d %d",&n,&l,&h);
		for(i=0;i<n;i++)
			scanf("%d",&a[i]);
		printf("Case #%d: ",d++);	
		for(i=l;i<=h;i++)
		{
			for(j=0;j<n;j++)
			{
				if(a[j]%i==0 || i%a[j]==0)
					continue;
				else break;
			}
			if(j == n) break;
		}
		if(i == h+1)
			printf("NO\n");
		else
			printf("%d\n",i);
	}
	return 0;
}