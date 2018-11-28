
#include <iostream>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include <string>
#include <cstdio>
#include <algorithm>

using namespace std;

int o,b;

int Abs(int x)
{
	return x>0 ? x:-x;
}

int main()
{
	int t,n,i,ans,k,j;
	freopen("A.out","w",stdout);
	char str[10];
	while(scanf("%d",&t ) == 1)
	{
		int d = 1;
		while(t--)
		{
			int to,tb,temp;
			to = tb = 0;
			o = b = 1;
			ans = 0;
			scanf("%d",&n);
			for(i=0;i<n;i++)
			{
				scanf("%s %d",str,&k);
				if(str[0] == 'B')
				{
					temp = Abs(b-k)-tb;
					if(temp <= 0)
					{
						ans++;
						to++;
						tb = 0;
					}
					else
					{
						ans += temp+1;
						to += temp+1;
						tb = 0;
					}
					b = k;
				}
				else
				{
					temp = Abs(o-k)-to;
					if(temp <= 0)
					{
						ans++;
						tb++;
						to = 0;
					}
					else
					{
						ans += temp+1;
						tb += temp+1;
						to = 0;
					}
					o = k;
				}
			}
			printf("Case #%d: %d\n",d++,ans);
		}
	}
	return 0;
}
/*
4 O 2 B 1 B 2 O 4
3 O 5 O 8 B 100
2 B 2 B 1

*/