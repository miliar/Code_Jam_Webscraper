#include <cstdio>
#include <iostream>
#include <map>
#include <vector>
#include <string>
#include <list>
#include <ctype.h>
#include <math.h>
#include <string.h>
#include <algorithm>
using namespace std;

const double EPS = 1e-9;

int main()
{
	int t;
	freopen("test.in", "a+", stdin);
	freopen("test.out", "w", stdout);
	cin >> t;
	int l, c, p;
	for (int k = 0; k < t; ++k)
	{
		cout << "Case #" << k+1 << ": ";
		cin >> l >> p >> c;
		if (l * c >= p)
		{
			cout << 0 << endl;
			continue;
		}
		//p += 1;
		int cnt = 0;
		double temp = (double)p / double(c*l);
		double up = log10(temp);
		double down = log10((double)c);
		double r = up / down;
		r += 1;
		//cout << r << endl;
		while (r > 1)
		{
			++cnt;
			r /= 2;
		}
		//printf("%.0lf\n", r); 
		cout << cnt << endl;
	}
	return 0;
}