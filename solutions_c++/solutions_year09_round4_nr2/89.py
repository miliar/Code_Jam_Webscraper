#include <vector>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cassert>
#include <string>
#include <cstdio>
#include <cmath>
#include <stack>
#define sz(x) ((int)(x.size()))
#define all(c) (c).begin(),(c).end() 
#define pb push_back 
#define mp make_pair
#define foreach(T, x, it) for (T::iterator it = x.begin(); it != x.end(); ++it)
using namespace std;
typedef long long lint;
typedef pair<int, int> pii;
typedef vector<int> vi;

struct Item {
	int i, j, use, nuse, key;
	Item(int i = 0, int j = 0, int use = 0, int nuse = 0, int key = 0) : 
		i(i), j(j), use(use), nuse(nuse), key(key) {}
};

bool operator <(const Item &a, const Item &b) {
	return a.key > b.key;
}

int R, C, F;
char S[100][100];
int Mark[60][60][1 << 6][1 << 6];
int D[60][60][1 << 6][1 << 6];

int Calc(int i, int j) {
	while (i < R && S[i][j] == '.') ++i;	
	return i - 1;
}

bool Test(int x, int p) { return (x >> p) & 1; }

void Solve(int num) {
	cin >> R >> C >> F;
	for (int i = 0; i < R; ++i) {
		scanf("%s", S[i]);
	}

	for (int i = 0; i < R; ++i) {
		for (int j = 0; j < C; ++j) {
			for (int k = 0; k < 1 << C; ++k) {
				for (int d = 0; d < 1 << C; ++d) {
					D[i][j][k][d] = 1 << 30;
				}
			}
		}
	}
	
	priority_queue<Item> q;
	q.push(Item(0, 0, 0, 0, 0));
	D[0][0][0][0] = 0;

	while (!q.empty()) {
		Item f = q.top();
		q.pop();

		if (f.i == R - 1) {
			printf("Case #%d: Yes %d\n", num, f.key);
			return;
		}
		int i = f.i, j = f.j, use = f.use, nuse = f.nuse;
		if (Mark[f.i][f.j][use][nuse] == num) continue;
		Mark[f.i][f.j][use][nuse] = num;
		

		if (j > 0 && (S[i][j - 1] == '.' || Test(use, j - 1))) {
			if (S[i + 1][j - 1] == '.' || Test(nuse, j - 1)) {
				int ni = Calc(i + 2, j - 1);
				if (ni - i == 1) {
					if (ni - i <= F && Mark[ni][j - 1][nuse][0] != num && D[ni][j - 1][nuse][0] > D[i][j][use][nuse]) {
						D[ni][j - 1][nuse][0] = D[i][j][use][nuse];
						q.push(Item(ni, j - 1, nuse, 0, D[ni][j - 1][nuse][0]));
					}
				}
				else {
					if (ni - i <= F && Mark[ni][j - 1][0][0] != num && D[ni][j - 1][0][0] > D[i][j][use][nuse]) {
						D[ni][j - 1][0][0] = D[i][j][use][nuse];
						q.push(Item(ni, j - 1, 0, 0, D[ni][j - 1][0][0]));
					}
				}
				
			}
			else {
				if (Mark[i][j - 1][use][nuse] != num && D[i][j - 1][use][nuse] > D[i][j][use][nuse]) {
					D[i][j - 1][use][nuse] = D[i][j][use][nuse];
					q.push(Item(i, j - 1, use, nuse, D[i][j - 1][use][nuse]));
				}
			}
		}

		if (j + 1 < C && (S[i][j + 1] == '.' || Test(use, j + 1))) {
			if (S[i + 1][j + 1] == '.' || Test(nuse, j + 1)) {
				int ni = Calc(i + 2, j + 1);
				if (ni - i == 1) {
					if (ni - i <= F && Mark[ni][j + 1][nuse][0] != num && D[ni][j + 1][nuse][0] > D[i][j][use][nuse]) {
						D[ni][j + 1][nuse][0] = D[i][j][use][nuse];
						q.push(Item(ni, j + 1, nuse, 0, D[ni][j + 1][nuse][0]));
					}
				} 
				else {
					if (ni - i <= F && Mark[ni][j + 1][0][0] != num && D[ni][j + 1][0][0] > D[i][j][use][nuse]) {
						D[ni][j + 1][0][0] = D[i][j][use][nuse];
						q.push(Item(ni, j + 1, 0, 0, D[ni][j + 1][0][0]));
					}
				}
			}
			else {
				if (Mark[i][j + 1][use][nuse] != num && D[i][j + 1][use][nuse] > D[i][j][use][nuse]) {
					D[i][j + 1][use][nuse] = D[i][j][use][nuse];
					q.push(Item(i, j + 1, use, nuse, D[i][j + 1][use][nuse]));
				}
			}
		}

		
		if (j > 0 && (S[i][j - 1] == '.' || Test(use, j - 1)) && S[i + 1][j - 1] == '#' && !Test(nuse, j - 1)) {
			
			if (Mark[i][j][use][nuse | (1 << (j - 1))] != num && D[i][j][use][nuse | (1 << (j - 1))] > D[i][j][use][nuse] + 1) {
				D[i][j][use][nuse | (1 << (j - 1))] = D[i][j][use][nuse] + 1;
				q.push(Item(i, j, use, nuse | (1 << (j - 1)), D[i][j][use][nuse | (1 << (j - 1))]));
			}
		}


		if (j + 1 < C && (S[i][j + 1] == '.' || Test(use, j + 1)) && S[i + 1][j + 1] == '#' && !Test(nuse, j + 1)) {
			
			if (Mark[i][j][use][nuse | (1 << (j + 1))] != num && D[i][j][use][nuse | (1 << (j + 1))] > D[i][j][use][nuse] + 1) {
				D[i][j][use][nuse | (1 << (j + 1))] = D[i][j][use][nuse] + 1;
				q.push(Item(i, j, use, nuse | (1 << (j + 1)), D[i][j][use][nuse | (1 << (j + 1))]));
			}
		}


	}


	printf("Case #%d: No\n", num);


}


int main() {	
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int tst;
	cin >> tst;
	for (int i = 1; i <= tst; ++i) Solve(i);
	return 0;
}

