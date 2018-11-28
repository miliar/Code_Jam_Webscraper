#include <cstdio>
#include <cstring>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#define REP(i,n) for (int i = 0; i < (n); ++i)
#define FORE(i,c) for (typeof(c.begin()) i = c.begin(); i != c.end(); ++i)
using namespace std;

int T;
int N, K;
char grid[500][500], data[500][500];
char P[] = {'R', 'B'};

bool win(int p)
{
	// horizontal
	REP(i, N) REP(j, N) if (j+K-1 < N)
	{
		bool valid = true;
		REP(k, K) if (data[i][j+k] != P[p])
			valid = false;
		if (valid) return true;
	}
	
	// vertical
	REP(i, N) REP(j, N) if (i+K-1 < N)
	{
		bool valid = true;
		REP(k, K) if (data[i+k][j] != P[p])
			valid = false;
		if (valid) return true;
	}
	
	// diag1
	REP(i, N) REP(j, N) if (i+K-1 < N && j+K-1 < N)
	{
		bool valid = true;
		REP(k, K) if (data[i+k][j+k] != P[p])
			valid = false;
		if (valid) return true;
	}
	
	// diag2
	REP(i, N) REP(j, N) if (i+K-1 < N && j-K+1 >=0)
	{
		bool valid = true;
		REP(k, K) if (data[i+k][j-k] != P[p])
			valid = false;
		if (valid) return true;
	}
	return false;
}

int main()
{
	//freopen("A-small-attempt0.in", "r", stdin), freopen("A-small.out", "w", stdout);
	freopen("A-large.in", "r", stdin), freopen("A-large.out", "w", stdout);
	scanf("%d", &T);
	REP(t, T)
	{
		scanf("%d%d", &N, &K);
		REP(i, N)
			scanf("%s", grid[i]);
		REP(i, N) REP(j, N)
			data[j][N-i-1] = grid[i][j];
		REP(j, N) REP(i, N)
		{
			int x = N-i-1;
			while (x < N && data[x+1][j] == '.')
			{
				swap(data[x][j], data[x+1][j]);
				x++;
			}
		}
		//printf("\n");
		//REP(i, N) printf("%s\n", data[i]);
		
		int res = 0;
		REP(p, 2) if (win(p))
			res |= 1<<p;
		
		printf("Case #%d: ", t+1);
		if (res ==0) puts("Neither");
		else if (res == 1) puts("Red");
		else if (res == 2) puts("Blue");
		else puts("Both");
	}
}
