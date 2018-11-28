#include <cstdio>
#include <algorithm>
#include <set>
#include <queue>
#include <string>
#include <vector>
#include <list>
using namespace std;

void testcase() {
	int n;
	scanf("%d", &n);
	vector<int> seq;
	int ksoros = 0, minim = INT_MAX;
	int suma = 0;
	for (int i = 0; i < n; ++i) {
		int x;
		scanf("%d", &x);
		seq.push_back(x);
		ksoros ^= x;
		suma += x;
		minim = min(minim, x);
	}
	if (ksoros != 0) printf("NO\n");
	else printf("%d\n", max(suma-minim, minim));
}

int main() {
	int t, v = 0;
	for (scanf("%d", &t); t--;) {
		printf("Case #%d: ", ++v);
		testcase();
	}
}
