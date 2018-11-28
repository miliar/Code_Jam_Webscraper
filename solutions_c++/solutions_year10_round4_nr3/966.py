#include <cstdio>
#include <cmath>
#include <iostream>

using namespace std;

typedef unsigned long long ull;
typedef long long ll;

void func();

int main() {
  freopen("in.in", "r", stdin);
  freopen("output.out", "w", stdout);

  int t;
  scanf("%d", &t);
  for (int i = 1; i <= t; i++) {
  	cout << "Case #" << i << ":";
  	func();
  }

  fclose(stdin);
  fclose(stdout);
}

bool b[110][110];
// WRITE ALL CODE BELOW THIS
void func() {
	int R;
	cin >> R;
	for (int i = 0; i <= 100; i++)
		for (int j = 0; j <= 100; j++)
			b[i][j] = false;
	for (int i = 0; i < R; i++) {
		int x1, y1, x2, y2;
		cin >> x1 >> y1 >> x2 >> y2;
		for (int j = x1; j <= x2; j++)
			for (int k = y1; k <= y2; k++)
				b[j][k] = true;
	}
	int c = 0;
	for (int i = 0; i <= 100; i++)
		for (int j = 0; j <= 100; j++)
			if (b[i][j])
				c++;
	int res = 0;
	while (c > 0) {
		res++;
		for (int i = 100; i > 0; i--)
			for (int j = 100; j > 0; j--) {
				if (b[i][j]) {
					if (!b[i-1][j] && !b[i][j-1]) {
						b[i][j] = false;
						c--;
					} else
						b[i][j] = true;
				} else {
					if (b[i-1][j] && b[i][j-1]) {
						b[i][j] = true;
						c++;
					} else
						b[i][j] = false;
				}
			}
	}
	cout << " " << res << endl;
}
