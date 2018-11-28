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

using namespace std;

int a[100000];

void solve()
{
	int n,l,r;
	scanf("%d%d%d",&n,&l,&r);
	for (int i = 0; i < n; i ++)
		scanf("%d",&a[i]);
	for (int i = l; i <= r; i ++)
	{
		bool ok = 1;
		for (int j = 0; j < n; j ++)
			ok = ok && ((i % a[j] == 0) || (a[j] % i == 0));
		if (ok)
		{
			printf("%d\n",i);
			return;
		}
	}
	printf("NO\n");

}

int main()
{
	int t;
	cin >> t;
	for (int i = 1; i <= t; i ++)
	{
		printf("Case #%d: ", i);
		solve();
	}
	return 0;
}
