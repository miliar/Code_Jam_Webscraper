#include <cstdio>
#include <iostream>
#include <vector>

#define PB push_back

using namespace std;

vector< int > go;

int main()
{
	freopen("c.in", "rt", stdin);
	freopen("c.out", "wt", stdout);

	int t, n, r, w, T, f, it;
	int m = 100003;
	cin >> t;
	for (int i = 1; i <= t; i++)
	{
		cin >> n;
		if (n == 2) r = 1;
		else
		{
			r = 1;
			for (int j = 1; j < (1 << (n-2)); j++)
			{
				go.resize(0);
				w = j; T = 2;
				while (w > 0)
				{
					if (w % 2 == 1) go.PB(T);
					w /= 2; T++;
				}
				//cerr << endl;
				//for (int k = 0; k < go.size(); k++) cerr << go[k] << ' ';
				f = go.size()+1;
				it = go.size()-1;
				while (it >= 0)
				{
					if (go[it] == f) f = it+1;
					it--;
				}
				if (f == 1)
				{
					r++;
					if (r > m) r -= m;
				}
			}
			cout << "Case #" << i << ": " << r << endl;
		}
	}

	return 0;
}
