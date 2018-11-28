#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cassert>
#include <vector>

using namespace std;

int R, C;
const int maxn = 50;
char G[maxn+5][maxn+5];

bool cmp(int a, int b){
	return a<b;
}

bool Change(int y, int x){
	if( x+1 == C || y+1 == R || G[y][x+1] != '#' ||
			G[y+1][x] != '#' || G[y+1][x+1] != '#' )
		return false;

	G[y][x] = '/'; G[y][x+1] = '\\';
	G[y+1][x] = '\\'; G[y+1][x+1] = '/';
	return true;
}

void Solve()
{
	for( int i = 0; i < R; i++ ){
		for( int j = 0; j < C; j++ ){
			if( G[i][j] == '#' ){
				if( !Change(i,j) ) {
					cout << "Impossible" << endl;
					return;
				}
			}
		}
	}
	for( int i = 0; i < R; i++ )
		cout << G[i] << endl;
}

int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);

	int T;
	cin >> T;
	for( int i = 1; i <= T; i++ ){
		cin >> R >> C;
		memset(G, 0, sizeof(G));
		for( int j = 0; j < R; j++ ){
			cin >> G[j];
		}

		cout << "Case #" << i << ":" << endl;
		Solve();
	}

	return 0;
}
