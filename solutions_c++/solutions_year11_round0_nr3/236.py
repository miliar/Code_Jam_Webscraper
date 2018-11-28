#include <cstdio>;
#include <cstring>;
#include <vector>;
#include <iostream>;
#include <algorithm>;
using namespace std;

int n;
int a[1010];

int calc()
{
	int sum1 = 0;
	sort(a, a+n);
	for (int i=1; i<n; i++) sum1 += a[i];
	return sum1;
}

int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T = 0;
	cin >> T;
	for (int i=1; i<=T; i++)
	{
		cin >> n;
		for (int j=0; j<n; j++) cin >> a[j];
		int ret = 0;
		for (int j=0; j<n; j++) ret = ret ^ a[j];
		if (ret == 0)
			printf("Case #%d: %d\n", i, calc());
		else
			printf("Case #%d: NO\n", i);
	}
}