#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <queue>
#include <algorithm>
#include <iomanip>
#include <map>
#include <set>
#include <math.h>
#include <stack>
#include <deque>
#include <numeric>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <bitset>

#define all(v) v.begin(),v.end()
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
const ld epsylon = 1e-9;
typedef unsigned int ui;
inline long double get_time(){   
	return (long double)clock()/CLOCKS_PER_SEC;
};
//ld start_time,end_time;

int a[128];
int norm(int idx)
{
	if (a[idx] % 3 == 0) return a[idx]/3;
	if (a[idx] % 3 == 1) return a[idx]/3+1;
	if (a[idx] % 3 == 2) return a[idx]/3+1;
}
int surp(int idx)
{
	if (a[idx] % 3 == 0) return a[idx]/3+1;
	if (a[idx] % 3 == 1) return a[idx]/3+1;
	if (a[idx] % 3 == 2) return a[idx]/3+2;
}

int main()
{
	freopen("input.in","r",stdin);
	freopen("B-small-attempt0.out","w",stdout);
	int t;
	scanf("%d", &t);
	for (int T = 1; T <= t; T++)
	{
		   int n, s, p;
		   scanf("%d %d %d", &n, &s, &p);
		   for (int i = 0; i < n; ++i)
			   scanf("%d", &a[i]);
		   int surps = 0;
		   int res = 0;
		   for (int i = 0; i < n; ++i)
		   {
			   if (norm(i) < p && surp(i) >= p && surps  < s && a[i] > 1 && a[i] < 29) surps++, res++;
			   else if (norm(i) >= p) res++;
		   }
		   printf("Case #%d: %d\n", T, res);

	}

	return 0;
}