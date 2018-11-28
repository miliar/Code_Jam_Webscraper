#include <cstdio>
#include <ctime>
#include <cassert>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <set>
#include <map>
#include <vector>
#include <algorithm>
#include <string>
#include <iostream>
using namespace std;
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define pi 3.1415926535897932384626433832795

const int inf=1000000000;

int main()
{
	freopen("problem3.in", "r", stdin);
	freopen("problem3.out", "w", stdout);
	int tests, n, x;
	scanf("%d", &tests);
	for(int i=1; i<=tests; ++i)
	{
		scanf("%d", &n);
		int sum=0, xor=0, minx=inf;
		for(int j=0; j<n; ++j)
		{
			scanf("%d", &x);
			sum+=x, xor^=x, minx=min(minx, x);
		}
		if(xor!=0)
			printf("Case #%d: NO\n", i);
		else
			printf("Case #%d: %d\n", i, sum-minx);
	}
	return 0;
}