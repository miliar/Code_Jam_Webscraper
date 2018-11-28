#include<iostream>
#include<cmath>
#include<algorithm>
using namespace std;

int n, s, p;
int a[200];

void solve()
{	
	scanf("%d %d %d", &n, &s, &p);
	for (int i = 0; i < n; i++) scanf("%d", &a[i]);
	sort(a, a + n);
	int ans = 0, tmp;
	for (int i = n - 1; i >= 0; i--)
		if ((a[i] + 2) / 3 >= p) {
			ans++;
		} else if (s > 0) {
			if (a[i] % 3 == 1)
				tmp = (a[i] + 2) / 3;
			else if (a[i] % 3 == 0)
				tmp = (a[i] + 3) / 3;
			else tmp = (a[i] + 4) / 3;
			if (tmp >= p && tmp - 2 >= 0 && tmp <= 10) {
				s--;
				ans++;
			}
		}
	printf("%d\n", ans);
			
}

int main()
{	
	int T, t;
	for (scanf("%d\n", &T), t = 1; t <= T; t++) {
		printf("Case #%d: ", t);		
		solve();
	}
}
