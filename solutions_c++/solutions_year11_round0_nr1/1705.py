#include <stdio.h>
#include <algorithm>
using namespace std;


char cmd[5];

int main()
{
	int t;
	int n, pos;
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	scanf("%d", &t);
	for (int test = 1; test <= t; ++test)
	{
		scanf("%d", &n);
		int ans = 0;
		int leftB = 0;
		int leftO = 0;
		int posB = 1;
		int posO = 1;

		//在前一个命令执行前，后一个命令只能到达指定位置等待
		//为每个机器人记录一个时间t，表示该机器人还有t步没走
		for (int i = 0; i < n; ++i)
		{
			scanf("%s%d", cmd, &pos);
			if ('O' == cmd[0])
			{
				int temp = abs(posO - pos) - leftO;
				//够走
				if (temp <= 0)
				{
					ans += 1;
					leftB += 1;
				}
				else
				{
					ans += temp + 1;
					leftB += temp + 1;
				}
				posO = pos;
				leftO = 0;
			}
			else if ('B' == cmd[0])
			{

				int temp = abs(posB - pos) - leftB;
				//够走
				if (temp <= 0)
				{
					ans += 1;
					leftO += 1;
				}
				else
				{
					ans += temp + 1;
					leftO += temp + 1;
				}
				posB = pos;
				leftB = 0;
			}

		}

		printf("Case #%d: %d\n", test, ans);
	}
	return 0;
}