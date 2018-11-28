#include <cstdio>
#include <cstring>

#include <algorithm>
#include <vector>

using namespace std;

int dx[4] = {-1, 0, 0, 1};
int dy[4] = {0, -1, 1, 0};

int n, m;
int data[105][105];
pair<int, int> next[105][105];
pair<int, int> order[10005];

int numLabel;
int label[105][105];
int labelOrder[10005];
int labelId[10005];
pair<int, int> am[10005];

bool cmpOrder( pair<int, int> u, pair<int, int> v )
{
	return data[u.first][u.second] < data[v.first][v.second];
}

bool cmpLabel( int u, int v )
{
	return am[u] < am[v];
}

int main( void )
{
//	freopen( "B.in", "r", stdin );

	int prob, nprob; scanf( "%d", &nprob );

	for( prob = 0; prob < nprob; ) {
		scanf( "%d %d", &n, &m );
		for( int i = 0; i < n; ++i )
			for( int j = 0; j < m; ++j )
				scanf( "%d", &data[i][j] );

		for( int i = 0; i < n; ++i )
			for( int j = 0; j < m; ++j ) {
				next[i][j] = make_pair(-1, -1);

				for( int k = 0; k < 4; ++k ) {
					int x = i + dx[k];
					int y = j + dy[k];

					if( x < 0 || y < 0 || x >= n || y >= m || data[x][y] >= data[i][j] ) continue;
					if( next[i][j].first < 0 || data[x][y] < data[next[i][j].first][next[i][j].second] ) next[i][j] = make_pair(x, y);
				}
			}

		int cnt = 0;
		for( int i = 0; i < n; ++i )
			for( int j = 0; j < m; ++j )
				order[cnt++] = make_pair(i, j);
		sort(order, order + cnt, cmpOrder);

		numLabel = 0;
		for( int i = 0; i < cnt; ++i ) {
			int j = order[i].first;
			int k = order[i].second;

			if( next[j][k].first < 0 ) {
				next[j][k] = order[i];
				label[j][k] = numLabel;
				am[numLabel++] = order[i];
			} else {
				next[j][k] = next[next[j][k].first][next[j][k].second];
				label[j][k] = label[next[j][k].first][next[j][k].second];
				if( order[i] < am[label[j][k]] ) am[label[j][k]] = order[i];
			}
		}

		for( int i = 0; i < numLabel; ++i ) {
			labelOrder[i] = i;
//			printf( "am[i] = (%d, %d)\n", am[i].first, am[i].second );
		}
		sort(labelOrder, labelOrder + numLabel, cmpLabel);
		for( int i = 0; i < numLabel; ++i ) labelId[labelOrder[i]] = i;

		printf( "Case #%d:\n", ++prob );
		for( int i = 0; i < n; ++i ) {
			for( int j = 0; j < m; ++j ) {
				if( j ) putchar( ' ' );
				putchar( labelId[label[i][j]] + 'a' );
			}
			putchar( '\n' );
		}
	}

	return 0;
}

