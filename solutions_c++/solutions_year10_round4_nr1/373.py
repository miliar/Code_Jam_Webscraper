#include <cstdio>
#include <vector>
#include <utility>
#include <queue>
#include <set>
using namespace std;

const int MAXN=52;
const int SZ=2*MAXN-1;

char tab[SZ][SZ];
typedef pair<int, int> pii;

int delta[4][2] = {{0,1}, {0, -1}, {1, 0}, {-1, 0}};

int sym_axis_y(int n) {
	int sz = 2*n-1;
	for (int j=0; j<n; j++) {

		int i = n-1-j;
		bool ok = true;
		for (int y=0; y<i && ok; y++)
			for (int x=0; x<sz && ok; x++) {
				if (tab[y][x] != ' ' 
					&& 2*i-y < sz && tab[2*i-y][x] != ' '
					&& tab[y][x] != tab[2*i-y][x])
					ok = false;
			}
		if (ok)
			return j;

		i = n-1+j;
		ok = true;
		for (int y=0; y<i && ok; y++)
			for (int x=0; x<sz && ok; x++) {
				if (tab[y][x] != ' ' 
					&& 2*i-y < sz && tab[2*i-y][x] != ' '
					&& tab[y][x] != tab[2*i-y][x])
					ok = false;
			}
		if (ok)
			return j;
	}
}

int sym_axis_x(int n) {
	int sz = 2*n-1;
	for (int j=0; j<n; j++) {

		int i = n-1-j;
		bool ok = true;
		for (int x=0; x<i && ok; x++)
			for (int y=0; y<sz && ok; y++) {
				if (tab[y][x] != ' ' 
					&& 2*i-x < sz && tab[y][2*i-x] != ' '
					&& tab[y][x] != tab[y][2*i-x])
					ok = false;
			}
		if (ok)
			return j;

		i = n-1+j;
		ok = true;
		for (int x=0; x<i && ok; x++)
			for (int y=0; y<sz && ok; y++) {
				if (tab[y][x] != ' ' 
					&& 2*i-x < sz && tab[y][2*i-x] != ' '
					&& tab[y][x] != tab[y][2*i-x])
					ok = false;
			}
		if (ok)
			return j;
	}
}


int main() {
	int T;
	scanf("%d", &T);
	for (int t=1; t<=T; t++) {
		int n;
		scanf("%d", &n);
		while (getchar() != '\n');
		memset(tab, ' ', sizeof(tab));
		for (int i=0; i<2*n-1; i++)
			gets(tab[i]);

		/*
		queue<pii> q;
		vector<pii> v;
		set<pii> s;
		q.push(pii(0, 0));
		s.insert(pii(0, 0));
		v.push_back(pii(0, 0));
		while (!q.empty()) {
			pii x = q.front();
			q.pop();
			for (int i=0; i<4; i++) {
				int nx = x.first + delta[i][0],
					ny = x.second + delta[i][1];
				if (s.find(pii(nx, ny)) == s.end() && abs(nx)+abs(ny)<n) {
					q.push(pii(nx, ny));
					v.push_back(pii(nx, ny));
					s.insert(pii(nx, ny));
				}
			}
		}*/

		int shift = sym_axis_x(n) + sym_axis_y(n);
		printf("Case #%d: %d\n", t, (n+shift)*(n+shift) - n*n);
	}
	return 0;
}