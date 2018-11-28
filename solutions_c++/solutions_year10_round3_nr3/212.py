#include <numeric>
#include <fstream>
#include <iostream>
#include <algorithm>
#include <stack>
#include <queue>
#include <set>
#include <vector>
#include <map>
#include <cmath>
#include <iomanip>
#include <string>
#include <cctype>
#include <stdio.h>
#include <cstdlib>
#include <memory.h>

using namespace std;

ifstream in("input.txt");
ofstream out("output.txt");

const int N = 520;

struct square {
	int x, y, k;

	square() {
		x = 0; y = 0; k = 0;
	}

	square(int i, int j, int q) {
		x = i; y = j; k = q;
	}

	friend bool operator < (square a, square b) {
		bool f = false;
		if (a.k < b.k) f = true;
		if (a.k == b.k && a.x > b.x) f = true;
		if (a.k == b.k && a.x == b.x && a.y > b.y) f = true;
		return f;
	}
};


int t, n, m, x, kol;
int a[N][N], f[N][N], h[N][N], v[N][N];
int kk[N];
bool w[N][N];
char ch;
priority_queue<square> Q;

int main()            
{
	in >> t;
	for (int tt = 0; tt < t; ++tt) {
		in >> n >> m;
		for (int i = 0; i < n; ++i) {
			kol = 0;
			for (int j = 0; j < m / 4; ++j) {
				in >> ch;
				if (ch >= '0' && ch <= '9') x = ch - '0';
				else x = int(ch - 'A') + 10;
				for (int k = 0; k < 4; ++k) {
					a[i][kol + 3 - k] = x % 2;
					x /= 2;
				}
				kol += 4;
			}
		}

		memset(h, 0, sizeof(h));

		for (int i = 0; i < n; ++i) h[i][0] = 1;
		for (int i = 0; i < n; ++i) 
			for (int j = 1; j < m; ++j) {
				if (a[i][j - 1] == a[i][j]) h[i][j] = 1;
				else h[i][j] = h[i][j - 1] + 1;
			}

		memset(v, 0, sizeof(v));
		for (int i = 0; i < m; ++i) v[0][i] = 1;
		for (int i = 1; i < n; ++i)
			for (int j = 0; j < m; ++j) {
				if (a[i - 1][j] == a[i][j]) v[i][j] = 1;
				else v[i][j] = v[i - 1][j] + 1;
			}
		
		memset(f, 0, sizeof(f));
		for (int i = 0; i < n; ++i)
			for (int j = 0; j < m; ++j) {
				if ((i == 0 && j == 0) || a[i][j] != a[i - 1][j - 1]) f[i][j] = 1;
				else 
				if (a[i][j] == a[i - 1][j - 1]) 
					f[i][j] = min(min(f[i - 1][j - 1] + 1, h[i][j]), v[i][j]);
				square s(i, j, f[i][j]);
				Q.push(s);
			}

/*		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < m; ++j) 
				out << f[i][j] << " ";
			out << endl;
		}

*/
		memset(w, 0, sizeof(w));
		memset(kk, 0, sizeof(kk));
		kol = 0;
		while (!Q.empty()) {
			square s = Q.top();
			Q.pop();
			int rx = s.x, ry = s.y;
			int lx = s.x - s.k + 1, ly = s.y - s.k + 1;
			if (!w[lx][ly] && !w[rx][ry] && !w[lx][ry] && !w[rx][ly]) {
				for (int i = lx; i <= rx; ++i)
					for (int j = ly; j <= ry; ++j) w[i][j] = true;
				if (kk[s.k] == 0) kol++;
				kk[s.k]++;
			}
			else if (s.k > 1) {
				s.k--;
				Q.push(s);
			}
		}

		out << "Case #" << tt + 1 << ": " << kol << endl;
		for (int i = 512; i >= 1; --i)
			if (kk[i] != 0) out << i << " " << kk[i] << endl;
			
	}

	return 0;
}
