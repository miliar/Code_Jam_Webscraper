#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int hei, wid;
int board[102][102];
int table[102][102];
int cnt = 0;

int dr[] = { 1, 0, 0, -1 };
int dc[] = { 0, 1, -1, 0 };

inline bool valid(int r, int c)
{
	return r>=0 && c>=0 && r<hei && c<wid;
}

bool flow(int r, int c)
{
	int minv = board[r][c];
	int nr = -1, nc = -1;
	for ( int i=0 ; i<4 ; ++i )
	{
		int rr = r + dr[i];
		int cc = c + dc[i];
		if ( valid(rr, cc) && board[rr][cc] <= minv)
		{
			minv = board[rr][cc];
			nr = rr;
			nc = cc;
		}
	}

	if ( table[r][c] == 0 )
	{
		table[r][c] = cnt++;
	}
	if ( minv < board[r][c] )
	{
		if ( table[nr][nc] == 0 )
			flow(nr, nc);
		table[r][c] = table[nr][nc];
	}
	return true;
}

int main()
{
	int T;
	scanf("%d", &T);
	for ( int t=1 ; t<=T ; ++t )
	{
		scanf("%d %d", &hei, &wid);
		for ( int i=0 ; i<hei ; ++i )
		{
			for ( int j=0 ; j<wid ; ++j )
			{
				scanf("%d", &board[i][j]);
			}
		}

		cnt = 1;
		memset(table, 0, sizeof(table));
		for ( int i=0 ; i<hei ; ++i )
		{
			for ( int j=0 ; j<wid ; ++j )
			{
				flow(i, j);
			}
		}

		char mapping[cnt];
		memset(mapping, -1, sizeof(mapping));
		char basin = 'a';

		printf("Case #%d:\n", t);
		for ( int i=0 ; i<hei ; ++i )
		{
			for ( int j=0 ; j<wid ; ++j )
			{
				if ( mapping[table[i][j]] == -1 )
				{
					mapping[table[i][j]] = basin++;
				}
				printf("%c ", mapping[table[i][j]]);
			}
			puts("");
		}
	}
	return 0;
}
