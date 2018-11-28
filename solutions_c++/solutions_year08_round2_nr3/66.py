#include <iostream>
using namespace std;

#define N 1000005
#define K 2097152
int a[N], b[105];

int T, t, i, j, k, n, m, x, y, r;

class sum {
public:
	int a[K+K];
	void set(int x, int dx) {
		int t;
		x += K;
		a[x] = dx;
		x >>= 1;
		while (x > 0) {
			t = a[x+x] + a[x+x+1];
			a[x] = t;
			x >>= 1;
		}
	}
	void init() {
		int i;
		for (i = K; i < K + K; i ++) {
			a[i] = 1;
		}
		for (i = K - 1; i > 0; i --) {
			a[i] = a[i+i] + a[i+i+1];
		}
	}
	int get(int x, int y) {
		int r = 0;
		x += K;
		y += K;
		while (x < y) {
			if (x % 2 == 1) {
				r += a[x];
				x ++;
			} else if (y % 2 == 0) {
				r += a[y];
				y --;
			} else {
				x >>= 1;
				y >>= 1;
			}
		}
		r += a[x];
		return r;
	}
	int move(int x, int dx) {
		int y;
		int s;
		s = get(0, x);
		dx = dx + s;
		y = 1;
		s = dx;
		while (y < K) {
			if (a[y+y] < s) {
				s -= a[y+y];
				y = y + y + 1;
			} else {
				y = y + y;
			}
		}
		return y - K;
	}
};

sum s;






int main() {
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	cin >> T;
	for (t =1; t <= T; t ++) {
		cin >> n >> m;
		for (i = 0; i < m; i++) {
			cin >> b[i];
		}

		memset(a, 0, sizeof(a));
		memset(a, 0, sizeof(b));
		a[0] = 1;
		i = 0;
		j = 2;
		k = 0;
		s.init();
		s.set(0, 0);
		s.set(n, 0);
		
		while (j <= n) {
			r = n - j + 1;
			x = j % r;
			if (x == 0) {
				x = r;
			}
			y = s.move(i, x) % n;
			a[y] = j;
			i = y;
			s.set(y, 0);
			s.set(y + n, 0);
			j ++;
		}

/*
		while (j <= n) {
			i = (i + 1) % n;
			if (a[i] == 0) {
				k ++;
			}
			if (k == j) {
				a[i] = j;
				k = 0;
				j ++;
			}
		}
*/
		cout << "Case #" << t << ": ";
		for (i = 0; i < m; i ++) {
			cout << a[b[i]-1] << ' ';
		}
		cout << endl;
	}
	return 0;
}


