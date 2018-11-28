#include <iostream>
#include <string>
#include <algorithm>
#include <set>

using namespace std;

int ind[10005], res[10005];
string str[10005], pat[10005];

int cmp (int a, int b)
{
	return pat[a] < pat[b];
}

int main()
{
  freopen("b.in", "r", stdin);
  freopen("b.out", "w", stdout);
  int T;
  cin >> T;
  for (int t = 1; t <= T; t++)
  {
    cout << "Case #" << t << ": ";
		int n, M;
		cin >> n >> M;
		for (int i = 0; i < n; i++)
		{
			cin >> str[i];
		}
		for (int m = 0; m < M; m++)
		{
			string lst;
			cin >> lst;
			for (int i = 0; i < n; i++)
			{
				ind[i] = i;
				pat[i] = str[i];
				res[i] = 0;
				for (int j = 0; j < pat[i].length(); j++)
					pat[i][j] = '!';
			}
			for (int p = 0; p < 26; p++)
			{
				set<string> s;
				sort(ind, ind + n, cmp);
				string cur = pat[0];
				int a = 0;
				int prev = 0;
				for (int i = 0; i < n; i++)
				{
					if (pat[ind[i]] != cur)
					{
						if (s.size() > 1)
						{
//							cerr << prev << i << endl;
							for (int k = prev; k < i; k++)
							{
								if (pat[ind[k]] == cur)
								{
									res[ind[k]]++;
//									cerr << ind[k] << " " << str[ind[k]] << ' ' << pat[ind[k]] << endl;
								}
							}
						}
						s.clear();
						prev = i;
						a = 0;
						cur = pat[ind[i]];
//						cerr << cur << endl;
					}
					for (int j = 0; j < pat[ind[i]].length(); j++)
						if (str[ind[i]][j] == lst[p])
							pat[ind[i]][j] = lst[p];
//					cerr << pat[ind[i]] << endl;
					if (s.find(pat[ind[i]]) == s.end())
						s.insert(pat[ind[i]]);
//						cerr << s.size() << endl;
				}
				if (s.size() > 1)
				{
					for (int k = prev; k < n; k++)
					{
						if (pat[ind[k]] == cur)
						{
							res[ind[k]]++;
//							cerr << ind[k] << " " << str[ind[k]] << ' ' << pat[ind[k]] << endl;
						}
					}
				}
			}
			int mx = -1;
			string ans;
			for (int i = 0; i < n; i++)
			{
				if (res[i] > mx)
				{
					ans = str[i];
					mx = res[i];
				}
			}
			cout << ans << " ";
		}
    cout << endl;
  }
  return 0;
}