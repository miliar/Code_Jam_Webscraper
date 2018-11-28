#include <iostream>
#include <string>
#include <vector>
using namespace std;

bool noZero(int a)
{
	return true;
	while (a)
	{
		if (a%10 == 0)
			return false;
		a /= 10;
	}
	return true;
}
bool check(int a, int b)
{
	int len = 0, ten = 1, aa = a;
	while (aa)
	{
		++len;
		ten *= 10;
		aa /= 10;
	}
	ten /= 10;
	for (int i = 0; i < len; ++i)
	{
		a = (a % ten) * 10 + a / ten;
		if (a == b)
			return true;
	}
	return false;
}
int main()
{
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int nt, t;
	scanf("%d", &nt);
	for (t = 1; t <= nt; ++t)
	{
		int a, b, n, m;
		scanf("%d%d", &a, &b);
		int ans = 0;
		for (n = a; n <= b; ++n)
			if (noZero(n))
				for (m = n + 1; m <= b; ++m)
					if (noZero(m) && check(n, m))
						++ans;
		t = t;
		printf("Case #%d: %d\n", t, ans);
	}
	return 0;
}
	