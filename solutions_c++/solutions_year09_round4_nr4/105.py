
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
using namespace std;

#define sz 5

int x[sz];
int y[sz];
int r[sz];

double dist(int i)
{
	int j, k;
	if (!i) j = 1;
	else j = 0;
	if (i == 2) k = 1;
	else k = 2;
	double ret = 0.0;
	ret += double(r[j] + r[k]);
	ret += sqrt(double( (x[j]-x[k])*(x[j]-x[k]) + (y[j]-y[k])*(y[j]-y[k]) ));
	return (ret/2.0);
}

int main ()
{
	freopen("D-small-attempt0.in", "r", stdin);
	freopen("D-small.txt", "w", stdout);
	int test_cases;
	cin >> test_cases;
	for (int numb = 0; numb < test_cases; numb++)
	{
		int n;
		cin >> n;
		for (int i = 0; i < n; i++)
			cin >> x[i] >> y[i] >> r[i];
		double ret; 
		if (n == 1) ret = double(r[0]);
		else if (n==2) ret = max(double(r[0]), double(r[1]));
		else
		{
			ret = 10000000.0;
			for (int i = 0; i < 3; i++)
				ret = min(ret, max(double(r[i]), dist(i)));
		}
		printf("Case #%d: %.7f\n", numb+1, ret);
	}
	return 0;
}
