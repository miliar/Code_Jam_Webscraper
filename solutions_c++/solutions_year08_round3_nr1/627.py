#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;


int n, p, k, l, f;

int main() {
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	scanf("%i", &n);
	for (int t = 0; t<n; t++) {
		scanf("%i %i %i", &p, &k, &l);
		vector <int> a;
		for (int i = 0; i<l; i++) {
			scanf("%i", &f);
			a.push_back(f);
		}
		sort(a.rbegin(),a.rend());
		int res = 0;
		if ((l-1) / k >= p)
			res = -1;
		else
		for (int i = 0; i<l; i++) {
			res += a[i] * (i / k + 1);
		}
		printf("Case #%i: %i\n", t+1, res);
	}

}