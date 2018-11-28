#include <cstdio>
#include <string>
#include <set>
using namespace std;

char str[128];

int run()
{
	int n;
	scanf("%d", &n);
	gets(str);
	for (int i = 0; i < n; ++i) {
		gets(str);
	}
	int m;
	scanf("%d", &m);
	gets(str);
	set<string> st;
	int ret = 0;
	for (int i = 0; i < m; ++i) {
		gets(str);
		st.insert(str);
		if (st.size() == n) {
			++ret;
			st.clear();
			st.insert(str);
		}
	}
	return ret;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; ++i) {
		printf("Case #%d: %d\n", i, run());
	}
}
