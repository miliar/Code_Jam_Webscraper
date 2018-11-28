#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <bitset>
#include <sstream>
#include <string>

#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>

#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>

#define FILL(arr,n) memset(arr,n,sizeof(arr))
#define FORUP(i,m,n) for(int i=(m); i<(n); i++)
#define FORDOWN(i,m,n) for(int i=(m)-1; i>=(n); i--)

#define PB push_back
#define MP make_pair
#define F first
#define S second

#define INF 2000000000
#define EPS 1e-11
#define PI acos(-1.0)
#define MAX_N 1000005
using namespace std;

typedef long long ll;
typedef pair<int,int> pii;
typedef vector<pii> vii;

char petak[5][5];

int
main()
{
	int T;
	bool isFinished;
	scanf("%d", &T);
	for(int tc = 1;tc <= T;tc++)
	{
		isFinished = true;
		for(int i = 0;i < 4;i++)
		{
			scanf("%s", petak[i]);
			for(int j = 0;j < 4 && isFinished;j++)
			{
				if(petak[i][j] == '.')
				{
					isFinished = false;
				}
			}
		}
		int ans = 0;
		bool yes;
		for(int i = 0;i < 4 && ans == 0;i++)
		{
			for(int j = 0;j < 4 && ans == 0;j++)
			{
				if(i == 0)
				{
					if(petak[i][j] == 'T' || petak[i][j] == 'O')
					{
						yes = true;
						for(int k = 1;k < 4;k++)
						{
							if(petak[k][j] != 'O' && petak[k][j] != 'T')
							{
								yes = false;
								break;
							}
						}
						if(yes) ans = 1;
					}
					if(petak[i][j] == 'T' || petak[i][j] == 'X')
					{
						yes = true;
						for(int k = 1;k < 4;k++)
						{
							if(petak[k][j] != 'X' && petak[k][j] != 'T')
							{
								yes = false;
								break;
							}
						}
						if(yes) ans = 2;
					}
				}
				if(j == 0)
				{
					if(petak[i][j] == 'T' || petak[i][j] == 'O')
					{
						yes = true;
						for(int k = 1;k < 4;k++)
						{
							if(petak[i][k] != 'O' && petak[i][k] != 'T')
							{
								yes = false;
								break;
							}
						}
						if(yes) ans = 1;
					}
					if(petak[i][j] == 'T' || petak[i][j] == 'X')
					{
						yes = true;
						for(int k = 1;k < 4;k++)
						{
							if(petak[i][k] != 'X' && petak[i][k] != 'T')
							{
								yes = false;
								break;
							}
						}
						if(yes) ans = 2;
					}
				}
				if(i == 0 && j == 0)
				{
					if(petak[i][j] == 'T' || petak[i][j] == 'O')
					{
						yes = true;
						for(int k = 1;k < 4;k++)
						{
							if(petak[i+k][j+k] != 'O' && petak[i+k][j+k] != 'T')
							{
								yes = false;
								break;
							}
						}
						if(yes) ans = 1;
					}
					if(petak[i][j] == 'T' || petak[i][j] == 'X')
					{
						yes = true;
						for(int k = 1;k < 4;k++)
						{
							if(petak[i+k][j+k] != 'X' && petak[i+k][j+k] != 'T')
							{
								yes = false;
								break;
							}
						}
						if(yes) ans = 2;
					}
				}
				if(i == 3 && j == 0)
				{
					if(petak[i][j] == 'T' || petak[i][j] == 'O')
					{
						yes = true;
						for(int k = 1;k < 4;k++)
						{
							if(petak[i-k][j+k] != 'O' && petak[i-k][j+k] != 'T')
							{
								yes = false;
								break;
							}
						}
						if(yes) ans = 1;
					}
					if(petak[i][j] == 'T' || petak[i][j] == 'X')
					{
						yes = true;
						for(int k = 1;k < 4;k++)
						{
							if(petak[i-k][j+k] != 'X' && petak[i-k][j+k] != 'T')
							{
								yes = false;
								break;
							}
						}
						if(yes) ans = 2;
					}

				}
			}
		}
		printf("Case #%d: ",tc);
		if(ans == 0)
		{
			if(isFinished)printf("Draw\n");
			else printf("Game has not completed\n");
		}
		else if(ans == 1)
		{
			printf("O won\n");
		}
		else
		{
			printf("X won\n");
		}
	}
}