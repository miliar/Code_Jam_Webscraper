#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <sstream>
#include <cmath>
#include <cassert>
#include <memory.h>

using namespace std;

#define pb push_back
#define mp make_pair
#define sz(a) (int)(a).size()
#define _(a,b) memset((a), (b), sizeof(a))

void prepare()
{
#ifdef _DEBUG
	freopen("input.txt", "r", stdin);
#endif
	freopen("output.txt", "w", stdout);
}

void solve(int tt)
{
	int n, k, z;
	cin >> n >> k;
	z = 1 << n;
	assert(z > 0);
	printf("Case #%d: ", tt + 1);
	if ((k + 1) % z == 0)
		printf("ON\n");
	else
		printf("OFF\n");
}

int main()
{
	prepare();
	int i, t;
	cin >> t;
	for (i = 0; i < t; i++)
		solve(i);
	return 0;
}