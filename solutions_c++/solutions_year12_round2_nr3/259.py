#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
#include <vector>
#include <algorithm>
typedef long long LL;
using namespace std;
#define F_IN  "C-small-attempt0.in"
#define F_OUT "C-small-attempt0.out"
#define PI 3.1415926535897932384626433832795

int a[100];
int b[100];
int n;

bool rec(int s1, int s2, int k)
{
	if (s2>0 && s1==s2)
	{
		return true;
	}
	if (k==n) return false;
	b[k] = 1;
	if (rec(s1 + a[k], s2, k+1)) return true;
	b[k] = 2;
	if (rec(s1, s2 + a[k], k+1)) return true;
	b[k] = 0;
	if (rec(s1, s2, k+1)) return true;
	return false;
}

int main()
{
    int tc, tt;
    freopen(F_IN, "r", stdin);
    freopen(F_OUT, "w", stdout);
    scanf("%i", &tc);
    for(tt=1; tt<=tc; ++tt)
    {
		scanf("%i", &n);
		for(int i=0; i<n; ++i) scanf("%i", &a[i]);
		rec(0, 0, 0);
		printf("Case #%i:\n", tt);
		for(int i=0; i<n; ++i) if (b[i]==1) printf("%i ", a[i]);
		printf("\n");
		for(int i=0; i<n; ++i) if (b[i]==2) printf("%i ", a[i]);
		printf("\n");
    }

    return 0;
}


