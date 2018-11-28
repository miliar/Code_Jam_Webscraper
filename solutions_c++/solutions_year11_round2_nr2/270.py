#include <iostream>
using namespace std;

pair<int, int> a[210];
int n, limit;

bool check(double delta) {
	double last = -1E+30;
	for (int i = 1; i <= n; i ++) {
		double le = a[i].first - delta;
		double ri = a[i].first + delta;
		int cnt = a[i].second;
		last = max(last+limit, le) + (double)(cnt-1) * limit;
		if (last > ri)
			return false;
	}
	return true;
}

void solve(int case_index) {
	cerr << case_index << endl;
	scanf("%d%d", &n, &limit);
	for (int i = 1; i <= n; i ++)
		scanf("%d%d", &a[i].first, &a[i].second);
	sort(a+1, a+n+1);
	double le = 0, ri = 1E+30;
	for (int i = 0; i < 500; i ++) {
		double mid = (le+ri) * 0.5;
		if (check(mid))
			ri = mid;
		else
			le = mid;
	}
	printf("Case #%d: %.4lf\n", case_index, le);
}

int main() {
	int case_count;
	scanf("%d", &case_count);
	for (int i = 1; i <= case_count; i ++)
		solve(i);
	return 0;
}