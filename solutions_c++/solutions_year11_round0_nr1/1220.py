#include <iostream>
#include <cstdio>
using namespace std;
struct step
{
	int pos;
	bool flag;
}s[200];
int solve()
{
	int n;
	scanf("%d",&n);
	for(int i = 1;i <= n;i++)
	{
		int a;
		char b;
		scanf(" %c %d",&b,&a);
		s[i].pos = a;
		s[i].flag = (b == 'B') ? 1 : 0;
	}
	int ans = 0,now = 1,p1 = 1,p2 = 1;
	while(now <= n)
	{
		if(s[now].flag == 1)
		{
			int mark = now;
			for(int i = now;i <= n;i++)
				if(s[i].flag == 0)
				{
					mark = i;
					break;
				}
			if(p1 > s[now].pos)
				p1--;
			else if(p1 < s[now].pos)
				p1++;
			else
				now++;
			if(p2 < s[mark].pos)
				p2++;
			else if(p2 > s[mark].pos)
				p2--;
		}
		else
		{
			int mark = now;
			for(int i = now;i <= n;i++)
				if(s[i].flag == 1)
				{
					mark = i;
					break;
				}
			if(p2 < s[now].pos)
				p2++;
			else if(p2 > s[now].pos)
				p2--;
			else
				now++;
			if(p1 < s[mark].pos)
				p1++;
			else if(p1 > s[mark].pos)
				p1--;
		}
		ans++;
	}
	return ans;
}
int main()
{
	int t;
	scanf("%d",&t);
	for(int i = 1;i <= t;i++)
	{
		printf("Case #%d: %d\n",i,solve());
	}
}
