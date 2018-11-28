#include <stdio.h>
#include <iostream>
#include <string.h>
#include <string>
#include <map>
#include <vector>
using namespace std;

int N;
int H;
int W;
int w[105][105];
char f[105][105];

int base = 10005;
vector<pair<int, int> > v[10005];
map<pair<int, int>, char> h;
map<pair<int, int>, pair<int, int> > root;

int dx[] = {-1, 0, 0, 1};
int dy[] = {0, -1, 1, 0};

pair<int, int> go(int x, int y){
	if( root.count(pair<int, int>(x, y) ) != 0)
		return root[pair<int, int>(x, y)];
	int l = -1;
	for(int i = 0; i < 4; i++){
		int nx = x + dx[i];
		int ny = y + dy[i];
		if( nx >= 0 && nx < H && ny >= 0 && ny < W){
			if( (l == -1 && w[x][y] > w[nx][ny])
			|| (l != -1 && w[x + dx[l]][y + dy[l]] > w[nx][ny])){
				l = i;
			}
		}
	}
	if( l != -1){
		return root[pair<int, int>(x, y)] = go(x + dx[l], y + dy[l]);
	}else{
		root[pair<int, int>(x, y)] = pair<int, int>(x, y);
	}
}

int main(){
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &N);
	for(int t = 0; t < N; t++){
		scanf("%d %d", &H, &W);
		int maxAlt = 0;
		for(int i = 0; i < H; i++){
			for(int j = 0; j < W; j++){
				scanf("%d", &w[i][j]);
				v[w[i][j]].push_back(pair<int, int>(i, j));
				maxAlt = max(maxAlt, w[i][j]);
			}
		}
		root.clear();
		int cur = 0;
		for(int i = maxAlt; i >= 0; i--){
			for(vector<pair<int, int> >::iterator it = v[i].begin(); it != v[i].end(); it++){
				if( root.count(*it) == 0){
					go(it->first, it->second);
				}
			}
		}
		h.clear();
		char c = 'a';
		printf("Case #%d:\n", t + 1);
		for(int i = 0; i < H; i++){
			for(int j = 0; j < W; j++){
				pair<int, int> r = root[pair<int, int> (i, j)];
				if( h.count(r) == 0){
					h[r] = (c++);
				}
				f[i][j] = h[r];
				if( j < W - 1)
					printf("%c ", f[i][j]);
				else
					printf("%c\n", f[i][j]);
			}
		}
	}
}