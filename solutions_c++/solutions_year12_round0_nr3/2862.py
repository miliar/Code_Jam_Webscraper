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

void shift(char * v, int b)
{
	char tmp = v[0];
	for (int i = 0; i < b-1; ++i)
	{
		v[i] = v[i + 1];
	}
	v[b-1] = tmp;
}

bool rec(int u, int v)
{
	char uu[40], vv[40];
	memset(uu, 0, sizeof(uu));
	memset(vv, 0, sizeof(vv));
	sprintf(uu, "%d", u);
	sprintf(vv, "%d", v);
	int br = 0;
	while (u) u/=10, br++;
	for (int i = 0; i < br+3; ++i)
	{
		if (strcmp(uu, vv) == 0) return true;
		else {
			shift(vv, br);
		}
	}
	return false;
}

int main()
{
	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);
	int t;
	scanf("%d", &t);
	for (int T = 1; T <= t; ++T)
	{
		int a, b;
		scanf("%d %d", &a, &b);
		unsigned long long res = 0;
		for (int i = a; i < b; ++i)
			for (int j = i+1; j <= b; ++j)
				if (rec(i, j)) res++;
		printf("Case #%d: %lld\n", T, res);
	}
	return 0;
}