#include<stdio.h>
#include<string.h>
#include<math.h>
#include<iostream>
#include<algorithm>
#include<utility>
#include<sstream>
#include<vector>
#include<string>
#include<set>
#include<map>

using namespace std;

const int maxn = 200;
const double eps = 1e-12;

int C, D;
pair<int, int> dog[maxn];

bool check(double allow)
{
	double bound = -1e100;
	for(int i=0; i<C; i++)
	{
		double st = max(bound, dog[i].first - allow);
		double ed = st + 1.0 * (dog[i].second - 1) * D;

		if(ed > dog[i].first + allow) return false;

		bound = ed + D;
	}

	return true;
}

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

	int ntest;
	scanf("%d", &ntest);
	for(int test = 1; test <= ntest; test++)
	{
		scanf("%d%d", &C, &D);
		for(int i=0; i<C; i++)
		{
			scanf("%d%d", &dog[i].first, &dog[i].second);
		}

		sort(dog, dog + C);

		double lower = 0, upper = 1e13;

		for(int times=0; times<500; times++)
		{
			double mid = (lower + upper) / 2;
			if(check(mid)) upper = mid;
			else lower = mid;
		}

		printf("Case #%d: %.10lf\n", test, upper);
	}
	return 0;
}
