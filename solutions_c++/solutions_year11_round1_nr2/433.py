#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

main ()
{
	int t;
	cin >> t;

	for (int T = 1; T <= t; T++)
	{
		int n,m;
		cin >> n >> m;

		vector <string> dict(n);
		for (int i = 0; i < n; i++) cin >> dict[i];

		//sort(dict.begin(),dict.end());
		string ans;

		for (int g = 0; g < m; g++)
		{
			string L;
			cin >> L;
			
			int max_loss = -1, index = -1;
			for (int i = 0; i < n; i++)
			{
				// my word is dict[i]
				// loss?
				vector <string> list;
				int pt = 0;
				for (int j = 0; j < n; j++) if (i != j && dict[i].size() == dict[j].size()) list.push_back(dict[j]);
				
				for (int j = 0; j < L.size(); j++)
				{
					vector <int> pos;
					for (int k = 0; k < dict[i].size(); k++) if (dict[i][k] == L[j]) pos.push_back(k);
					if (pos.size() == 0)
					{
						vector <string> new_list;
						for (int k = 0; k < list.size(); k++)
						{
							if (list[k].find(L[j]) != -1) { pt++; break; }
						}
						for (int k = 0; k < list.size(); k++)
						{
							if (list[k].find(L[j]) == -1) new_list.push_back(list[k]);
						}
						list = new_list;
					} else
					{
						vector <string> new_list;
						for (int k = 0; k < list.size(); k++)
						{
							vector <int> poss;
							for (int r = 0; r < list[k].size(); r++)
							{
								if (list[k][r] == L[j]) poss.push_back(r);
							}
							if (poss == pos) new_list.push_back(list[k]);
						}
						list = new_list;
					}
				}
				
				if (max_loss == -1 || max_loss < pt) { max_loss = pt; index = i; }
			}
			if (g < m-1) ans += dict[index] + " ";
			else ans += dict[index];
		}
		cout << "Case #" << T << ": " << ans << "\n";
	}
}
