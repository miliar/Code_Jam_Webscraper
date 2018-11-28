#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <assert.h>
#include <time.h>
#include <math.h>

#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <functional>
#include <string>
#include <set>
#include <map>
#include <iostream>


using namespace std;
const int inf = 0x7fffffff;
typedef long long int llint;
typedef map<llint, int> mapa;

mapa M;
llint a[500];
int take[500];
int n;

void reset_take()
{
	memset(take, 0, sizeof take);
	take[0] = 1;
}

void next_take()
{
	int i = 0;
	for (i = 0; take[i] == 1; i++)
		take[i] = 0;
	take[i] = 1;
}

llint get_sum()
{
	llint sum = 0;
	for (int i = 0; i < 20; i++)
		sum += take[i] ? a[i] : 0;
	return sum;
}

void print_hit()
{
	bool first = true;
	for (int i = 0; i < 20; i++) {
		if (take[i]) {
			if (!first) putchar(' ');
			first = false;
			printf("%lld", a[i]);
		}
	}
	printf("\n");
}

int solve()
{
	int i, j, k;
	bool hit_found = false;
	llint hit_sum;
	llint sum;
	sort(a, a+n);
	reset_take();
	do {
		sum = get_sum();
		M[sum]++;
		if (M[sum] == 2)
		{
			hit_found = true;
			hit_sum = sum;
			print_hit();
			break;
		}
		next_take();
	} while (take[20] == 0);
	
	if (!hit_found)
	{
		printf("Impossible\n");
		return 0;
	}
	
	reset_take();
	for (reset_take(); 1; next_take())
	{
		sum = get_sum();
		if (sum == hit_sum) {
			print_hit();
			return 0;
		}
	}
}

int main()
{
	int i, j, k;
	int t;
	scanf("%d", &t);

	for (int tt = 0; tt < t; tt++)
	{
		M.clear();
		scanf("%d", &n);
		for (i = 0; i < n; i++)
			scanf("%lld", a+i);
		printf("Case #%d:\n", tt+1);
		solve();
	}
	
	return 0;
}

