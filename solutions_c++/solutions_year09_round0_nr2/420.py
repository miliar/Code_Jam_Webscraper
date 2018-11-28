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

using namespace std; 

#define rep(i,n) for(int i=0;i<(n);++i)
#define clr(a,b) memset(a,b,sizeof(a)); 
#define all(c) (c).begin(), (c).end() 
#define inf 1000000000 

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<string> vs;
typedef vector<int> vi;

int table[100][100];
int sink[100][100];
char ans[100][100];

int dx[] = {0, -1, 1, 0};
int dy[] = {-1, 0, 0, 1};

int W, H;

int findSink(int i, int j)
{
	if (sink[i][j] != -1)
		return sink[i][j];

	int bi = -1, bj = -1;


	for (int k = 0; k < 4; k++)
	{
		int ni = i + dy[k];
		int nj = j + dx[k];

		if (ni < 0 || nj < 0 || ni >= H || nj >= W)
			continue;
		
		if ((bi == -1) || (table[bi][bj] > table[ni][nj]))
		{
			bi = ni;
			bj = nj;
		}
	}
	
	int s;
	
	if (bi != -1 && table[bi][bj] < table[i][j])
	{
		s = findSink(bi, bj);
	}
	else
	{
		s = i * 100 + j;
	}
	sink[i][j] = s;		

	return s;
}

int main(int argc, char* argv[])
{
	freopen("Test.in", "r", stdin);
	//freopen("Test.out", "w", stdout);

	int T;
	scanf("%d", &T);

	for (int nTest = 1; nTest <= T; nTest++)
	{
		scanf("%d%d", &H, &W);

		for (int i = 0; i < H; i++)
		{
			for (int j = 0; j < W; j++)
			{
				scanf("%d", &table[i][j]);
			}
		}
		memset(sink, -1, sizeof(sink));

		for (int i = 0; i < H; i++)
		{
			for (int j = 0; j < W; j++)
			{
				findSink(i, j);
			}
		}
		memset(ans, 0, sizeof(ans));

		char c = 'a';

		for (int i = 0; i < H; i++)
		{
			for (int j = 0; j < W; j++)
			{
				int ni = sink[i][j] / 100;
				int nj = sink[i][j] % 100;
				
				if (ans[ni][nj] == 0)
				{
					ans[ni][nj] = c++;
				}
				ans[i][j] = ans[ni][nj];
			}
		}



		printf("Case #%i:\n", nTest);
		for (int i = 0; i < H; i++)
		{
			for (int j = 0; j < W; j++)
			{
				printf("%c%c", ans[i][j], j == W - 1 ? '\n' : ' ');
			}
		}
	}
 


	return 0;
}


