#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

int main (void) {
	int testnum;
	vector < int > V;
	scanf ("%d", &testnum);
	for (int testcase = 1; testcase <= testnum; testcase++) {
		int n;
		scanf ("%d", &n);
		V.clear();
		int s = 0, sum = 0, min_value = 1000001;
		for ( int i = 0; i < n; i++) {
			int tmp;
			scanf( "%d", &tmp);
			V.push_back(tmp);
			s = s ^ tmp;
			sum += tmp;
			min_value = min( min_value, tmp);
		}
		sort(V.begin(), V.end());
		if (s == 0)
			printf ( "Case #%d: %d\n", testcase, sum - min_value);
		else
			printf ( "Case #%d: NO\n", testcase);
	}
	return 0;
}



