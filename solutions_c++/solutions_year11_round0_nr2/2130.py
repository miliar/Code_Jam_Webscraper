#include <iostream>
#include <cstdio>
#include <vector>
#include <cstring>

using namespace std;

int m[26][26];
bool o[26][26];
vector<int> ans;

void check()
{
	for(int i=0; i<ans.size(); i++)
		for(int j=0; j<ans.size(); j++)
			if(o[ans[i]][ans[j]])
				ans.clear();
}

int main()
{
	int t;
	cin >> t;
	for(int T=1; T<=t; T++)
	{
		ans.clear();
		memset(m, -1, sizeof m);
		memset(o, 0, sizeof o);
		int c, d;
		cin >> c;
		while(c--)
		{
			char p, q, r;
			cin >> p >> q >> r;
			m[p-'A'][q-'A'] = r-'A';
			m[q-'A'][p-'A'] = r-'A';
		}
		cin >> d;
		while(d--)
		{
			char p, q;
			cin >> p >> q;
			o[p-'A'][q-'A'] = true;
		}

		int n;
		cin >> n;
		while(n--)
		{
			char tc;
			cin >> tc;
			tc -= 'A';
			ans.push_back(tc);
			while(ans.size() >= 2)
			{
				int l1 = ans[ans.size()-2], l2 = ans.back();
				if(m[l1][l2] != -1)
				{
					ans.pop_back();
					ans.pop_back();
					ans.push_back(m[l1][l2]);
				}
				else
					break;
			}
			check();
		}
		cout << "Case #" << T << ": [";
		for(int i=0; i<ans.size(); i++)
		{
			if(i)
				cout << ", ";
			cout << char(ans[i]+'A');
		}
		cout << "]" << endl;
	}
	return 0;
}

