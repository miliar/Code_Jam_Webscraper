#include <stdlib.h>
#include <iostream>
#include <math.h>
using namespace std;
int g[1005];
int main()
{
	freopen ("C-largeout.txt","w",stdout);
	int t,n,k,r;
	int m;
	scanf("%d",&t);
	for (int i=1;i<=t;i++)
	{
		scanf ("%d%d%d",&r,&k,&n);
		for (int j=0;j<n;j++)
			scanf("%d",&g[j]);
		int cnt=0;
		int point=0;
		int cur=0;
		int sum=0;
		int num=0;
		while(cnt<r)
		{
			while(cur<k)
			{
				if (cur+g[point]<=k&&num<n)
				{
					cur+=g[point];
					point++;
					num++;
					point%=n;

				}
				else break;
			}
			cnt++;
			sum+=cur;
			cur=0;
			num=0;
			if (point==0)
				break;
		}
		if(cnt<r)
		{
			int shang=r/cnt;
			int yu=r%cnt;
			sum*=shang;
			cnt=0;
			cur=0;
			point=0;
			while(cnt<yu)
			{
				while(cur<k)
				{
					if (cur+g[point]<=k&&num<n)
					{
						cur+=g[point];
						point++;
						num++;
						point%=n;
						
					}
					else break;
				}
				cnt++;
				sum+=cur;
				num=0;
				cur=0;
			}
		}
		printf("Case #%d: %d\n",i,sum);

	}
	return 0;
}