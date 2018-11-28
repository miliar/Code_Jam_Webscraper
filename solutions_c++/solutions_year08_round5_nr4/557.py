#include <string>
#include <vector>
#include <iostream>
#include <sstream>
#include <string>
#include <stack>
#include <deque>
#include <set>
#include <map>
#include <algorithm>
#include <iterator>
#include <cmath>
#include <memory>
#include <cstdlib>

using namespace std;

int H,W;

int cant[110][110];

int mas[110][110];
int used[110][110];

#define MOVES 2
int DX[] = {2,1};
int DY[] = {1,2};

int run(int x, int y)
{
	if (used[x][y] == 1)
		return mas[x][y];
	int res = 0;
	for (int i=0; i<MOVES; i++)
	{
		int nx = x+DX[i];
		int ny = y+DY[i];
		if (nx > H)
			continue;
		if (ny > W)
			continue;
		if (cant[nx][ny] == 0)
			res += run(nx,ny);
	}
	used[x][y] = 1;
	res %= 10007;
	mas[x][y] = res;
	return res;
}

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int tt=1; tt<=T; tt++)
	{
		cerr << tt << endl;

		int R;
		scanf("%d%d%d", &H, &W, &R);
		memset(used,0,sizeof(used));
		memset(cant,0,sizeof(cant));
		for (int i=0; i<R; i++)
		{
			int r,c;
			scanf("%d%d", &r, &c);
			cant[r][c] = 1;
		}
		used[H][W] = 1;
		mas[H][W] = 1;
		int res = run(1,1);
		res %= 10007;
		printf("Case #%d: %d\n", tt, res);

	}
	return 0;
}