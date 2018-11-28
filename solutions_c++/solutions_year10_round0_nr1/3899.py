#include <algorithm>
#include <functional>
#include <cmath>
#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <sstream>
#include <queue>
#include <iostream>

using namespace std;

int tc, n, k;

int main()
{
	//freopen("A-small.in", "r", stdin);
	//freopen("A-small.out", "w", stdout);
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	scanf("%d", &tc);
	for(int T = 1; T <= tc; ++T)
	{
		scanf("%d %d", &n, &k);
		printf("Case #%d: ", T);
		if(k % (1 << n) == (1 << n) - 1)
			printf("ON\n");
		else
			printf("OFF\n");
	}
	return 0;
}
