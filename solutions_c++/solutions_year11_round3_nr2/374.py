#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

#define int long long

using namespace std;

const int MAX = 1000;

int a[MAX];

vector<int> m;

main()
{
	ofstream fout ("B-large.out");
	ifstream fin ("B-large.in");

	int t0, tt;
	fin >> t0;
	tt = t0;
	while(t0 --> 0)
	{
		m.clear();
		int l, t, n, c;
		fin >> l >> t >> n >> c;
		for(int i = 0; i < c; i++)
			fin >> a[i];
		int ans = 0;
		bool b = true;
		for(int i = 0; i < n; i++)
		{
			ans += 2 * a[i % c];
			if(ans > t)
			{
				if(b && ans != t)
				{
					m.push_back((ans - t) / 2);
					b = false;
				}
				else
					m.push_back(a[i % c]);
			}
		}
		sort(m.begin(), m.end());
		for(int i = 0; i < l && m.size() - i; i++)
			ans -= m[m.size() - i - 1];
		fout << "Case #" << tt - t0 << ": " << ans << endl;
	}
	return 0;
}
