#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;

int cases;
int curcase;
int pg, pd;
long long N;

int gcd(int a, int b) {
	return b == 0 ? a : gcd(b, a % b);
}

int main()
{
	freopen("A-large (1).in", "r", stdin);
	freopen("out.txt", "w", stdout);

	scanf("%d", &cases);
	curcase = 1;

	while (curcase <= cases)
	{
		scanf("%lld%d%d", &N, &pd, &pg);

		bool possi;
		if (pg == 0){
			if(pg == 0 && pd == 0)
				possi = true;
			else
				possi = false;
		}
		else if (pg == 100){
			if(pd == 100 && pg == 100)
				possi = true;
			else
				possi = false;
		}
		else
			possi = (100/gcd(100, pd) <= N);

		if(possi == true)
			printf("Case #%d: Possible\n", curcase);
		else
			printf("Case #%d: Broken\n", curcase);

		curcase ++;
	}
}
