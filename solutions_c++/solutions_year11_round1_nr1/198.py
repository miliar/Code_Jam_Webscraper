#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
#define LL long long

int main()
{
	int cases;
	scanf("%d",&cases);
	for (int tcase=1;tcase<=cases;tcase++)
	{
		LL pd,pg,n;
		cin >> n >> pd >> pg;
		bool flag=false;
		for (LL d=1;d<=205 && d<=n;d++)
		if (d*pd % 100 == 0)
		{
			int w = d*pd/100;
			for (LL x=1;x<=205;x++)
			if (d*x * pg % 100 ==0)
			{
				LL now=d*x*pg/100 ,l,r;
				l=w; r=(x-1)*d+w;
				// w <= d*x*pg/100 <= (x-1)*d+w
				//  d*x*pg/100 <= (x-1)*d+w
				if (l<=now && now<=r)
				{
					flag=true;
					break;
				}
			}
			if (flag) break;
		}
		printf("Case #%d: ",tcase);
		if (flag) puts("Possible");
			else puts("Broken");
	}
	return 0;
}
