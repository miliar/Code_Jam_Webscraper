#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;

pair<int,int> x[1011];
bool cmp(const int& a, const int& b) {
	return make_pair(-x[a].first*x[a].second, a)
	     < make_pair(-x[b].first*x[b].second, b);
}

int main()
{
	int T; cin >> T;
	for (int ti = 1; ti <= T; ti++) {
		int N; cin >> N;
		for (int i = 0; i < N; i++) cin >> x[i].first;
		for (int i = 0; i < N; i++) cin >> x[i].second;

		int a[1011];
		for (int i = 0; i < N; i++) a[i] = i;
		sort(a, a+N, cmp);

		printf("Case #%d:", ti);
		for (int i = 0; i < N; i++) {
			printf(" %d", a[i]);
		}
		puts("");
	}
}
