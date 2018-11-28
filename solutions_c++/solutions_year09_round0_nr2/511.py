#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <map>
#include <set>

using namespace std;

#define mp make_pair
#define pb push_back
#define sz(c) (int)((c).size())
#define f first
#define s second

#define fin  "B.IN"
#define fout "B.OUT"

#define NMAX 102

int dx[] = { -1,  0, 0, 1};
int dy[] = {  0, -1, 1, 0};

int T, N, M;
int mapA[NMAX][NMAX];

char id, label[NMAX][NMAX];

char df(int x,int y)
{
	int i, rx, ry, newX, newY, nextV = 10011;

	for ( i = 0; i < 4; ++i )
	{
		newX = x + dx[i];
		newY = y + dy[i];

		if ( newX < 1 || newY < 1 || newX > N || newY > M )
			continue;

		if ( mapA[newX][newY] < nextV )
			nextV = mapA[newX][newY], rx = newX, ry = newY;
	}

	if ( nextV >= mapA[x][y] )
	{
		if ( label[ x ][ y ] == 0 )
			label[ x ][ y ] = ++id;
	}
	else
		label[ x ][ y ] = df(rx,ry);

	return label[ x ][ y ];
}

int main()
{
	int t, i, j;

	ifstream f1(fin);
	ofstream f2(fout);

	f1 >> T;

	for ( t = 1; t <= T; ++t )
	{
		f1 >> N >> M;

		id = 'a' - 1;
		for ( i = 1; i <= N; ++i )
		for ( j = 1; j <= M; ++j )
			f1 >> mapA[i][j], label[i][j] = 0;

		for ( i = 1; i <= N; ++i )
		for ( j = 1; j <= M; ++j )
			if ( !label[i][j] )
			{
				df(i,j);
			}

		f2 << "Case #" << t << ":\n";

		for ( i = 1; i <= N; ++i )
		{
			for ( j = 1; j < M; ++j )
				f2 << label[i][j] << " ";
			f2 << label[i][M] << "\n";
		}
	}

	return 0;
}