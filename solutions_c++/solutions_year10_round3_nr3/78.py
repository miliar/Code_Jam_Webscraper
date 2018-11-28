#include <iostream>
#include <cmath>
#include <vector>
#include <string>
#include <cstring>
#include <algorithm>
#include <memory.h>
#include <set>
#include <map>
#include <cstdio>
using namespace std;
#define pb push_back
#define all(c) c.begin(), c.end()
typedef long long int64;

struct Point
{
	int x;
	int y;
	Point(int x_, int y_): x(x_), y(y_)
	{ }
};

template<class T> T sqr(const T& t) {return t * t;}
template<class T> T abs(const T& t) {return ((t > 0) ? (t) : (-t));}

void initialize()
{
    freopen("large.in", "r", stdin);
    freopen("_.out", "w", stdout);
}

int readHex(char c) {
	if (c >= '0' && c <= '9') return c - '0';
	return 10 + c - 'A';
}

const int MAX = 500 + 20;
int table[MAX][MAX];

int hash[MAX][MAX];
int goodHash[MAX][MAX];
int mnA = 1927;
int mnB = 2371;
int degA[MAX];
int degB[MAX];

int color(int x, int y) {
	if (table[x][y] == -1) return -1;
	return (x + y + table[x][y]) % 2;
}


int main()
{
    initialize();


	char str[1000];
	int T;
	cin >> T;
	for (int tt = 1; tt <= T; ++tt) {
		map<int, int> res;
		int n, m;
		cin >> n >> m;
		for (int i = 0; i < n; ++i) {
			scanf("%s", str);
			for (int j = 0; j < m / 4; ++j) {
				int num = readHex(str[j]);
				for (int k = 0; k < 4; ++k) {
					table[i][j * 4 + k] = (num & (1 << (3 - k))) ? 1 : 0;
				}
			}
		}

		//for (int k = min(n,m); k >= 1; --k) {
		//	for (int i = 0; i < n - k + 1; ++i) {
		//		for (int j = 0; j < m - k + 1; ++j) {
		//			bool ok = true;
		//			if (color(i,j) == -1) continue;
		//			for (int i1 = i; i1 < i + k; ++i1) {
		//				for (int j1 = j; j1 < j + k; ++j1) {
		//					if (color(i, j) != color(i1, j1)) ok = false;
		//				}
		//			}
		//			if (ok) {
		//				res[k]++;
		//				for (int i1 = i; i1 < i + k; ++i1) {
		//					for (int j1 = j; j1 < j + k; ++j1) {
		//						table[i1][j1] = -1;
		//					}
		//				}
		//			}
		//		}
		//	}
		//}


		degA[0] = degB[0] = 1;
		for (int i = 1; i < MAX; ++i) {
			degA[i] = degA[i - 1] * mnA;
			degB[i] = degB[i - 1] * mnB;
		}
		for (int i = 1; i <= n; ++i) {
			for (int j = 1; j <= m; ++j) {
				goodHash[i][j] = goodHash[i - 1][j] * mnA + goodHash[i][j - 1] * mnB - goodHash[i - 1][j - 1] * mnA * mnB + 1;
			}
		}

		//int px = 0, py = 0;
		for (int k = min(n, m); k >= 1;) {
			//cerr << "k = " << k << endl;
			bool ok = false;
			for (int i = 1; i <= n; ++i) {
				for (int j = 1; j <= m; ++j) {
					hash[i][j] = hash[i - 1][j] * mnA + hash[i][j - 1] * mnB - hash[i - 1][j - 1] * mnA * mnB + color(i - 1, j - 1);
				}
			}
			for (int i = 0; i <= n - k && !ok; ++i) {
				for (int j = 0; j <= m - k; ++j) {
					int val = hash[i + k][j + k] - degA[k] * hash[i][j + k] - degB[k] * hash[i + k][j] + degA[k] * degB[k] * hash[i][j];
					if (val == goodHash[k][k] || val == 0) {
						ok = true;
						res[k]++;
						for (int i1 = i; i1 < i + k; ++i1) {
							for (int j1 = j; j1 < j + k; ++j1) {
								table[i1][j1] = -1;
							}
						}
						j += k - 1;
						//break;
					}
				}
			}
			if (!ok) {
				k--;
			}
		}
	
		//for (int i = 0; i < n; ++i) {
		//	for (int j = 0; j < m; ++j) {
		//		int c = color(i, j);
		//		if (c == -1) continue;
		//		int shift = 0;
		//		for (int k = 1; k < min(n - i, m - j); ++k) {
		//			bool ok = true;
		//			for (int l = 0; l <= k && ok; ++l) {
		//				if (color(i + k, j + l) != c || color(i + l, j + k) != c) ok = false;
		//			}
		//			if (!ok) {
		//				shift = k;
		//				break;
		//			}
		//		}
		//		res[shift]++;
		//		for (int k = 0; k < shift; ++k) {
		//			for (int l = 0; l < shift; ++l) {
		//				table[i + k][j + l] = -1;
		//			}
		//		}
		//	}
		//}
		printf("Case #%d: %d\n", tt, res.size());
		map<int, int>::reverse_iterator it = res.rbegin(), jt = res.rend();
		for (; it != jt; ++it) {
			printf("%d %d\n", it->first, it->second);
		}
	}

    return 0;
}