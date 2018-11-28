#include <cstdio>
#include <cmath>
#include <vector>
#include <string>
#include <deque>
#include <map>
#include <algorithm>

using namespace std;

void solve()
{
	int n;
	vector<int> a, b;
	scanf("%d",&n);

	for(int i = 0; i < n; ++i) {
		int m;
		scanf("%d",&m);
		a.push_back(m);
	}
	b = a;
	sort(b.begin(), b.end());
	double r = 0.;
	for(int i = 0; i < a.size(); ++i) {
		if(a[i] != b[i]) r += 1.0;
	}
	printf("%lf\n",r);
}

int main(int argc, char *argv[])
{
	int kase;
	scanf("%d",&kase);
	for(int i = 1; i <= kase; ++i) {
		printf("Case #%d: ",i);
		solve();
	}
	return 0;
}
