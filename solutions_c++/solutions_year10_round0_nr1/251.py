#define _CRT_SECURE_NO_DEPRECATE
#include <stdio.h>
#include <memory.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include <set>
#include <map>
#include <string>
#include <vector>
#include <queue>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <ctime>
#include <fstream>
#include <iostream>

using namespace std;

#define CL(x) memset(x, 0, sizeof(x))

#define FOR(i, n) for (int i = 0; i < (int)(n); i++)

typedef long long LL;
typedef vector<int> vi;
typedef vector<string> VS;

void Solve()
{
	int n, k;
	scanf("%d %d", &n, &k);
	int m = (1 << n) - 1;
	if ((k & m) == m)
		printf("ON\n");
	else
		printf("OFF\n");
}


int main()
{
	freopen("c:\\my\\in.txt", "r", stdin);
	freopen("c:\\my\\out.txt", "w", stdout);

	int t;
	scanf("%d", &t);

	FOR(i, t)
	{
		printf("Case #%d: ", i + 1);
		Solve();
	}
	return 0;
}