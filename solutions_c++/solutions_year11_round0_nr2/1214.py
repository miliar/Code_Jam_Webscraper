#include <iostream>
#include <cstdio>
#include <cstring>
#define see(x) cerr << "LINE " << __LINE__ << " : " << #x << " : " << x <<endl
using namespace std;
char xiao[40][5],fan[40][5];
void solve()
{
	int c,d,n;
	scanf("%d",&c);
	char str[200],ans[200];
	for(int i = 0;i < c;i++)
		scanf("%s",xiao[i]);
	scanf("%d",&d);
	for(int i = 0;i < d;i++)
		scanf("%s",fan[i]);
	scanf("%d",&n);
	scanf("%s",str);
	int l1 = 3,l2 = 2;
	int i = 0,now = 0;
	for(;i < n;i++)
	{
		bool flag = false;
		for(int k = 0;k < c && now > 0;k++)
		{
			int mark1 = -1,mark2 = -1;
			for(int p = 0;p < l1 - 1;p++)
			{
				if(xiao[k][p] == str[i] && mark1 == -1)
					mark1 = p;
				if(xiao[k][p] == ans[now - 1] && p != mark1)
					mark2 = p;
				if(mark1 != -1&& mark2 != -1)
					break;
			}
			if(mark1 != -1&& mark2 != -1)
			{
				flag = true;
				//see(now);
				ans[now - 1] = xiao[k][2];
				break;
			}
		}
		for(int j = 0;str[i] != ans[j] && !flag && j < now;j++)
		{
			for(int p = 0;p < d;p++)
			{
				int mark1 = -1,mark2 = -1;
				for(int k = 0;k < l2;k++)
				{
					if(str[i] == fan[p][k] && mark1 == -1)
						mark1 = k;
					if(ans[j] == fan[p][k] && k != mark1)
						mark2 = k;
					if(mark1 != -1 && mark2 != -1)
						break;
				}
				if(mark1!= -1 && mark2 != -1)
				{
					now = 0;
					flag = true;
					break;
				}
			}
		}
		if(!flag)
			ans[now++] = str[i];
		//see(ans[now - 1]);
	}
	putchar('[');
	for(int e = 0;e < now;e++)
	{
		if(e != 0)
			printf(", ");
		printf("%c",ans[e]);
	}
	puts("]");
}
int main()
{
	int t;
	scanf("%d",&t);
	for(int i = 1;i <= t;i++)
	{
		printf("Case #%d: ",i);
		solve();
	}
}
