#include <cstdio>
#include <set>
using namespace std;
int a, b, r;
void gao(int n) {
	int d = 0, p = 1;
	for (int t = n; t; t /= 10) {
		++d;
		p *= 10;
	}
	p /= 10;
	set<int> ed;
	for (int i = 1, m = n; i != d; ++i)
	{
		int c = m % 10;
		m = m / 10 + c * p;
		if (m > n && m <= b) {
			ed.insert(m);
		}
	}
	r += ed.size();
}
int main(int argc, char const *argv[])
{
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; ++i)
	{
		scanf("%d%d", &a, &b);
		r = 0;
		for (int k = a; k <= b; ++k) {
			gao(k);
		}
		printf("Case #%d: %d\n", i, r);
	}
	return 0;
}