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

int main()
{
	freopen("problem1.in", "r", stdin);
	freopen("problem1.out", "w", stdout);
	int tests, n, rp, rt, p[2], t[2];
	char crt;
	scanf("%d", &tests);
	for(int i=1; i<=tests; ++i)
	{
		scanf("%d", &n);
		p[0]=p[1]=1, t[0]=t[1]=0;
		for(int j=0; j<n; ++j)
		{
			scanf(" %c%d", &crt, &rp);
			rt=(crt=='O');
			t[rt]=max(t[1-rt], t[rt]+abs(rp-p[rt]))+1, p[rt]=rp;
		}
		printf("Case #%d: %d\n", i, max(t[0], t[1]));
	}
	return 0;
}