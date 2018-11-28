#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int f(const vector<string>& vs, const string& s)
{
	int i, maxi = -1;

	for (i = 0; i < vs.size(); i++)
	{
		if (vs[i].size() <= s.size() && s.substr(0, vs[i].size()) == vs[i])
			if (maxi == -1 || vs[i].size() > vs[maxi].size())
				maxi = i;
	}

	return maxi;
}

int main()
{
	int t, i, m, n, j, mkdir;
	vector<string> already, tobe;

	cin >> t;
	for (i = 0; i < t; i++)
	{
		cin >> n >> m;
		already.resize(n);
		tobe.resize(m);

		for (j = 0; j < n; j++)
			cin >> already[j];
		for (j = 0; j < m; j++)
			cin >> tobe[j];
		already.push_back("/");

		mkdir = 0;
		for (j = 0; j < tobe.size(); j++)
		{
			if (find(already.begin(), already.end(), tobe[j]) == already.end())
			{
				int x = f(already, tobe[j]);
				if (x == -1)
				{
					mkdir = -1;
					break;
				}

				int y = already[x].size();
				string making = already[x];

				while(y < tobe[j].size())
				{
					if (tobe[j][y] == '/')
					{
						y++;
						continue;
					}
					int z = tobe[j].find('/', y);
					if (z == string::npos)
						z = tobe[j].size();
					if (z != string::npos)
					{
						string n = tobe[j].substr(y, z-y);
						if (making[making.size()-1] != '/')
							making += "/";
						making += n;
						mkdir++;
						already.push_back(making);

						y = z+1;
					}
				}
			}
		}

		cout << "Case #" << i+1 << ": " << mkdir << endl;
	}

	return 0;
}
