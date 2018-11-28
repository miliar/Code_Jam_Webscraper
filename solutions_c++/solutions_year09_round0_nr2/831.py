#include <cstdio>
#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <cstring>
#include <cstdlib>
#include <string>
#include <cassert>

typedef long long int64;
typedef double real;

const int inf = 0x3f3f3f3f;

#define Eo(x) { std::cerr << #x << " = " << x << std::endl; }
#define tname "counterexample"

using namespace std;

const int maxn = 502;
int a[maxn][maxn];
char res[maxn][maxn];

int used;
int h,w;

int dx[] = {0,-1,1,0};
int dy[] = {-1,0,0,1};

char dfs(int i, int j){
	if (res[i][j]) return res[i][j];
	int mn = inf;
	int ind = -1;
	for (int d = 0; d < 4; d++){
		int ax = j + dx[d];
		int ay = i + dy[d];
		if (ax < 0 || ay < 0 || ax >= w || ay >= h) continue;
		if (a[ay][ax] < mn){
			mn = a[ay][ax];
			ind = d;
		}
	}
	if (a[i][j] <= mn){
		res[i][j] = 'a' + used;
		used++;
		return res[i][j];
	}
	char r = dfs(i+dy[ind],j+dx[ind]);
	res[i][j] = r;
	return r;
}

int main(){
	int T; cin >> T;
	for (int _ = 0; _ < T; _++){
		cin >> h >> w;
		for (int i = 0; i < h; i++)
			for (int j = 0; j < w; j++)
				scanf("%d",&a[i][j]);

		memset(res,0,sizeof(res));
		used = 0;
		for (int i = 0; i < h; i++){
			for (int j = 0; j < w; j++) if (!res[i][j]){
				dfs(i,j);
			}
		}
		printf("Case #%d:\n",_+1);
		for (int i = 0; i < h; i++){
			for (int j = 0;j  < w; j++){
				printf("%c ",res[i][j]);
			}
			printf("\n");
		}
	}
	return 0;
}

