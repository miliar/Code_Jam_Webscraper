#include <iostream>
#include <cstdio>

using namespace std;
int gcd(int a, int b)
{
	//cout<<"gcd "<<a<<" "<<b<<endl;
	return b?gcd(b,a%b):a;
}
int main()
{
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t) {
		long long n, pd, pg;
		cin >> n >> pd >> pg;
		//pd=0,pg=0
		//cout<<"pd="<<pd<<endl;
		long long d;
		if (pd > 0) {
			int g = gcd(pd, 100);
			pd /= g;
			d = 100 / g;
		} else {
			pd = 0;
			d = 1;
		}
		//cout << "d="<<d<<endl;
		if (d > n) {
			printf("Case #%d: Broken\n", t);
			continue;
		}
		if (pg == 0) {
			if (pd > 0)
				printf("Case #%d: Broken\n", t);
			else
				printf("Case #%d: Possible\n", t);
			continue;
		}
		long long x = pd;
		long long dx;
		for (dx = 0; dx <= 100; ++dx)
			if ((100 * x + (100 - pg) * dx) % pg == 0) break;
		if (dx > 100 || (100 * x + (100 - pg) * dx) % pg != 0) {
			printf("Case #%d: Broken\n", t);
			continue;			
		}
		//cout << x << " " << dx << endl;
		if (100 * x + 100 * dx - pg * dx < pg * d) {
			if (100 == pg) {
				printf("Case #%d: Broken\n", t);
				continue;
			}
		}
		printf("Case #%d: Possible\n", t);
	}
}
