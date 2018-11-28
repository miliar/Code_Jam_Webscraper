#include <assert.h> 
#include <ctype.h> 
#include <float.h> 
#include <math.h> 
#include <stdio.h> 
#include <string> 
#include <stdlib.h> 
#include <time.h> 
#include <algorithm> 
#include <numeric> 
#include <functional> 
#include <utility> 
#include <vector> 
#include <list> 
#include <set> 
#include <map> 
#include <queue> 
#include <stack> 
#include <sstream> 
#include <iostream> 
#include <memory.h>

using namespace std; 

#define rep(i,n) for(int i=0;i<(n);++i)
#define clr(a,b) memset(a,b,sizeof(a)); 
#define all(c) (c).begin(), (c).end() 
#define inf 1000000000 

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<string> vs;
typedef vector<int> vi;

char table[10][10];
int vis[10][10];
int R, C;

int dx[] = {1, 0, -1, 0, 1, 1, -1, -1};
int dy[] = {0, -1, 0, 1, 1, -1, -1, 1};

int orient[10][10][2];
void brute();

void start(int fx, int fy, int x, int y, int len)
{
	y = (y + R) % R;
	x = (x + C) % C;

	if (x == fx && y == fy && len)
	{
		brute();
		return;
	}
	if (vis[y][x])
		return;

	vis[y][x] = 1;


	for (int i = 0; i < 2; i++)
	{
		start(fx, fy, x + dx[orient[y][x][i]], y + dy[orient[y][x][i]], len + 1);
	}

	vis[y][x] = 0;
}
int ans;
void brute()
{
	for (int i = 0; i < R; i++)
	{
		for (int j = 0; j < C; j++)
		{
			if (vis[i][j] == 0)
			{

				start(j, i, j, i, 0);


				return;
			}
		}
	}

	ans++;
}

void solveTest()
{
	cin >> R >> C;
	for (int i = 0; i < R; i++)
	{
		scanf("%s", table[i]);

		for (int j = 0; j < C; j++)
		{
			if (table[i][j] == '|')
			{
				orient[i][j][0] = 1;
				orient[i][j][1] = 3;
			}
			else if (table[i][j] == '-')
			{
				orient[i][j][0] = 0;
				orient[i][j][1] = 2;
			}
			else if (table[i][j] == '/')
			{
				orient[i][j][0] = 5;
				orient[i][j][1] = 7;


			}
			else if (table[i][j] == '\\')
			{
				orient[i][j][0] = 4;
				orient[i][j][1] = 6;


			}
			else
			{
				assert	 (false);
			}
		}
	}

	ans = 0;
	brute();

	printf("%d\n", ans);

}



int main(int argc, char* argv[])
{
	freopen("test.in", "r", stdin);

	int T;
	scanf("%d", &T);

	for (int nTest = 1; nTest <= T; nTest++)
	{		
		printf("Case #%d: ", nTest);

		solveTest();

		fflush(stdout);
	} 

	return 0;
}


