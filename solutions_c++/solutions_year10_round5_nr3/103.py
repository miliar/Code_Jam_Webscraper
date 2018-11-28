#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>

#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>
#include <utility>

using namespace std;

#define abs(x) ((x) < 0 ? (-(x)) : (x))
#define min(x, y) ((x) < (y) ? (x) : (y))
#define max(x, y) ((x) > (y) ? (x) : (y))

#define mp make_pair
#define pb push_back

typedef long long i64;

const int M = 10000000;
int p[M];
int q[M];
i64 b[100000];
int w[M];
int u[M];

int main() {
/*	int n = 10;
	int result = 0;
	memset(p, 0, sizeof(p));
	p[1000000] = 1;
	b[0] = 0;
	for (n = 1; n <= 100; ++n) {
	result = 0;
	bool f = true;
	int l = 100000000, r = -1;
	while (f) {
		f = false;
		for (int i = 0; i < 10000000; ++i) {
			q[i] = p[i];
		}
		l = 100000000, r = -1;
		for (int i = 1; i < 10000000 - 1; ++i) {
			if (p[i] > 1) {
				f = true;
				q[i - 1] += p[i] / 2;
				q[i + 1] += p[i] / 2;
				result += p[i] / 2;
				q[i] -= (p[i] & ~1);
			}
		}
		for (int i = 0; i < 10000000; ++i) {
			p[i] = q[i];
			if (p[i]) l = min(l, i), r = max(r, i);
			
		}
	}
	b[n] = result + (n / 2) + b[n / 2] * 2;
//	cout << n << " " << b[n] << " " << b[n] - b[n - 1] << " " << result << " " << result % (n) << " " << result / (n) << endl;
	memset(p, 0, sizeof(p));
	for (int i = -((n + 1) / 4); i <= (n + 1) / 4; ++i) {
		if (!i && (((n + 1) / 2) & 1)) p[1000000 + i] = 1;
		else if (i) {
			p[1000000 + i] = 1;
		}
	}
	for (int i = ((n + 1) / 4); i >= -((n + 1) / 4); --i) {
		p[1000000 + i + 2] += p[1000000 + i];
	}
	}
	return 0;*/
	

	b[0] = 0;
	b[1] = 0;
	for (int i = 2; i <= 1000; ++i) {
		if (!(i & 1)) b[i] = b[i - 1] + (i / 2) * (i64)(i / 2);
		else b[i] = b[i - 1];
	}
	
	int T; scanf("%d", &T);
	for (int tt = 0; tt < T; ++tt) {
		int n; scanf("%d", &n);
		map<int, int> p, q;
//		memset(p, 0, sizeof(p));
/*		int l = 1000000000, r = -1;*/
		int h = 0, t = 0;
		for (int i = 0; i < n; ++i) {
			int a, b;
			scanf("%d %d", &a, &b);
			a += 1000000;
			p[a] = b;
/*			if (a < l) l = a;
			if (a > r) r = a;*/
		}
		bool f = true;
		i64 result = 0;
		int k = 0;
/*			for (int i = -10; i <= 10; ++i) {
				cout << p[1000000 + i] << " ";
			}
			cout << endl;*/

		while (f) {
			f = false;
			q = p;
			for (map<int, int>::iterator it = p.begin(); it != p.end(); ++it) {
				int i = it->first;
				int x = it->second;
				if (x > 1) {
					f = true;
					result += b[x];
					q[i] -= x;
					for (int j = -(x / 2); j <= (x / 2); ++j) {
						if (j || (x & 1)) {
							if (q.find(i + j) == q.end()) q[i + j] = 0;
							q[i + j] += 1;
						}
					}
				}
			}
			p = q;
			++k;
		}
		printf("Case #%d: %lld\n", tt + 1, result);
		fflush(stdout);
	}
	return 0;
}
