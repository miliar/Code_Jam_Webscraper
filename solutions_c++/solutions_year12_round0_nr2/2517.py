#include <iostream>
#include <cstring>
#include <algorithm>
#include <vector>
using namespace std;

int main()
{
	//freopen("input.in", "r", stdin);
	//freopen("output.txt", "w", stdout);
	int T;
	cin >> T;
	for(int test = 1; test <= T; test++)
	{
		int n, s, p;
		cin >> n >> s >> p;
		vector<int> v(n);
		for(int i = 0; i < n; i++)
			cin >> v[i];

		int x[3];
		int res = 0;
		for(int i = 0; i < n; i++)
		{
			int d = v[i] / 3;
			int m = v[i] % 3;
			for(int j = 0; j < 3; j++)
				x[j] = d;
			for(int j = 0; j < m; j++)
				x[2 - j]++;
			if(x[2] >= p) res++;
			else if(p - x[2] > 1) continue;
			else if(x[2] == x[1] && s > 0 && v[i] > 0)
			{
				res++;
				s--;
			}
		}
		cout << "Case #" << test << ": " << res << endl;
	}
	return 0;
}