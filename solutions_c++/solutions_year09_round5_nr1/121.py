#include<iostream>
#include<cstdio>
#include<vector>
#include<algorithm>

using namespace std;

const int dx[4] = {0, 1, 0, -1};
const int dy[4] = {1, 0, -1, 0};

struct pos
{
	int x, y;
};

const int bigprime = 910109;

vector<pos> Q[5];
vector<pos> hashtable[910109][5];
pos bpos[5], cpos[5], tpos[5], epos[5];

int ans, bR, cR;
int Dg[1000000], cost[1000000];
char map[20][20];
int R, C;

bool operator==( const pos &A, const pos &B )
{
	return (A.x == B.x && A.y == B.y);
}

bool operator!=( const pos &A, const pos &B )
{
	return !(A.x == B.x && A.y == B.y);
}

bool operator<(const pos &A, const pos &B )
{
	if ( A.x != B.x ) return (A.x < B.x);
	else return (A.y < B.y);
}

bool v[5];
int dfs(int t)
{
	v[t] = false;
	int ret = 1;
	for (int i = 0; i < bR; i++ )
	if ( v[i] && abs(tpos[i].x - tpos[t].x) + abs(tpos[i].y - tpos[t].y) == 1 ) ret += dfs(i);
	return ret;
}

bool indanger()
{
	memset(v, true, sizeof(v));
	return (dfs(0) != bR);
}

bool checkvalid()
{
	for (int i = 0; i < bR; i++ )
		if ( tpos[i].x < 0 || tpos[i].x >= R || tpos[i].y < 0 || tpos[i].y >= C ) return false;
	for (int i = 0; i < bR; i++ )
		for (int j = i + 1; j < bR; j++ )
			if ( tpos[i] == tpos[j] ) return false;
	for (int i = 0; i < bR; i++ )
		if ( map[tpos[i].x][tpos[i].y] == '#' ) return false;
	return true;
}

void hashinsert(int d, int c)
{
	if ( d == 2 ) return;
	if ( !checkvalid() ) return;

	for (int i = 0; i < bR; i++ ) epos[i] = tpos[i];
	for (int i = bR - 1; i > 0; i-- )
		for (int j = 0; j < i; j++ )
			if ( epos[j + 1] < epos[j] ) swap( epos[j], epos[j + 1] );

	int hashp = 0;
	for (int i = 0; i < bR; i++ )
		hashp = ((hashp * R + epos[i].x) * C + epos[i].y) % bigprime;
	for (int i = 0; i < hashtable[hashp][0].size(); i++ )
	{
		bool ok = true;
		for (int k = 0; k < bR; k++ )
			if ( epos[k] != hashtable[hashp][k][i] ) ok = false;
		if ( ok ) return;
	}
	for (int k = 0; k < bR; k++ ) hashtable[hashp][k].push_back(epos[k]);
	for (int k = 0; k < bR; k++ ) Q[k].push_back(epos[k]);
	Dg[Q[0].size() - 1] = d; cost[Q[0].size() - 1] = c;
}

void move(pos &A, int k)
{
	A.x += dx[k];
	A.y += dy[k];
}

bool canmove( int i, int k )
{
	bool ret = true;
	move( tpos[i], k );
	if ( !checkvalid() ) ret = false;
	move( tpos[i], k^2 ); move( tpos[i], k^2 );
	if ( !checkvalid() ) ret = false;
	move( tpos[i], k );
	return ret;
}

void extend(int t)
{
	int danger = Dg[t];
	for (int i = 0; i < bR; i++ ) tpos[i] = Q[i][t];
	//cout << "here\n" << t << endl;
	//for (int i = 0; i < bR; i++ ) cout << tpos[i].x << " " << tpos[i].y << endl;
	//cout << indanger() << endl;
	for (int i = 0; i < bR; i++ )
		for (int j = 0; j < 4; j++ )
		if ( canmove(i,j) )
		{
			move(tpos[i],j);
			if ( !indanger() )
				hashinsert(0, cost[t] + 1);
			else
				hashinsert(danger+1, cost[t] + 1);
			move(tpos[i],j^2);
		}
}

bool equal(int f)
{
	for (int i = 0; i < bR; i++ )
		if ( Q[i][f] != cpos[i] ) return false;
	return true;
}

void bfs()
{
	for (int i = 0; i < bigprime; i++ )
		for (int j = 0; j < 5; j++ )
			hashtable[i][j].clear();
	for (int i = 0; i < 5; i++ ) Q[i].clear();
	for (int i = 0; i < bR; i++ ) Q[i].push_back(bpos[i]);
	Dg[0] = 0; cost[0] = 0;
	int f = -1;
	while ( ++f < Q[0].size() )
	{
		if ( equal(f) ){ ans = cost[f]; return; }
		extend(f);
	}
}

int main()
{
	freopen( "in.txt", "r", stdin );
	freopen( "out.txt", "w", stdout );
	int test_cases, casen = 0;
	for ( scanf( "%d", &test_cases ); test_cases > 0; test_cases -- )
	{
		scanf( "%d %d", &R, &C );
		for (int i = 0; i < R; i++ )
			scanf( "%s", map[i] );
		bR = 0; cR = 0;
		for (int i = 0; i < R; i++ )
			for (int j = 0; j < C; j++ )
			{
				if ( map[i][j] == 'o' || map[i][j] == 'w' )
					bpos[bR++] = (pos){i,j};
				if ( map[i][j] == 'x' || map[i][j] == 'w' )
					cpos[cR++] = (pos){i,j};
			}
		if ( bR != cR ) ans = -1;
		else {ans = -1; bfs(); }
		printf( "Case #%d: %d\n", ++casen, ans );
		//while (1);
	}
}
