#define _CRT_SECURE_NO_WARNINGS
#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <vector>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <numeric>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <ctime>
using namespace std;

typedef long long int64;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<double> vd;
typedef pair<int,int> pii;

#define For(i,a,b) for (int i(a),_b(b); i <= _b; ++i)
#define Ford(i,a,b) for (int i(a),_b(b); i >= _b; --i)
#define Rep(i,n) for (int i(0),_n(n); i < _n; ++i)
#define Repd(i,n) for (int i((n)-1); i >= 0; --i)
#define Fill(a,c) memset(&a, c, sizeof(a))
#define MP(x, y) make_pair((x), (y))
#define All(v) (v).begin(), (v).end()

template<typename T, typename S> T cast(S s) {
	stringstream ss;
	ss << s;
	T res;
	ss >> res;
	return res;
}

template<typename T> inline T sqr(T a) { return a*a; }
template<typename T> inline int Size(const T& c) { return (int)c.size(); }
template<typename T> inline void checkMin(T& a, T b) { if (b < a) a = b; }
template<typename T> inline void checkMax(T& a, T b) { if (b > a) a = b; }

int n, m;
int state[2000];
vi all[2000];
vi unmalted[2000];
int malted[2000];
int cnt[2000];

int main() {
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int numTests;
	scanf("%d", &numTests);
	For(test, 1, numTests) {
		scanf("%d%d", &n, &m);
		Rep(i, n) {
			all[i].clear();
			state[i] = 0;
		}
		queue<int> que;
		Rep(i, m) {
			unmalted[i].clear();
			malted[i] = -1;
			int t;
			scanf("%d", &t);
			while (t --> 0) {
				int x, y;
				scanf("%d%d", &x, &y);
				--x;
				if (y == 1)
					malted[i] = x;
				else 
					unmalted[i].push_back(x);
			}
			cnt[i] = Size(unmalted[i]);
			Rep(j, Size(unmalted[i]))
				all[unmalted[i][j]].push_back(i);
			if (cnt[i] == 0)
				que.push(i);
		}
		while (!que.empty()) {
			int x = que.front();
			que.pop();
			if (malted[x] == -1)
				continue;
			state[malted[x]] = 1;
			Rep(i, Size(all[malted[x]])) {
				int y = all[malted[x]][i];
				//assert(cnt[y] > 0);
				--cnt[y];
				if (cnt[y] == 0) 
					que.push(y);
			}
		}
		bool ok = true;
		Rep(i, m) {
			if (malted[i] != -1 && state[malted[i]] == 1)
				continue;
			bool flag = false;
			Rep(j, Size(unmalted[i])) {
				if (state[unmalted[i][j]] == 0) {
					flag = true;
					break;
				}
			}
			if (!flag) {
				ok = false;
				break;
			}
		}
		printf("Case #%d:", test);
		if (!ok) {
			printf(" IMPOSSIBLE\n");
		} else {
			Rep(i, n)
				printf(" %d", state[i]);
			printf("\n");
		}
	}

	exit(0);
}
