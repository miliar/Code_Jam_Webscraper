#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <cstring>
#include <string.h>
using namespace std;
int digits;
int count(int n)
{
	int res = 0;
	while(n > 9)
	{
		res++;
		n /= 10;
	}
	return res;
}
bool ok (int n, int m)
{
	int f = 10;
	int d = digits;
	while (d)
	{
		int newN = ((n%f)*d) + n/f;
		if(newN == m)
			return true;
		f *= 10;
		d /= 10;
	}
	return false;
}
int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t, a, b, res;
	cin >> t;
	for (int T = 1; T <= t; ++T)
	{
		cin >> a >> b;
		
		digits = pow(10.0, count(a));
		res = 0;
		for (int n = a; n <= b; ++n)
		{
			set<int>adj;
			int d = digits;
			int f = 10;

			while (d > 9)
			{
				int m = (n%d)*f + n/d;
				if (m >= a && m <= b && m > n)
				{
					adj.insert(m);
				}
				d/=10;
				f*=10;
			}
			res += adj.size();
		}
		cout << "Case #" << T << ": " << res << endl;
	}
}	