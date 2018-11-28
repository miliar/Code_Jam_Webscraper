#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>

using namespace std;

char replac [200][200];
bool remov [200][200];


int main ()
{
	freopen("B-large.in","rt",stdin);
	freopen("B-large.out","wt",stdout);
	int t;
	cin >> t;

	for ( int tt = 1 ; tt <= t ; tt++)
	{
		memset(replac,0,sizeof(replac));
		memset(remov,0,sizeof(remov));

		int n;
		cin >> n;
		for ( int i = 0 ; i < n ; i ++ )
		{
			string s;
			cin >>s;
			replac[s[0]][s[1]] = s[2];
			replac[s[1]][s[0]] = s[2];
		}
		cin >> n;
		for ( int i = 0 ; i < n ; i ++ )
		{
			string s;
			cin >> s;
			remov[s[0]][s[1]] = 1;
			remov[s[1]][s[0]] = 1;
		}
		vector<char > res;

		string ss;
		cin >> n>> ss;


		for ( int i = 0 ; i < n ; i ++)
		{
			char g = ss[i], lst = 0;
			if ( res.size() )
				lst = res.back();

			if ( replac[g][lst]  )
				res.back() = replac [g][lst];
			else
			{
				bool flg = 0;
				for ( int j = 0 ; j < res.size(); j ++ )
				{
					if ( remov [g][res[j]] )
					{
						res.clear();
						flg = 1;
						break;
					}
				}
				if ( ! flg )
				{
					res.push_back(g);
				}
			}
		}
		cout << "Case #"<<tt<<": [";
		bool isf = 1;
		for ( int i = 0 ; i < res.size() ; i ++ )
		{
			if ( ! isf )
				cout << ", ";
			isf = 0;

			cout << res[i];

		}
		cout << "]\n";
	}
	return 0;
}
