#pragma comment(linker,"/STACK:256000000")

#ifdef __GNUC__
#define int64 long long
#else /* MSVC, say */
#define int64 __int64
#endif 

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <memory.h>
#include <ctype.h>
#include <stdlib.h>
#include <iostream>
#include <sstream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <stack>

using namespace std;

#define MAX(a,b) (((a) > (b)) ? (a) : (b))
#define MIN(a,b) (((a) < (b)) ? (a) : (b))

#define MAXN (1 << 8)

int main() {
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);

	int tests;
	scanf("%d", &tests);
	for (int test = 0; test < tests; test++) {
		int n, m;
		scanf("%d\n", &m);
		vector <string> s, q;
		for (int i = 0; i < m; i++) {
			char buf[MAXN];
			gets(buf);
			s.push_back(string(buf));
		}
		scanf("%d\n", &n);
		for (int i = 0; i < n; i++) {
			char buf[MAXN];
			gets(buf);
			q.push_back(string(buf));
		}
		for (int i = 0; i < m; i++) {
			q.push_back(s[i]);
		}
		int ans = 0;
		int pos = 0;
		while (1) {
			set <string> dict;
			while (pos < q.size()) {
				string cur = q[pos];
				dict.insert(cur);
				if (dict.size() == m) {
					break;
				}
				pos++;
			}
			if (pos >= n) {
				break;
			}		
			ans++;
		}
		printf("Case #%d: %d\n", test + 1, ans);
	}

	return 0;
}
