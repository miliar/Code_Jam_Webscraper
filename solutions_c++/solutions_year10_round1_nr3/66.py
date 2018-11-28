#include <iostream>
#include <cstdio>
#include <vector>
#include <string.h>
#include <algorithm>
using namespace std;
const int N = 100, A = 256, INF = 10000000;
typedef long long int LL;
int t, a1, a2, b1, b2, L, P, m, b, e;
LL ans;
bool win(int x, int y)
{
	if(x < y)
		swap(x, y);
	if(x >= 2 * y)
		return true;
	if(y == 0)
		return true;
	return !win(y, x - y);
}

int main()
{
	int i, j, k;
	cin >> t;
	for(int testCase = 1; testCase <= t; ++testCase)
	{
		ans = 0;
		cin >> a1 >> a2 >> b1 >> b2;
		for(i = a1; i <= a2; ++i)
		{
			//cout << i << endl;
		//	ans += max(i / 2 - b1 + 1, 0);
		//	ans += max(b2 - 2 * i + 1, 0);
			//for(j = max(b1, i / 2 + 1); j <= min(b2, 2 * i - 1) ; ++j)
		//	cout << i << endl;
			L = 0, P = i;
			while(L < P)
			{
				m = (L + P) / 2;
		//		cout << L << P << m << endl;
				if(win(i, m))
					L = m + 1;
				else
					P = m;
			}
			b = L;
			L = i, P = INF;
			while(L < P)
			{
				m = (L + P + 1) / 2;
		//		cout << L << P << m << endl;
				if(win(i, m))
					P = m - 1;
				else
					L = m;
			}
			e = L;
		//	cout << i << " " << b << " " << e << endl;
			b = max(b, b1);
			e = min(e, b2);
		//	cout << i << " " << b << " " << e << endl;
			ans += LL(b2 - b1 + 1) - LL(max(0, e - b + 1));
		}
		cout << "Case #" << testCase << ": " << ans << endl;
	}
}
/*
1
1 1000000
1 1000000
*/
