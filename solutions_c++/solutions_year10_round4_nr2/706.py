#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>

using namespace std;

static int
doit()
{
	int p;
	scanf("%d", &p);
	int n = 1 << p;
	static char got[1024];
	memset(got, 0, sizeof(got));
	for (int i = 0; i < n; i++) {
		int m;
		scanf("%d", &m);
		vector<int> v;
		for (int k = (n+i)/2; k >= 1; k /= 2)
			v.push_back(k);
		for (int i = 0; i < p-m; i++) {
			int a = v.back();
			got[a] = 1;
			v.pop_back();
		}
	}
	int all = 0;
	for (int i = 1; i < n; i++)
		if (got[i])
			all++;
	// read price; pass
	for (int i = 1; i < n; i++) {
		int t;
		scanf("%d", &t);
	}

	return all;
}

int
main()
{
	int t;
	scanf("%d", &t);
	for (int i = 0; i < t; i++)
		printf("Case #%d: %d\n", i+1, doit());
	return 0;
}
