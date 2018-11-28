#include <cstdio>
#include <iostream>
using namespace std;

int T, ttt;
long long n;
int pd, pg;

void out(bool flag)
{
	printf("Case #%d: ", ++ttt);
	if (flag)
		printf("Possible\n");
	else
		printf("Broken\n");
}

void work()
{
	cin >> n >> pd >> pg;
	if (pd == 0) {
		if (pg == 100)
			out(false);
		else
			out(true);
		return;
	}
	if (pd > 0 && pd < 100 && (pg == 0 || pg == 100)) {
		out(false);
		return;
	}
	if (pd == 100) {
		if (pg == 0)
			out(false);
		else
			out(true);
		return;
	}
	int c2 = 0, c5 = 0;
	while (pd % 2 == 0) {pd /= 2; ++c2;}
	while (pd % 5 == 0) {pd /= 5; ++c5;}
	int ans = 1;
	for (int i = 1; i <= 2 - c2; ++i) ans *= 2;
	for (int i = 1; i <= 2 - c5; ++i) ans *= 5;
	if (ans <= n)
		out(true);
	else
		out(false);
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	scanf("%d", &T);
	while (T--) work();
}