#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
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
#include <ctime>

using namespace std;

const int inf = 1000 * 1000 * 1000;

typedef vector<int> vint;
typedef vector<vint> vvint;
//typedef double D;
typedef long long LL;

vector<string> A;
vector<double> wp, oowp, owp;


int t, n;

double WP(int x, int y = -1)
{
	int k = 0;
	int w = 0;
	for(int i = 0; i < n; ++i)
		if (A[x][i] != '.' && i != y)
			k++, w += (A[x][i] == '1');
	return (w + 0.0) / (k + 0.0);
}

double OWP(int x)
{
	if (owp[x] != -1.0)
		return owp[x];
	double res = 0;
	int k = 0;
	for(int i = 0; i < n; ++i)
		if (A[x][i] != '.')
			k++, res += WP(i, x);
	return owp[x] = res / (k + 0.0);
}

double OOWP(int x)
{
	if (oowp[x] != -1.0)
		return oowp[x];
	double res = 0;
	int k = 0;
	for(int i = 0; i < n; ++i)
		if (A[x][i] != '.')
			k++, res += OWP(i);
	return oowp[x] = res / (k + 0.0);
}


int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin >> t;
	for(int I = 1; I <= t; ++I)
	{
		cin >> n;
		wp.assign(n, -1.0);
		owp.assign(n, -1.0);
		oowp.assign(n, -1.0);
		A.clear();
		A.assign(n, string());
		for(int i = 0; i < n; ++i)
			cin >> A[i];
		printf("Case #%d:\n", I);
		for(int i = 0; i < n; ++i)
			WP(i);
		for(int i = 0; i < n; ++i)
			OWP(i);
		for(int i = 0; i < n; ++i)
			OOWP(i);
		for(int i = 0; i < n; ++i)
			printf("%.8lf\n", 0.25 * WP(i) + 0.5 * OWP(i) + 0.25 * OOWP(i));
	}
	return 0;

}