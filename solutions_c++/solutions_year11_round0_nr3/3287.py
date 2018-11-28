#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <cmath>
#include <cassert>
#include <cstdlib>
#include <cstring>
#include <queue>
#include <stack>

#define all(x) (x).begin(),(x).end()
#define nmax 1000000

using namespace std;

int a[nmax];

void solve(int _case)
{
	int n;
	scanf("%d",&n);
	for (int i = 0; i < n; i ++)
		scanf("%d",&a[i]);
	int x = 0;
	int s = 0;
	for (int i = 0; i < n; i ++)
	{
		x ^= a[i];
		s += a[i];
	}
	printf("Case #%d: ",_case);
	if (x != 0)
		printf("NO\n");
	else
		printf("%d\n", s - *min_element(a,a + n));
}

int main()
{
	int t;
	scanf("%d",&t);
	for (int i = 1; i <= t; i ++)
		solve(i);
	return 0;
}
