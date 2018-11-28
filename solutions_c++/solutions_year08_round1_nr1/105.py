#include <cstdio>
#include <vector>
#include <algorithm>
#include <functional>
using namespace std;

#define ALL(v) (v).begin(), (v).end()
#define SZ(v) (int)((v).size())
#define FOR(i, a, b) for(__typeof(a) i = (a); i < (b); i++)

typedef long long llong;

int main()
{
	vector<llong> n1, p1, n2, p2;
	int T;
	scanf("%d", &T);
	FOR(t, 0, T) {
		int n; scanf("%d", &n);
		n1.clear(); p1.clear();
		n2.clear(); p2.clear();
		FOR(i, 0, n) {
			int e; scanf("%d", &e);
			if(e > 0) p1.push_back(e);
			else n1.push_back(-e);
		}
		FOR(i, 0, n) {
			int e; scanf("%d", &e);
			if(e > 0) p2.push_back(e);
			else n2.push_back(-e);
		}
		llong res = 0;
		sort(ALL(p1), greater<llong>()); sort(ALL(n1), greater<llong>());
		sort(ALL(p2), greater<llong>()); sort(ALL(n2), greater<llong>());
		int m1 = min(SZ(p1), SZ(n2)), m2 = min(SZ(p2), SZ(n1));
		FOR(i, 0, m1) res -= p1[i]*n2[i];
		FOR(i, 0, m2) res -= p2[i]*n1[i];
		FOR(i, m1, SZ(p1)) res += p1[i]*p2[SZ(p2)-1-i+m1];
		FOR(i, m1, SZ(n2)) res += n2[i]*n1[SZ(n1)-1-i+m1];
		printf("Case #%d: %lld\n", t+1, res);
	}
	return 0;
}

