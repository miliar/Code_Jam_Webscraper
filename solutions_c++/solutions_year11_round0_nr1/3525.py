#include<iostream>
#include<cmath>
using namespace std;

const int maxn = 100 + 10;
char ord[maxn];
int a[maxn], n;

void solve()
{
	scanf("%d", &n);
		int po, pb, lo, lb, curt;
	curt = lo = lb = 0;
	po = pb = 1;
	for (int i = 0; i < n; i++) {
		scanf(" %c %d", &ord[i], &a[i]);
		//printf("%c %d\n", ord[i], a[i]);
		if (ord[i] == 'O') {
			if (lo + abs(po - a[i]) + 1 <= curt)
				lo = ++curt;
			else curt = lo += abs(po - a[i]) + 1;
			po = a[i];
		} else
		{
			if (lb + abs(pb - a[i]) + 1 <= curt)
				lb = ++curt;
			else curt = lb += abs(pb - a[i]) + 1;
			pb = a[i];
		}
	}
	scanf("\n");
	printf("%d\n", curt);
}

int main()
{
	int T, t;
	for (scanf("%d\n", &T), t = 1; t <= T; t++) {
		printf("Case #%d: ", t);
		solve();
	}
}
