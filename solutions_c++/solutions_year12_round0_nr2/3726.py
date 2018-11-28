#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cmath>
using namespace std;

int main()
{
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-small-attempt0.out","w",stdout);
	int t,n,s,p,i,Case=1;
	int elem[105];
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d %d %d",&n,&s,&p);
		for(i = 1; i <= n; i++)
		{
			scanf("%d",&elem[i]);
			if(elem[i] % 3 == 0)
				elem[i] /= 3;
			else
				elem[i] = (elem[i]/3) + 1;
		}
		int ans = 0;
		for(i = 1; i <= n; i++)
		{
			if(elem[i] >= p)
			{
				ans++;
			}
			else
			{
				if(s != 0 && elem[i] + 1 >= p && elem[i] != 0)
				{
					ans++;
					s--;
				}
			}
		}
		printf("Case #%d: %d\n",Case++,ans);
    }
    return 0;
}

