#include<iostream>
#include<algorithm>
#include<cstdio>
#include<vector>
using namespace std;

struct walk {
	size_t b, e, s;
	walk() {}
	double len() const {
		return e - b;
	}
};

bool comp(walk a, walk b)
{
	return a.s < b.s;
}

void work()
{
	size_t X, S, R, N, D, T;
	cin >> X >> S >> R >> T >> N;
	vector<walk> a(N);
	size_t le = 0;
	for(size_t i = 0; i < N; i++) {
		cin >> a[i].b >> a[i].e >> a[i].s;
		if(le != a[i].b) {
			a.push_back(walk());
			a.back().b = le;
			a.back().e = a[i].b;
			a.back().s = S;
		}
		le = a[i].e;
		a[i].s += S;
	}
	if(le != X) {
		a.push_back(walk());
		a.back().b = le;
		a.back().e = X;
		a.back().s = S;
	}
	D = R - S;
	double t = T, ans = 0;
	sort(a.begin(), a.end(), comp);
	bool flag = 1;
	for(const auto & i: a) {
		if(flag) {
			double use = i.len() / (i.s + D);
			if(use < t) {
				t -= use;
				ans += use;
			} else {
				use = (i.len() - t * (i.s + D)) / i.s;
				ans += use + t;
				flag = 0;
			}
		} else {
			ans += i.len() / i.s;
		}
	}
	printf("%.10lf\n", ans);
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int kase;
	scanf("%d", &kase);
	for(int i = 1; i <= kase; i++) {
		printf("Case #%d: ", i);
		work();
	}
}
