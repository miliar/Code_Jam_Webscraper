#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <string>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>

#define pb push_back
#define mp make_pair

using namespace std;

typedef long long lint;
typedef vector<int> vi;
typedef pair<int, int> pii;
const int Inf = 0x7fffffff;

vector<int> mas;
int d;
/*
lint f(lint x)
{
	lint res = 0;
	for(int i = 0; i < mas.size(); ++i)
	{
		res = max(res, abs(mas[i] - x));
		x += d;
	}
	return res;
}
*/
bool ok(double t)
{
	double left = mas[0] - t;
	for(int i = 1; i < (int)mas.size(); ++i)
	{
		if(mas[i] >= left + d)
			left = max(left + d, mas[i] - t);
		else
			if(mas[i] + t < left + d)
				return false;
			else
				left += d;
	}
	return true;
}

int Solution()
{
	mas.clear();
	int c;
	cin >> c >> d;
	for(int i = 0; i < c; ++i)
	{
		int p, v;
		cin >> p >> v;
		for(int j = 0; j < v; ++j)
			mas.pb(p);
	}
	/*
	lint l = -1 << 60, r = 1 << 60;
	while(r - l > 1000)
	{
		lint x = l + (r - l) / 3;
		lint y = r - (r - l) / 3;
		if(f(l) >= f(x) && f(x) >= f(y))
			l = x;
		else
			r = y;
	} */

	double l = 0., r = 1e14;
	while(r - l > 1e-10)
	{
		double x = (r + l) / 2.;
		if(ok(x))
			r = x;
		else
			l = x;
	}
	printf("%.10lf\n", (r + l) / 2.);
	return 0;
}

#define debug

int main()
{
#ifdef debug
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("B-small-attempt0.out", "w", stdout);
#endif
	int t;
	cin >> t;
	for(int i = 1; i <= t; ++i)
	{
		cout << "Case #" << i << ": ";
		Solution();
	}
#ifdef debug
	system("@pause");
#endif
	return 0;
}
