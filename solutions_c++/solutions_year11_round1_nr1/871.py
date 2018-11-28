#include<stdio.h>
#include<algorithm>
using namespace std;

long long n;
int pd, pg;

bool solve()
{
	scanf("%I64d %d %d", &n, &pd, &pg);
	if (pd < 100 && pg == 100)return false;
	if (pd > 0 && pg == 0)return false;
	for(int i = 1; i <= n && i <= 200; ++i)
	{
		if(i * pd % 100 == 0)return true;;
	}
	return false;
}

int main()
{
	int tc;
	scanf("%d", &tc);
	for (int t = 1; t <= tc; t++)
	{
		printf("Case #%d: ", t);
		puts(solve() ? "Possible" : "Broken");
	}
	return 0;
}
