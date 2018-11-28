#include <stdio.h>
#include <map>
#include <string>

using namespace std;

int nextEngine(int s, int q, int queries[], int start)
{
	bool used[128] = {false};
	int numfree = s;
	while (start < q) {
		if (!used[queries[start]]) {
			numfree--;
			used[queries[start]] = true;
		}
		if (!numfree) return start;
		start++;
	}
	return q;
}

string getstring()
{
	char buff[1028];
	fgets(buff, sizeof(buff), stdin);
	int l = strlen(buff);
	if (l && buff[--l] == '\n')
		buff[l] = 0;
	return string(buff);
}

int main(void)
{
	//freopen("a-sample.in", "rt", stdin);
	//
	int T;
	T = atoi(getstring().c_str());
	for (int tc = 1; tc <= T; tc++) {
		printf("Case #%d: ", tc);
		map<string,int> engines;
		int queries[1024];
		int s, q;
		s = atoi(getstring().c_str());
		for (int i = 0; i < s; i++) {
			engines[getstring()] = i;
		}
		q = atoi(getstring().c_str());
		for (int i = 0; i < q; i++) {
			queries[i] = engines[getstring()];
		}
		int ans = 0;
		int x = nextEngine(s, q, queries, 0);
		if (x < q) {
			do {
				ans++;
				x = nextEngine(s, q, queries, x);
			} while (x < q);
		}
		printf("%d\n", ans);
	}
	//
	return 0;
}
