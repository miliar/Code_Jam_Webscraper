#include <iostream>
#include <fstream>
#include <algorithm>
#include <iomanip>
#include <vector>

using namespace std;

ifstream in("small.in");
ofstream out("small.out");

int s[1100];

vector <int> v[2200000];

int main()
{
	int test, t;
	int i,n,j,k;
	in >> test;
	for (t = 1; t <= test; ++t)
	{
		for (i = 0 ; i < 2200000; ++i)
			v[i].clear();
		in >> n;		
		for (i = 0 ; i < n; ++i)
		{
			in >> s[i];
		}
		for (int x = 0; x < (1 << n); ++x)
		{
			int ans = 0;
			for (i = 0; i < n; ++i)
				if (x & (1 << i))
					ans += s[i];
			v[ans].push_back(x);
		}

		bool f = true;
		int ans1, ans2;

		for (i = 0 ; i < 2200000 && f; ++i)
			if (v[i].size() > 1)
			{
				for (j = 0; j < v[i].size() && f; ++j)
					for (k = j + 1; k < v[i].size() && f; ++k)
						if ((v[i][j] & v[i][k]) == 0)
						{
							f = false;
							ans1 = v[i][j];
							ans2 = v[i][k];
						}
			}

		out << "Case #" << t << ":" << endl;
		for (i = 0 ; i < n; ++i)
			if (ans1 & (1 << i))
				out << s[i] << " ";
		out << endl;
		for (i = 0 ; i < n; ++i)
			if (ans2 & (1 << i))
				out << s[i] << " ";
		out << endl;


	}
	return 0;
}