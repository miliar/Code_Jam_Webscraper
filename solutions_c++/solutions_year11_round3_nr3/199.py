#include<iostream>
#include<string>
#include<fstream>
#include<cmath>
#include<vector>
#include<cstdio>
#include<algorithm>
using namespace std;


int main()
{
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small-attempt0.out", "w", stdout);

	int t;
	cin >> t;
	for(int test = 1; test <= t; test++)
	{
		int n, l, h;
		cin >> n >> l >> h;
		vector<int> v(n);
		for(int i = 0; i < n; i++)
			cin >> v[i];

		int res = -1;
		for(int c = l; res == -1 && c <= h; c++)
		{
			bool ok = true;
			for(int i = 0; ok && i < n; i++)
				if(!(c % v[i] == 0 || v[i] % c == 0))
					ok = false;
			if(ok)
				res = c;
		}

		if(res == -1)
			cout << "Case #" << test << ": NO" << endl;
		else
		{
			cout << "Case #" << test << ": " << res << endl;
		}



	}





	return 0;
}