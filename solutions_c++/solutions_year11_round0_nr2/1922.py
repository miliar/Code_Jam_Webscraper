#include <iostream>
#include <cstring>
#include <vector>
using namespace std;
int main()
{
	int t;
	cin >> t;
	for (int i = 1; i <= t; ++i)
	{
		int cmb[26][26];
		memset(cmb, 0xff, sizeof(cmb));
		bool opp[26][26] = {false};
		int c, d, n;
		cin >> c;
		for (int j = 0; j < c; ++j)
		{
			char str[4];
			cin >> str;
			int a = str[0] - 'A', b = str[1] - 'A';
			cmb[a][b] = cmb[b][a] = str[2] - 'A';
		}
		cin >> d;
		for (int j = 0; j < d; ++j)
		{
			char str[3];
			cin >> str;
			int a = str[0] - 'A', b = str[1] - 'A';
			opp[a][b] = opp[b][a] = true;
		}
		cin >> n;
		char str[128]; // max 100
		cin >> str;
		vector<char> res;
		for (int j = 0; j < n; ++j)
		{
			int a = str[j] - 'A';
			if (res.empty()) res.push_back(a);
			else
			{
				int cmbv = cmb[res.back()][a];
				if (cmbv != -1)
				{
					res.pop_back();
					res.push_back(cmbv);
				}
				else
				{
					bool cleared = false;
					for (int k = 0; k != res.size(); ++k)
					{
						if (opp[res[k]][a])
						{
							res.clear();
							cleared = true;
							break;
						}
					}
					if (!cleared) res.push_back(a);
				}
			}
		}
		cout << "Case #" << i << ": [";
		for (int k = 0; k != res.size(); ++k)
		{
			cout << (char)(res[k] + 'A');
			if (k != res.size() - 1) cout << ", ";
		}
		cout << "]" << endl;
	}
	return 0;
}