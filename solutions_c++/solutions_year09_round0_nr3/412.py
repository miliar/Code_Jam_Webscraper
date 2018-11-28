//============================================================================
// Name        : welcome.cpp
// Author      : Fify
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <memory.h>
using namespace std;

char wel[] = "welcome to code jam";
const int LEN = 19;

int ans[LEN + 1][505];
char str[505];

int main()
{
	freopen("/home/fify/Desktop/data3.in", "r", stdin);
	freopen("/home/fify/Desktop/data3.out", "w", stdout);
	void solve();
	int t;
	//cin>>t;
	scanf("%d", &t);
	getchar();
	for(int i = 0;i<t;i++)
	{
		solve();
	}
	return 0;
}

void solve()
{
	static int cas = 1;
	memset(ans, 0, sizeof(ans));

	gets(str);

	if(str[0] == wel[0])
		ans[0][0] = 1;
	else
		ans[0][0] = 0;

	int len = (int)strlen(str);
	for(int i = 1;i<len;i++)
	{
		ans[0][i] = ans[0][i-1];
		if(str[i] == wel[0])
		{
			ans[0][i] ++;
		}
	}
	for(int i = 1;i<LEN;i++)
	{
		for(int j = 0;j<len; j++)
		{
			ans[i][j] = ans[i][j-1];
			if(str[j] == wel[i])
			{
				ans[i][j] += ans[i-1][j-1];
				if(ans[i][j] >= 10000)
				{
					ans[i][j] %= 10000;
				}
			}
		}
	}

	printf("Case #%d: %04d\n", cas++, ans[LEN-1][len-1]);
}

