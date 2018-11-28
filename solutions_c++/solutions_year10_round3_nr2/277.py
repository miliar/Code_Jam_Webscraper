#include <iostream>
#include <algorithm>
#include <math.h>
using namespace std;
int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("out.out", "w", stdout);
	long long t, l, p ,c;
	cin >> t;
	for (int i = 1; i <= t; i++)
	{
		cin >> l >> p >> c;
		int k = 0;
		while (l * c < p)
		{
			l *= c;
			k++;
		}
		cout << "Case #" << i << ": " << ((k > 0) ? int(ceil(log(double(k + 1)) / log(2.0))) : 0) << endl;
	}
	
	return 0;
}