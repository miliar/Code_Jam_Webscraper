#include <algorithm>
#include <iostream>
#include <sstream>
#include <cstdlib>
#include <bitset>
#include <cctype>
#include <cstdio>
#include <string>
#include <vector>
#include <queue>
#include <deque>
#include <cmath>
#include <stack>
#include <list>
#include <map>
#include <set>
using namespace std;

typedef long long LL;
typedef pair<int,int> PII;

int T, N, M, ans;
char s[1000];
set<string> st;

int main() {
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d", &T);
	for (int cas = 1; cas <= T; ++cas) {
		scanf("%d", &N);
		gets(s);
		for (int i = 0; i < N; ++i)
			gets(s);
		scanf("%d", &M);
		gets(s);
		st.clear();
		ans = 0;
		for (int i = 0; i < M; ++i) {
			gets(s);
			st.insert(s);
			if (st.size() == N) {
				ans++;
				st.clear();
				st.insert(s);
			}
		}
		printf("Case #%d: %d\n", cas, ans);
	}
	return 0;
}


