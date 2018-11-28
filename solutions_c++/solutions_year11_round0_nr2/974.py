#pragma comment(linker, "/STACK:160777216")
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <queue>
#include <string>
#include <set>
#include <map>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <numeric>
#include <ctime>
#include <deque>
#include <climits>
#include <list>
using namespace std;

int nextInt() {
	int x;
	scanf("%d", &x);
	return x;
}

double nextDouble() {
	double x;
	scanf("%lf", &x);
	return x;
}

long long nextLong() {
	long long x;
	scanf("%lld", &x);
	return x;
}

char buf[1010111];
string nextString() {
	scanf("%s", buf);
	return buf;
}

string nextLine() {
	gets(buf);
	return buf;
}

int main() {
	freopen("B-large.in", "rt", stdin);
	freopen("b_large.out", "wt", stdout);
	int T = nextInt();
	for (int cas = 1; cas <= T; ++cas) {
		int c = nextInt();
		vector<vector<int> > r(256, vector<int>(256, -1));
		for (int i = 0; i < c; ++i) {
			string s = nextString();
			int x = s[0];
			int y = s[1];
			int z = s[2];
			r[x][y] = r[y][x] = z;
		}
		int d = nextInt();
		vector<vector<bool> > kill(256, vector<bool>(256, false));
		for (int i = 0; i < d; ++i) {
			string s = nextString();
			int x = s[0];
			int y = s[1];
			kill[x][y] = kill[y][x] = true;
		}
		int n = nextInt();
		string s = nextString();
		vector<int> res;
		for (int i = 0; i < s.size(); ++i) {
			int prev = res.size() == 0 ? -1 : res.back();
			int x = s[i];
			if (prev != -1 && r[prev][x] != -1) {
				res.pop_back();
				res.push_back(r[prev][x]);
			} else {
				bool killed = false;
				for (int i = 0; i < res.size(); ++i) {
					if (kill[res[i]][x]) {
						res.clear();
						killed = true;
						break;
					}
				}
				if (!killed) {
					res.push_back(x);
				}
			}
		}
		printf("Case #%d: [", cas, res);
		for (int i = 0; i < res.size(); ++i) {
			if (i > 0) {
				printf(", ");
			}
			printf("%c", res[i]);
		}
		printf("]\n");
		cerr << cas << " " << T << endl;
	}
	return 0;
}