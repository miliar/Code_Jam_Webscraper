#include<iostream>
#include<cstdio>

using namespace std;

#define MAXS 3010
#define MAXM 10010
const int inf = 1000000000;

const int dx[6] = {-1, -1, 0, 1, 1, 0};
const int dy[6] = {-1, 0, 1, 1, 0, -1}; 
const int corner[6] = {2, 4, 8, 16, 32, 64};
const int edge[6] = {128, 256, 512, 1024, 2048, 4096};

int Map[MAXS * 2][MAXS * 2];
int father[MAXS * MAXS * 4]; 
int S, M;
int x[MAXM], y[MAXM];

int findfather(int t)
{
	if (father[t] == -1) return t;
	else return (father[t] = findfather(father[t]));
}

void mrg(int a, int b)
{
	if (findfather(a) != findfather(b))
	father[findfather(a)] = findfather(b);
}

bool CheckSame(int x1, int y1, int x2, int y2)
{
	//cout << x1 << " " << y1 << " " << x2 << " " << y2 << endl;
	//cout << findfather(x1 * MAXS * 2 + y1) << " " << findfather(x2 * MAXS * 2 + y2) << endl;
	if (findfather(x1 * MAXS * 2 + y1) == findfather(x2 * MAXS * 2 + y2)) return true;
	else return false;
}

void Spread(int x, int y)
{
	//cout << x << " " << y << endl;
	for (int i = 0; i < 6; i++ )
	if ( Map[x + dx[i]][y + dy[i]] > 0 )
		Map[x][y] |= Map[x + dx[i]][y + dy[i]];
	for (int i = 0; i < 6; i++ )
	if ( Map[x + dx[i]][y + dy[i]] > 0 )
	if ( Map[x + dx[i]][y + dy[i]] < Map[x][y] )
		Spread(x + dx[i], y + dy[i]);
}

void Merge(int x, int y)
{
	for (int i = 0; i < 6; i++ )
	if ( Map[x + dx[i]][y + dy[i]] > 0 )
		mrg(x * MAXS * 2 + y, (x + dx[i]) * MAXS * 2 + y + dy[i]);
}

bool CheckWinning(int x, int y, int casen, int movek)
{
	int cntC = 0, cntE = 0;
	for (int i = 0; i < 6; i++ )
	if ((Map[x][y] & corner[i]) > 0) cntC ++;
	for (int i = 0; i < 6; i++ )
	if ((Map[x][y] & edge[i]) > 0) cntE ++;
	int R = 0, blocks[6];
	for (int i = 0; i < 6; i++ )
	if (Map[x + dx[i]][y + dy[i]] > 0 && Map[x + dx[(i + 1) % 6]][y + dy[(i + 1) % 6]] == 0)
		blocks[R++] = i;
	bool circleE = false;
	for (int i = 0; i < R; i++ )
		for (int j = i + 1; j < R; j++ )
			if (CheckSame(x + dx[blocks[i]], y + dy[blocks[i]], x + dx[blocks[j]], y + dy[blocks[j]])) circleE = true;
	bool ret = false;
	if (cntC >= 2 || cntE >= 3 || circleE) ret = true;
	if (cntC >= 2 && cntE >= 3 && circleE) printf( "Case #%d: bridge-fork-ring in move %d\n", casen, movek );	
	else if (cntC >= 2 && cntE >= 3) printf( "Case #%d: bridge-fork in move %d\n", casen, movek );	
	else if (cntC >= 2 && circleE) printf( "Case #%d: bridge-ring in move %d\n", casen, movek );	
	else if (cntE >= 3 && circleE) printf( "Case #%d: fork-ring in move %d\n", casen, movek );	
	else if (cntC >= 2) printf( "Case #%d: bridge in move %d\n", casen, movek );	
	else if (cntE >= 3) printf( "Case #%d: fork in move %d\n", casen, movek );	
	else if (circleE) printf( "Case #%d: ring in move %d\n", casen, movek );	
	return ret;
}

void solve(int casen)
{
	scanf( "%d %d", &S, &M );
	memset( Map, 0, sizeof( Map ) );
	memset( father, 0xff, sizeof( father ) );
	for (int i = 0; i < M; i++ )
		scanf( "%d %d", &x[i], &y[i] );
	for (int i = 0; i < M; i++ )
	{		
		Map[x[i]][y[i]] |= 1;
		
		if (x[i] == 1) Map[x[i]][y[i]] |= edge[0];
		if (y[i] == 1) Map[x[i]][y[i]] |= edge[1];
		if (x[i] - y[i] == S - 1) Map[x[i]][y[i]] |= edge[2];
		if (x[i] == 2 * S - 1) Map[x[i]][y[i]] |= edge[3];
		if (y[i] == 2 * S - 1) Map[x[i]][y[i]] |= edge[4];
		if (y[i] - x[i] == S - 1) Map[x[i]][y[i]] |= edge[5]; 
		for (int k = 0; k < 6; k++ )
		if ( (Map[x[i]][y[i]] & edge[k]) > 0 )
		if ( (Map[x[i]][y[i]] & edge[(k + 1) % 6]) > 0 )
		{
			Map[x[i]][y[i]] |= corner[k];
			Map[x[i]][y[i]] -= edge[k];
			Map[x[i]][y[i]] -= edge[(k + 1) % 6];
		}
		Spread(x[i], y[i]);
		if ( CheckWinning(x[i], y[i], casen, i + 1) ) return;	
		Merge(x[i], y[i]);		
	}
	printf( "Case #%d: none\n", casen );
}

int main()
{
	freopen( "in.txt", "r", stdin );
	freopen( "out.txt", "w", stdout );
	int test_cases;
	scanf( "%d", &test_cases );
	for (int i = 1; i <= test_cases; i++ )
		solve(i);
}

 