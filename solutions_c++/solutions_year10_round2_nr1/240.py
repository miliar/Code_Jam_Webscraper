#include <string>
#include <cstring>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>
#include <queue>
#include <cassert>

using namespace std;

int T;
const int MAXN = 110;

int main(void) 
{
	scanf("%d", &T);

	for (int t = 1; t <= T; ++t) {
		
		set < string > S;
		int N, M, ret = 0;

		cin >> N >> M;

		for (int i = 0; i < N; ++i) {
			char cpath[MAXN];
			scanf("%s", cpath);

			string path = cpath;
			path = path + "/";
			S.insert(path);
		}

		string need[MAXN];

		for (int i = 0; i < M; ++i) {
			char cpath[MAXN];
			scanf("%s", cpath);

			need[i] = cpath;
			need[i] = need[i] + "/";
		}

		sort(need, need + M);

		for (int i = 0; i < M; ++i) {
			string part = "/";

			for (int j = 1; j < need[i].size(); ++j) {
				part = part + need[i][j];
				if (need[i][j] == '/') {
					if (S.find(part) == S.end()) {
						++ret;
						S.insert(part);
					}
				}
			}
		}

		printf("Case #%d: %d\n", t, ret);
	}

	return 0;
}