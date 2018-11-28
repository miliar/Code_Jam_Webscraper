#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <ctime>
#include <vector>
#include <string>
#include <map>
#include <algorithm>

using namespace std;

char ch[64][64];

int R, C;

void input() {
	scanf("%d%d", &R, &C);
	for(int i = 0;i < R;i ++) scanf("%s", ch[i]);
}

int valid(int i,int j) {
	if(i+1 >= R||j+1 >= C) return 0;
	if(ch[i][j+1] != '#'||ch[i+1][j] != '#'||ch[i+1][j+1] != '#') return 0;
	return 1;
}

void solve() {
	for(int i = 0;i < R;i ++) {
		for(int j = 0;j < C;j ++) if(ch[i][j] == '#') {
			if(valid(i, j)) {
				ch[i][j] = '/'; ch[i][j+1] = '\\';
				ch[i+1][j] = '\\'; ch[i+1][j+1] = '/';
			}
			else {
				printf("Impossible\n");
				return ;
			}
		}
	}
	for(int i = 0;i < R;i ++) printf("%s\n", ch[i]);
}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("output", "w", stdout);
	int T;
	scanf("%d", &T);
	for(int cas = 1;cas <= T;cas ++) {
		input();
		printf("Case #%d:\n", cas);
		solve();
	}
	return 0;
}
