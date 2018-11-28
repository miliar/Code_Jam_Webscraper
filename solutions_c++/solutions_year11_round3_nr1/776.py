# include <iostream>
# include <string>
# include <fstream>
# include <vector>
using namespace std;

int main()
{
	ifstream cin("CA.in");
	ofstream cout("CA.out");
	int t = 0;
	cin >> t;
	int casenum = 0;
	while(t - casenum)
	{
		bool ans = false;
		int n, m;
		cin >> n >> m;
		vector<string> s(n);
		for(int i = 0; i < n; ++i)
			cin >> s[i];

		int i = 0;
		for(; i < n; ++i)
		{
			int j = 0;
			for(; j < m; ++j)
				if(s[i][j] == '#')
				{
					if(j < m - 1 && i < n - 1 && s[i][j + 1] == s[i][j] && s[i + 1][j] == s[i][j] && s[i + 1][j + 1] == s[i][j])
					{
						s[i][j] = '/';
						s[i][j + 1] = '\\';
						s[i + 1][j] = '\\';
						s[i + 1][j + 1] = '/';
					}
					else
						break;
				}
			if(j != m)
				break;
		}
		if(i == n)
			ans = true;

		casenum++;
		cout << "Case #" << casenum << ":" << endl;
		if(!ans)
			cout << "Impossible" << endl;
		else
			for(int i = 0; i < n; ++i)
				cout << s[i] << "\n";
	}
	return 0;
}
