#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <string>
#include <cmath>
using namespace std;

const double PI = 3.1415926535897932384626433832795;

char buf[10000];
int a[10000];

int gcd (int a, int b)
{
	if (b == 0)
		return a;
	else
		return gcd (b, a % b);
}

void solve()
{
	int n, l, h;
	scanf("%d%d%d", &n, &l, &h);
	for(int i = 0; i < n; ++i)
		scanf("%d", &a[i]);
	for(int i = l; i <= h; ++i) {
		bool ok = true;
		for(int j = 0; j < n; ++j) {
			int g = gcd(i, a[j]);
			if (g == i || g == a[j])
				;
			else
			{
				ok = false;
				break;
			}
		}
		if (ok) {
			cout << i << endl;
			return;
		}
	}
	cout << "NO\n";
}

int main()
{
	freopen("in.txt", "rt", stdin);
	freopen("out.txt", "wt", stdout);
	int t;
	gets(buf);
	t = atoi(buf);
	for(int i = 0; i < t; ++i) {
		printf("Case #%d: ", i + 1);
		solve();
	}
	return (0);
}
