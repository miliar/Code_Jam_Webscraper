#include <cstdio>
#include <string>
#include <cmath>
#include <vector>
#include <memory>
#include <algorithm>
using namespace std;
int main(void)
{
	int t,n,p,p1,p2,d1,d2,q;
	char c;
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&t);
	for (q = 1; q <= t; q++)
	{
 		scanf("%d",&n);
		int ans = 0;
		int p1 = 1, p2 = 1, d1 = 0, d2 = 0;
		for (int i = 0 ; i < n ; i++)
		{
			scanf("%c%c%d",&c,&c,&p);
			if (c == 'O')
			{
				if (((p1 - d1)<=p)&&((p1+d1)>=p))
				{
					p1 = p;
					ans += 1;
					d2 += 1;
					d1 = 0;
				} else
					if (p > (p1+d1))
					{
						ans += (p - (p1+d1))+1;
						d2 += (p-(p1+d1))+1;
						p1 = p;
						d1 = 0;
					} else
					{
						ans += ((p1-d1)-p)+1;
						d2 += ((p1-d1)-p)+1;
						p1 = p;
						d1 = 0;
					}
			} else
			{
				if (((p2 - d2)<=p)&&((p2+d2)>=p))
				{
					p2 = p;
					ans += 1;
					d1 += 1;
					d2 = 0;
				} else
					if (p > (p2+d2))
					{
						ans += (p - (p2+d2))+1;
						d1 += (p-(p2+d2))+1;
						p2 = p;
						d2 = 0;
					} else
					{
						ans += ((p2-d2)-p)+1;
						d1 += ((p2-d2)-p)+1;
						p2 = p;
						d2 = 0;
					}
			
			}
		}
		printf("Case #%d: %d\n",q,ans);
	}
	return 0;
}