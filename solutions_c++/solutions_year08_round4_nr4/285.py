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

int nn,n,k,res;
char s[100000];
int perm[100];

int main()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	scanf("%d\n",&nn);
	for (int ii=1; ii<=nn; ++ii)
	{
		scanf("%d\n",&k);
		gets(s);
		n=(int)strlen(s);
		for (int i=0; i<k; ++i)
			perm[i]=i;
		res=1000000000;
		do
		{
			int r=0;
			char old=0;
			for (int i=0; i<n; ++i)
			{
				char c=s[i/k*k+perm[i%k]];
				if (old!=c)
					++r;
				old=c;
			}
			res=min(res,r);
		} while (next_permutation(&perm[0], &perm[k]));
		printf("Case #%d: %d\n", ii, res);
	}
	return 0;
}
