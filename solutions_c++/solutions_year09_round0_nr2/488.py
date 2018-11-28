#include <vector> 
#include <list> 
#include <map> 
#include <set> 
#include <deque> 
#include <queue> 
#include <stack> 
#include <bitset> 
#include <algorithm> 
#include <functional> 
#include <numeric> 
#include <utility> 
#include <sstream> 
#include <iostream> 
#include <iomanip> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <cctype> 
#include <string> 
#include <cstring> 
#include <ctime> 
using namespace std;
typedef long long ll;


int graph[110][110];
int altitude[110][110];
int used[30];
int T,h,w,now;
int dx[] = {-1, 0, 0, 1};
int dy[] = {0, -1, 1, 0};
int go(int x, int y)
{
	if(graph[x][y] >= 0) return graph[x][y];
	int tos = 1000000000, ind = -1;
	for(int i = 0; i < 4; i++)
	{
		int nx = x + dx[i];
		int ny = y + dy[i];
		if(nx >= 0 && nx < h && ny >= 0 && ny < w && altitude[nx][ny] < altitude[x][y] && altitude[nx][ny] < tos)
		{
			tos = altitude[nx][ny];
            ind = i;
		}
	}
	if(ind == -1) 
	{
		graph[x][y] = now++;
	}
	else
	{
		graph[x][y] = go(x + dx[ind], y + dy[ind]);
	}
	return graph[x][y];
}
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	scanf("%d", &T);
	for(int k = 0; k < T; k++)
	{
		scanf("%d%d", &h, &w);
		for(int i = 0; i < h; i++)
			for(int j = 0; j < w; j++)
			{
				scanf("%d", &altitude[i][j]);
			}

		memset(graph, 0xff, sizeof graph);
		now = 0;
		for(int i = 0; i < h; i++)
		{
			for(int j = 0; j < w; j++)
			{
				go(i, j);
			}
		}
        
        now = 'a';
		memset(used, 0xff, sizeof used);
		for(int i = 0; i < h; i++)
		{
			for(int j = 0; j < w; j++)
			{
				if(graph[i][j] < 'a')
				{
					if(used[graph[i][j]] != -1)
						graph[i][j] = used[graph[i][j]];
					else
					{
						used[graph[i][j]] = now;
						graph[i][j] = now++;
					}
				}
			}
		}

		printf("Case #%d:\n", k + 1);
		for(int i = 0; i < h; i++)
		{
			printf("%c", (char)graph[i][0]);
			for(int j = 1; j < w; j++)
			{
				printf(" %c", (char)graph[i][j]);
			}
			puts("");
		}
	}
	
}
