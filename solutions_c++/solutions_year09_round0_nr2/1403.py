#include <cstdio>
#include <iostream>
#include <queue>
#include <vector>
#include <stack>
#define  r first
#define  c second
using namespace std;
typedef pair<int,int> pii;

int dx[] = {-1, 0, 0, 1 };
int dy[] = {0, -1, 1, 0};

int N, R, C;
int arr[110][110];
char ans[110][110];
bool vis[110][110];

void findPath(stack<pii>& path, pii start);

int main()
{
	freopen("B.in", "r", stdin);
	freopen("B.txt", "w", stdout);
	int tcase, i, j, k;
	scanf("%d", &N);
	for(tcase = 1; tcase <= N; ++tcase)
	{
		
		scanf("%d%d", &R, &C);
		for(i = 0; i < R; ++i)
			for(j = 0; j < C; ++j) scanf("%d", &arr[i][j]);
		
	
		char next = 'a';
		memset(ans, 0, sizeof(ans));
		for(i = 0; i < R; ++i)
		{
			for(j = 0; j < C; ++j){
				if(ans[i][j] != 0) continue;

				stack<pii> path;
				findPath(path, pii(i, j));
				pii end = path.top();
				char tofill = ans[end.r][end.c];
				if(tofill == 0) tofill = next++;
				while(!path.empty())
				{
					end = path.top(); path.pop();
					ans[end.r][end.c] = tofill;
				}
			}
		}

		printf("Case #%d:\n", tcase);
		for(i = 0; i < R; ++i)
		{
			for(j = 0; j < C; ++j) {
				if(j) printf(" ");
				printf("%c", ans[i][j]);
			}
			puts("");
		}
	}
	return 0;
}

void findPath(stack<pii>& path, pii start)
{
	int x, y, k, X, Y;
	pii hold;
	path.push(start);
	while(true)
	{
		
		x = start.r, y = start.c;
		int minval = 1<<29;
		
		for(k = 0; k < 4; ++k) {
			int X = dx[k] + x, Y = dy[k] + y;
			if(!(X >= 0 && X < R && Y >= 0 && Y < C)) continue;
			if(arr[X][Y] < arr[x][y]){
				if(arr[X][Y] < minval) {
					minval = arr[X][Y];
					hold = pii(X, Y);
				}
			}
		}
		if(minval == 1 << 29) return;

		path.push(hold);
		if(ans[hold.r][hold.c] != 0) return;
		start = hold;
	}
	return;
}