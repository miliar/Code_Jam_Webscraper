#include <cstdio>
#include <string>
#include <cstring>
#include <set>

using namespace std;

char str[123];

int dd()
{
	set<string> st;
	int a, b;
	scanf("%d %d", &a, &b);
	for (int i = 0; i < a; ++i) {
		scanf("%s", str);
		st.insert(str);
	}
	int ret = 0;
	for (int i = 0; i < b; ++i) {
		scanf("%s", str);
		for (int j = 1; str[j]; ++j) {
			if (str[j] == '/') {
				str[j] = 0;
				if (st.find(str) == st.end()) {
					++ret;
					st.insert(str);
				}
				str[j] = '/';
			}
		}
		if (st.find(str) == st.end()) {
			++ret;
			st.insert(str);
		}
	}
	return ret;
}

int main()
{
	freopen("AA.in", "r", stdin);
	freopen("AA.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; ++i) {
		printf("Case #%d: %d\n", i, dd());
	}
	return 0;
}