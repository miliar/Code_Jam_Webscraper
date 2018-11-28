/* kaneko-A.cc
 */
#include <iostream>
#include <string>
#include <cstdio>
#include <cassert>
using namespace std;

int T, M, N, noseet[11];
string room[10];
int cache[1024][10];

int dfs(int row, int filled);
void seat(int n, int filled, int next_filled, int&f2, int&nf2)
{
    int w = 0;
    if (n) w |= 1<<(n-1);
    if (n+1<N) w |= 1<<(n+1);
    f2 |= w;
    f2 |= 1<<n;
    nf2 |= w;
}
int dfs_col(int row, int filled, int col, int next_filled)
{
    if (col == N) {
	if (row+1 == M) return 0;
	return dfs(row+1, next_filled);
    }
    int m = dfs_col(row, filled, col+1, next_filled);
    for (int i=col; i<N; ++i) {
	if (filled & (1<<i)) continue;
	int f2 = filled, nf2 = next_filled;
	seat(i, filled, next_filled, f2, nf2);
	int s = 1+dfs_col(row, f2, i+1, nf2);
	if (s > m) m = s;
    }
    return m;
}
int dfs(int row, int filled)
{
    if (cache[filled][row] >= 0) return cache[filled][row];
    int next_filled = noseet[row+1];
    return (cache[filled][row] = dfs_col(row, filled, 0, next_filled));
}
int main()
{
    cin >> T;
    for (int t=0; t<T; ++t) {
	cin >> M >> N;
	for (int i=0; i<M; ++i) {
	    cin >> room[i];
	    noseet[i] = 0;
	    for (int j=0; j<N; ++j)
		if (room[i][j] == 'x') noseet[i] |= 1<<j;
	}
	noseet[M] = 0;
	
	fill(&cache[0][0], &cache[1023][9]+1, -1);
	int ret = dfs(0, noseet[0]);
	printf("Case #%d: %d\n", t+1, ret);
    }
}


