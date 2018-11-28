#define _USE_MATH_DEFINES
#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <utility>
#include <string>
#include <vector>
#include <ctime>
#include <set>

using namespace std;

#pragma comment (linker, "/STACK:64000000")

bool is_between(int x, int l, int r)
{
	return x >= l && x <= r;
}

int dig_number(int x)
{
	int count = 0;
	while (x) x/=10, count++;
	return count;
}

long long f(int a,int l, int r)
{
	int k = a, c = 1, d = 1;
	set <int> google_code_jam_is_the_awesomest_contest_in_the_world;
	//bool b_ar[2000001] = {0};
	int a_dig = dig_number(a);
	long long res = 0;
	k/=10;
	while (k) ++c, k /= 10, d*=10;
	k = a;
	for (int i = 0; i < c; ++i)
	{
		k = k/10 + (k%10)*d;
		if (a < k && is_between(k,l,r) && a_dig == dig_number(k) && !google_code_jam_is_the_awesomest_contest_in_the_world.count(k))// && !b_ar[k])
			++res,google_code_jam_is_the_awesomest_contest_in_the_world.insert(k);//, b_ar[k]=1;
		
	}
	return res;
}


int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);

	int t, a, b;
	long long res;
	scanf("%d", &t);

	for (int i = 0; i < t; ++i)
	{
		res = 0;
		scanf("%d%d", &a, &b);
		for (int j = a; j <= b; ++j)
			res += f(j,a,b);
		printf("Case #%d: %I64d\n", i+1, res);
	}

	

	return 0;
} 