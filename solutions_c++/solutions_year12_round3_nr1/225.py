#include <iostream>
#include <fstream>
#include <cmath>
#include <string>
#include <algorithm>
#include <queue>


using namespace std;

ifstream in("large.in");
ofstream out("large.out");

vector <int> v[1100];

int n;

int s[1100];

bool solve()
{
	int i,j;

	for (i = 0 ; i < n; ++i)
		s[i] = -1;

	queue <int> q;

	int k = 0;

	for (i = 0; i < n; ++i)
		//if (s[i] == -1)
		{
			for (j = 0 ; j < n; ++j)
				s[j] = -1;

			q.push(i);
			++k;
			s[i] = k;
			while (!q.empty())
			{
				int t = q.front();
				q.pop();
				for (j = 0; j < v[t].size(); ++j)
					if (s[v[t][j]] == -1)
					{
						s[v[t][j]] = k;
						q.push(v[t][j]);
					}
					else
						return true;
			}			
		}

	return false;


}

int main()
{
	int test,t,i,j;

	in >> test;
	
	for (t = 1; t <= test; ++t)
	{
		for (i = 0 ; i < 1100; ++i)
			v[i].clear();

		in >> n;

		for (i = 0 ; i < n; ++i)
		{
			int m, k;
			in >> m;
			for (j = 0 ; j < m; ++j)
			{
				in >> k;
				v[i].push_back(k - 1);
			}
		}

		bool f = solve();

		if (!f)
			out << "Case #" << t << ": No" << endl;
		else
			out << "Case #" << t << ": Yes" << endl;

	}

	return 0;
}