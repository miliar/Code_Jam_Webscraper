#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
#include <vector>
#include <algorithm>
typedef long long LL;
using namespace std;

//#define F_IN  "a.in"
//#define F_OUT "a.out"

#define F_IN  "A-large.in"
#define F_OUT "A-large.out"
#define PI 3.1415926535897932384626433832795
#define EPS 1e-9

int sum;
int a[1000];
int n;

bool accept(double value, double have, int skip)
{
	for(int i=0; i<n; ++i) if (a[i] < value && i != skip)
	{
		have -= value - a[i];
	}
	return have >= 0.0;
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
		sum = 0;
		for(int i=0; i<n; ++i)
		{
			scanf("%i", &a[i]);
			sum += a[i];
		}

		printf("Case #%i:", tt);
		for(int i=0; i<n; ++i)
		{
			double A=0.0;
			double B=1.0;
			double C;
			while (B-A>EPS)
			{
				C = (A+B)/2.0;
				if (!accept(a[i] + sum*C, (1 - C)*sum, i)) B = C; else A = C;
			}
			printf(" %.6f", A*100);			
		}
		printf("\n");
    }

    return 0;
}


