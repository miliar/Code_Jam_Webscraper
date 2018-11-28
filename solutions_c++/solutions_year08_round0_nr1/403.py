#include <iostream>
#include <string>
#include <map>
using namespace std;

int n, m;
map<string, int> save;
int chk[120];

int main()
{
	int t;
	int i, j;

	freopen("A.txt", "w", stdout);
	freopen("A-large.in", "r", stdin);

	cin >> t;
	for(int loop=1; loop<=t; loop++)
	{
		save.clear();
		fill(chk, chk+20, 0);
		cin >> n;

		string s;
		getline(cin, s);
		for(i=0; i<n; i++)
		{
			getline(cin, s);
			save[s] = i+1;
		}

		int res = 0;
		cin >> m;
		getline(cin, s);

		int cnt = 0;
		for(i=0; i<m; i++)
		{
			string word;
			getline(cin, word);
			int c = save[word];
			if(chk[c]) continue;
			else
			{
				cnt++;
				chk[c] = 1;
			}
			if(cnt==n)
			{
				for(j=1; j<=n; j++)
				{
					chk[j] = 0;
				}
				chk[c] = 1;
				res++;
				cnt = 1;
			}
		}
		cout << "Case #" << loop << ": " << res << endl;
	}

	return 0;
}