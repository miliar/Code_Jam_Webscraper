#include <string>
#include <vector>
#include <iostream>
#include <cstdio>
#include <algorithm>

using namespace std;

int main()
{
	freopen ("b.in", "r", stdin);
	freopen ("b.out", "w", stdout);

	int t;
	cin >> t;

	for (int i = 0; i < t; i++)
	{
//		cout << i;
		int x,y,z;
		vector<string> G;
		vector<string> O;
		string L;
		string R;
		cin >> x;

		for (int j = 0; j < x; j++)
		{
			string str;
			cin >> str;
			G.push_back(str);
		}

		cin >> y;

		for (int j = 0; j < y; j++)
		{
			string str;
			cin >> str;
			sort(str.begin(), str.end());
			O.push_back(str);
		}

		sort(O.begin(), O.end());

		cin >> z;
		cin >> L;

		for (int j = 0; j < z; j++)
		{
			R.push_back(L[j]);
			while (R.size() > 1)
			{
//				cout << R;
				bool combine = false;

				for (int k = 0; k < x; k++)
					if (G[k][0] == R[R.size() - 1] && G[k][1] == R[R.size() - 2] ||
							G[k][1] == R[R.size() - 1] && G[k][0] == R[R.size() - 2])
					{
						R.resize(R.size() - 2);
						R.push_back(G[k][2]);
						combine = true;
						break;
					}

				if (!combine)
				{
					for (int p = 0; p < R.size(); p++)
						for (int q = p + 1; q < R.size(); q++)
						{
							string xx;
							xx.push_back(R[p]);
							xx.push_back(R[q]);
							sort(xx.begin(), xx.end());
							if (find(O.begin(), O.end(), xx) != O.end())
							{
								R.clear();
								break;
							}
						}

					break;
				}
			}
		}

		cout << "Case #" << i + 1 << ": [";
		for (int j = 0; j < R.size(); j++)
		{
			cout << R[j];
			if (j != R.size() - 1)
				cout << ", ";
		}

		cout << "]\n";
	}

	return 0;
}

