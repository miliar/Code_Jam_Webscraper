#include <map>
#include <set>
#include <vector>
#include <algorithm>
#include <iostream>
#include <cmath>
using namespace std;

typedef pair<int, int> pii;
#define MP(x, y) make_pair(x, y)

int doit(int a, int b)
{
	set<pii> s;
	for (int i = a; i < b; i++)
	{
		int l = log10(i);
		if (l == 0) return 0;

		int k = i;
		for (int j = 0; j < l; j ++)
		{
			int c = k%10;
			c *= pow(10, l);
			k /= 10;
			c += k;
			k = c;

			//cout << i << ", " << c << endl;

			if (k >= a && k <= b && i != k && i < k)
			{
				//cout << i << ", " << k << endl;
				s.insert(MP(i, k));
			}
		}
	}
	return s.size();
}

int main(int argc, const char *argv[])
{
	int T;
	cin >> T;
	for (int i = 0; i < T; i ++)
	{
		int a, b;
		cin >> a >> b;
		cout << "Case #" << i+1 << ": " << doit(a, b) << endl;
	}
	return 0;
}
