#include <iostream>
#include <stdio.h>
using namespace std;
int cal(int l,int p,int c)
{
	int ans=0;
	int h=p;
	while (h>l)
	{
		ans++;
		if (h%c==0)
		{
			h=h/c;
		}
		else h=h/c+1;		
	}
	return ans;
}

int main()
{
	freopen("g2.in","r",stdin);
	freopen("g2.out","w",stdout);
	int t;
	int l,p,c;
	int ans;
	int a;
	scanf("%d",&t);
	int i;
	for(i = 1;i <= t;i++)
	{
		scanf("%d%d%d",&l,&p,&c);
		ans = cal(l,p,c);
		a = 0;
		while (ans != 1)
		{
			if (ans %2 == 0)
			{
				ans /= 2;
				a++;
			}
			else
			{
				a++;
				ans /= 2;
				ans += 1;
			}
		}
		printf("Case #%d: %d\n",i,a);
	}
}