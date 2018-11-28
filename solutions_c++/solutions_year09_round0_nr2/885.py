#include <iostream>
#include <cstdio>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <string>
#include <sstream>
#include <algorithm>
#include <stack>

#define INF 1000000000
#define EPS 1E-8
#define PI 3.14159265358979

using namespace std;

struct union_find {
	int* p;
	char* ch;
	union_find(int size) {
		p = new int[size];
		ch = new char[size];
		for(int i = 0; i < size; ++i) p[i] = i;
		for(int i = 0; i < size; ++i) ch[i] = 0;
	}
	void union_(int x, int y) {
		x = find(x); y = find(y);
		p[x] = y;
	}
	int find(int x) {
		if(x == p[x]) return x;
		return p[x] = find(p[x]);
	}
	char get_char(int x) {
		return ch[find(x)];
	}
	void set_char(int x, char c) {
		ch[find(x)] = c;
	}
};

int attr[200][2000];
int dir[4][2] = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};

int main() {
	int t, h, w;
	cin >> t;
	for(int o = 0; o < t; ++o) {
		printf("Case #%d:\n", o + 1);
		cin >> h >> w;
		for(int i = 0; i < h; ++i) {
			for(int j = 0; j < w; ++j) {
				cin >> attr[i][j];
			}
		}
		union_find uf(w * h);
		for(int i = 0; i < h; ++i) {
			for(int j = 0; j < w; ++j) {
				int mina = 10000, d = -1;
				for(int k = 0; k < 4; ++k) {
					int x = i + dir[k][0], y = j + dir[k][1];
					if(x < 0 || y < 0 || x >= h || y >= w || attr[x][y] >= attr[i][j]) continue;
					if(mina > attr[x][y]) {
						mina = attr[x][y];
						d = k;
					}
				}
				if(d == -1) continue;
				int x = i + dir[d][0], y = j + dir[d][1];
				uf.union_(i * w + j, x * w + y);
			}
		}
		int used[26] = {0};
		for(int i = 0; i < h; ++i) {
			for(int j = 0; j < w; ++j) {
				if(j) printf(" ");
				if(!uf.get_char(i * w + j)) {
					int u = 0;
					for(; u < 26 && used[u]; ++u);
					uf.set_char(i * w + j, u + 'a');
					if(u == 26) cerr << "error" << endl;
					used[u] = 1;
				}
				printf("%c", uf.get_char(i * w + j));
			}
			puts("");
		}
	}
	return 0;
}