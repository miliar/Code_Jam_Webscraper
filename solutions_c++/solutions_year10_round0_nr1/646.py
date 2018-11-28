const double pi=3.1415926535897932, e=2.7182818284590452;
#define _CRT_SECURE_NO_DEPRECATE
#pragma comment(linker, "/stack:16000000")
#include <cstdio>
#include <cmath>
#include <complex>
#include <algorithm>
#include <functional>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <map>
#include <set>
using namespace std;

int ii, nn;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	scanf("%d", &nn);
	for (ii=0; ii<nn; ++ii)
	{
		int x,y;
		scanf("%d%d", &x, &y);
		
		if (y%(1<<x) == (1<<x)-1)
			printf("Case #%d: ON\n", ii+1);
		else
			printf("Case #%d: OFF\n", ii+1);
	}
	return 0;
}
