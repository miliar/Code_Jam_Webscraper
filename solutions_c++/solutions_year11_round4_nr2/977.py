#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

int a[20][20];
int n, m, d;
char ch;

int dis(int a, int b, int c){
	if (b % 2 == 1)
		return c - (a + b / 2);
	return 2 * c - (2 * a + b - 1);
}

bool inside(int x, int y, int z){
	if (x == 1 && y == 1)
		return 0;
	if (x == 1 && y == z)
		return 0;
	if (x == z && y == 1)
		return 0;
	if (x == z && y == z)
		return 0;
	return 1;
}

bool check(int x, int y, int z){
	int t1, t2;
	t1 = t2 = 0;
	for (int i = x; i < x + z; i++)
		for (int j = y; j < y + z; j++)
			if (inside(i - x + 1, j - y + 1, z)){
				t1 += a[i][j] * dis(x, z, i);
				t2 += a[i][j] * dis(y, z, j);
			}
	return t1 == 0 && t2 == 0;
}

void solve(){
	cin >> n >> m >> d;
	for (int i = 1; i <= n; i++)
		for (int j = 1; j <= m; j++){
			cin >> ch;
			a[i][j] = d + (int)ch - (int)'0';
		}

	int size = min(n, m);
	for (; size >= 3; size--)
		for (int i = 1; i <= n - size + 1; i++)
			for (int j = 1; j <= m - size + 1; j++)
				if (check(i, j, size)){
					cout << size << endl;
					return;
				}
	cout << "IMPOSSIBLE\n";
}

int main(){
	freopen("blade.in", "r", stdin);
	freopen("blade.out", "w", stdout);

	int t;
	cin >> t;
	for (int i = 1; i <= t; i++){
		printf("Case #%d: ", i);
		solve();
	}

	return 0;
}
