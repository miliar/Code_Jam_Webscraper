#include <cstdio>
using namespace std;

void Ans(int testcase, char msg[])
{
	printf("Case #%d: %s\n", testcase, msg);
}
typedef long long int64;
bool check1(int64 n, int pd)
{
	if (pd == 0) return true;
	int f2 = 0, f5 = 0;
	while (pd != 0 && pd % 2 == 0)
	{
		pd /= 2;
		f2++;
	}
	while (pd != 0 && pd % 5 == 0)
	{
		pd /= 5;
		f5++;
	}
	if (f2 > 2) f2 = 2;
	if (f5 > 5) f5 = 2;
	int f = 1;
	for (int i = 1; i <= f2; i++)
		f *= 2;
	for (int i = 1; i <= f5; i++)
		f *= 5;
	return n >= (100 / f);
}
int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int testcase = 1; testcase <= T; testcase++)
	{
		int64 n;
		int pd, pg;
		scanf("%lld%d%d", &n, &pd, &pg);
		if (check1(n, pd))
		{
			if (pg == 100 && pd != 100)
				Ans(testcase, "Broken");
			else if (pg == 0 && pd != 0)
				Ans(testcase, "Broken");
			else
				Ans(testcase, "Possible");
		}
		else
			Ans(testcase, "Broken");
	}
}
