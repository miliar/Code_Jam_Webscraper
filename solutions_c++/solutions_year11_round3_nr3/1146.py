#include <iostream>
#include <cstdio>
#include <memory.h>
#include <string>
#include <cstring>
#include <algorithm>
using namespace std;
int p[105];
int gcd(int a,int b)
{
	if (b == 0)
		return a;
	else
		return gcd(b,a % b);
}
int lcm(int a,int b)
{
	return a * b / gcd(a,b);
}
int main()
{
	int i,j,k,m,n,t,cas = 1;
	int num,l,r,res,res1,cnt,cnt1;
	bool flag;
	freopen("C-small-attempt1.in","r",stdin);
	freopen("C-small-attempt1.out","w",stdout);
	scanf("%d",&t);
	while (t--)
	{
		printf("Case #%d: ",cas++);
		scanf("%d %d %d",&n,&l,&r);
		for (i = 0;i < n; i++)
			scanf("%d",&p[i]);
		bool find;
		for (i = l;i <= r;i++)
		{
			find = true;
			for (j = 0;j < n;j++)
			{
				cnt = min(i,p[j]);
				cnt1 = max(i,p[j]);
				if (cnt1 % cnt != 0)
				{
					find = false;
					break;
				}
			}
			if (find)
			{
				printf("%d\n",i);
				break;
			}
		}
		if (!find)
			printf("NO\n");
	}
	return 0;
}