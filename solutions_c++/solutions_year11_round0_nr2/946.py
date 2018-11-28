#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main()
{
	freopen("input.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for(int tc = 0; tc < t; tc++)
	{
		int n, m, x;
		cin >> n;
		vector <string> a(n), b;
		for(int i = 0; i < n; i++)
			cin >> a[i];
		cin >> m;
		b.resize(m);
		for(int i = 0; i < m; i++)
			cin >> b[i];
		string s, t;
		cin >> x;
		cin >> s;
		for(int i = 0; i < s.length(); i++)
		{
			t.push_back(s[i]);
			while(t.size() > 1)
			{
				bool ok = false;
				int p = t.length() - 1;
				for(int i = 0; i < n; i++)
					if(t[p - 1] == a[i][0] && t[p] == a[i][1] || t[p - 1] == a[i][1] && t[p] == a[i][0])
					{
						t.pop_back();
						t.pop_back();
						t.push_back(a[i][2]);
						ok = true;
						break;
					}
				if(!ok)
					break;
			}
			int p = t.length() - 1;
			for(int j = 0; j < p; j++)
			{
				bool ok = false;
				for(int k = 0; k < m; k++)
					if(t[j] == b[k][0] && t[p] == b[k][1] || t[j] == b[k][1] && t[p] == b[k][0])
					{
						ok = true;
						break;
					}
				if(ok)
				{
					t.clear();
					break;
				}
			}
		}
		string ans = "[";
		for(int i = 0; i < t.length(); i++)
		{
			ans.push_back(t[i]);
			if(i != t.length() - 1)
				ans += ", ";
		}
		ans += "]";
		printf("Case #%d: ", tc + 1);
		cout << ans << endl;
	}
	return 0;
}