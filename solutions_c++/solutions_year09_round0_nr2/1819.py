#include <stdio.h>
#include <string>
#include <vector>
#include <iostream>
#include <string.h>
#include <queue>
#include <cassert>
#include <map>
#define Eo(x) { cerr << #x << " = " << x << endl;}
#define inf 0x3f3f3f3f
using namespace std;
int n,m;
int d[4][2] = {{-1,0},{0, -1},{0,1},{1,0}};
inline bool onb( int x, int y){
	return (x >= 0 && y >= 0 && x < m && y < n);
}

int a[3000][3000];
int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int _;
	cin >> _;
	for ( int t0 = 0; t0 < _; t0++){
		cin >> m >> n;
		vector<pair<int,int> > next[m][n];
		bool notsink[m][n];
		memset(notsink,0,sizeof(notsink));

		char mark[m][n];
		memset(mark,0,sizeof(mark));
		for ( int i = 0; i < m; i++)
			for ( int j = 0; j < n; j++)
				cin >> a[i][j];
		for ( int i = 0; i < m; i++)
			for ( int j = 0; j < n; j++){
				int minl = a[i][j];
				int sx = -1;
				int sy = -1;
				for ( int t = 0; t < 4; t++){
					int x = i + d[t][0];
					int y = j + d[t][1];
					if ( onb(x, y) && a[x][y] < minl){
						sx = x;
						sy = y;
						minl = a[x][y];
					}
				}
				if ( sx != -1){
					next[sx][sy].push_back(make_pair(i,j));
					notsink[i][j] = true;
				}

			}
		char a = 'a';
		for ( int i = 0; i < m; i++)
			for ( int j = 0; j < n; j++)
				if (!notsink[i][j]){
					assert (!mark[i][j]);
					queue< pair < int, int > > q;
					q.push(make_pair(i,j));
					while (!q.empty()){
						pair <int, int > curr = q.front();
						q.pop();
						int x = curr.first;
						int y = curr.second;
						if (mark[x][y]) continue;
						mark[x][y] = a;
						for ( int t = 0 ; t < next[x][y].size(); t++)
							q.push(next[x][y][t]);
					}
					a++;
				}
	map <char, char> zz;
	char ww = 'a';
	cout << "Case #" << t0 +1 << ":" << endl;
		for ( int i = 0; i < m; i++){
			for ( int j = 0; j < n - 1; j++){
				if (zz.find(mark[i][j]) == zz.end())
					zz[mark[i][j]] = ww++;
				cout << zz[mark[i][j]] << " ";
			}
			if (zz.find(mark[i][n - 1]) == zz.end())
				zz[mark[i][n - 1]] = ww++;
			cout << zz[mark[i][n - 1]] << endl;
		}


	}

	return 0;
}
