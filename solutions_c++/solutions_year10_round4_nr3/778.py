// C.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <iostream>
#include <string>
using namespace std;

int bact[105][105];
int bact2[105][105];

int _tmain(int argc, _TCHAR* argv[])
{
	freopen("data.txt", "r", stdin);
	freopen("data.out", "w", stdout);

	void solve();

	int t;
	cin >> t;
	for(int i = 0;i<t;i++)
	{
		solve();
	}
	return 0;
}

void solve()
{
	memset(bact, 0, sizeof(bact));

	int r;
	int x1, x2, y1, y2;
	cin >> r;
	for(int i = 0;i<r;i++)
	{
		cin >> x1 >> y1 >> x2 >> y2;
		for(int j = x1;j<=x2;j++)
		{
			for(int k = y1;k<=y2;k++)
			{
				bact[j][k] = 1;
			}
		}
	}

	int envolve();
	int envolve2();

	int ans = 0;
	while(1)
	{
		if(envolve())
		{
			ans ++;
		}
		else
			break;

		if(envolve2())
		{
			ans ++;
		}
		else
			break;
	}

	//cout << ans + 1 << endl;
	static int cas = 1;
	printf("Case #%d: %d\n", cas ++, ans + 1);
}

int envolve( )
{
	memset(bact2, 0, sizeof(bact2));
	int ans = 0;
	for(int i = 0;i<=100;i++)
	{
		bact2[i][0] = bact2[0][i] = 0;
	}
	for(int i = 1;i<=100;i++)
	{
		for(int j = 1;j<=100;j++)
		{
			if(bact[i][j] == 1)
			{
				if(bact[i - 1][j] == 0 && bact[i][j - 1] == 0)
				{
					bact2[i][j] = 0;
				}
				else
				{
					bact2[i][j] = 1;
					ans = 1;
				}
			}
			else if(bact[i][j] == 0)
			{
				if(bact[i - 1][j] == 1 && bact[i][j - 1] == 1)
				{
					bact2[i][j] = 1;
					ans = 1;
				}
				else
				{
					bact2[i][j] = 0;
				}
			}
		}
	}

	return ans;
}

int envolve2( )
{
	memset(bact, 0, sizeof(bact));
	int ans = 0;
	for(int i = 0;i<=100;i++)
	{
		bact[i][0] = bact[0][i] = 0;
	}
	for(int i = 1;i<=100;i++)
	{
		for(int j = 1;j<=100;j++)
		{
			if(bact2[i][j] == 1)
			{
				if(bact2[i - 1][j] == 0 && bact2[i][j - 1] == 0)
				{
					bact[i][j] = 0;
				}
				else
				{
					bact[i][j] = 1;
					ans = 1;
				}
			}
			else if(bact2[i][j] == 0)
			{
				if(bact2[i - 1][j] == 1 && bact2[i][j - 1] == 1)
				{
					bact[i][j] = 1;
					ans = 1;
				}
				else
				{
					bact[i][j] = 0;
				}
			}
		}
	}

	return ans;
}