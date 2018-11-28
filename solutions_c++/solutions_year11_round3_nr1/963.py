#include <iostream>
#include <vector>
#include <string>
using namespace std;

bool possible(const vector<string>& vs)
{
	for (int i = 0; i < vs.size(); i++)
	{
		for (int j = 0; j < vs[i].size(); j++)
			if (vs[i][j] == '#')
				return false;
	}

	return true;
}

vector<string> make(vector<string> vs)
{
	for (int i = 0; i < vs.size(); i++)
	{
		for (int j = 0; j < vs[i].size(); j++)
		{
			if (vs[i][j] == '#')
			{
				if (j+1 < vs[i].size() && vs[i][j+1] == '#')
					if (i+1 < vs.size() && vs[i+1][j] == '#')
						if (i+1 < vs.size() && j+1 < vs[i+1].size() && vs[i+1][j+1] == '#')
						{
							vs[i][j] = '/';
							vs[i][j+1] = '\\';
							vs[i+1][j] = '\\';
							vs[i+1][j+1] = '/';

							return make(vs);
						}
			}
		}
	}

	return vs;
}

int main()
{
	int r, c, i, t;

	cin >> t;
	for (i = 0; i < t; i++)
	{
		cin >> r >> c;
		vector<string> vs(r);
		for (int j = 0; j < r; j++)
			cin >> vs[j];

		vs = make(vs);
		cout << "Case #" << i+1 << ":\n";
		if (possible(vs))
		{
			for (int a = 0; a < vs.size(); a++)
			{
				for (int b = 0; b < vs[a].size(); b++)
				{
					cout << vs[a][b];
				}
				cout << endl;
			}
		}
		else
			cout << "Impossible\n";
	}

	return 0;
}
