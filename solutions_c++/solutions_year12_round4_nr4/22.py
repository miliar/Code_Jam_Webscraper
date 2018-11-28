#include<iostream>
#include<cstdio>

using namespace std;

#define MAXM 15
const int inf = 1000000000;

const int dx[3] = {1, 0, 0};
const int dy[3] = {0, 1, -1};

int R,C;
char map[MAXM][MAXM];
bool reach[MAXM][MAXM];
bool here[MAXM][MAXM];

int countt;

void dfs(int x, int y)
{
	if (map[x][y] == '#') return;
	if (!reach[x][y]) reach[x][y] = true;
	else return;
	countt ++;
	
	for (int i = 0; i < 3; i++ )
		dfs(x - dx[i], y - dy[i]);
}

bool testdir(int dir)
{
	bool nhere[MAXM][MAXM];
	memset( nhere, false, sizeof(nhere) );
	bool effect = false;
	for (int i = 0; i < R; i++ )
	for (int j = 0; j < C; j++ )
	if ( here[i][j] ){
		int nx = i + dx[dir], ny = j + dy[dir];
		if (map[nx][ny] == '#'){
			nhere[i][j] = true;
		}
		else{
			if (!reach[nx][ny]) return false;
			effect = true;
			nhere[nx][ny] = true;
		}
	}
	if ( effect )
		memcpy( here, nhere, sizeof( here ) );
	return effect;
}

bool search(int dir, int turns){
	if (turns > 2) return false;
	int cnt = 0;
	for (int i = 0; i < R; i++ )
		for (int j = 0; j < C; j++ )
			if ( here[i][j] ) cnt ++;
	if ( cnt == 1 ) return true;
	bool there[MAXM][MAXM];
	memcpy( there, here, sizeof( here ) );
	if (testdir(0)){
		if ( search(0, 0) ) return true;
		memcpy( here, there, sizeof( here ) );
	}
	if (dir == 2) {
		if ( testdir(2) ){
			if ( search(2, turns) ) return true;
			memcpy( here, there, sizeof( here ) );
		}
		if ( testdir(1) ){
			if (search(1, turns + 1)) return true;
			memcpy( here, there, sizeof( here ) );		
		}
	}
	else {
		if ( testdir(1) ){
			if (search(1, turns)) return true;
			memcpy( here, there, sizeof( here ) );
		}
		if ( testdir(2) ){
			if (search(2, turns + dir)) return true;
			memcpy( here, there, sizeof( here ) );				
		}
	}
	return false;
}

void solve_cave(int cave){
	int cx, cy;
	for (int i = 0; i < R; i++ )
		for (int j = 0; j < C; j++ )
			if ( map[i][j] == '0' + cave )
			{
				cx = i;
				cy = j;
			}
	memset( reach, false, sizeof( reach ) );
	countt = 0;
	dfs(cx, cy);
	memcpy( here, reach, sizeof( reach ) );
	
	bool res = search(0, 0);
	printf( "%d: %d ", cave, countt );
	if (res) printf( "Lucky\n" );
	else printf( "Unlucky\n" );
}

void solve(int casen)
{
	scanf( "%d %d", &R, &C );
	for (int i = 0; i < R; i++ )
		scanf( "%s", map[i] );
	printf( "Case #%d:\n", casen );
	int caves = 0;
	for (int i = 0; i < R; i++ )
		for (int j = 0; j < C; j++ ) 
			if (map[i][j] >= '0' && map[i][j] <= '9')
				caves ++;
	for (int i = 0; i < caves; i++ )
		solve_cave(i);
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

 