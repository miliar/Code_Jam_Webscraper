#include <iostream>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;



int main()
{
    freopen("a.in","rt",stdin);
    freopen("a.out","wt",stdout);
    
	int t,www = 1;
	cin >> t;
	int n,m;
	while(t--)
	{
		vector<string> v;
		cin >> n >> m;
		string s;
		for(int i = 0; i < n; i++)
		{
			cin >> s;
			s += "/";
			v.push_back(s);
		};
		int ans = 0;
		for(int i = 0; i < m; i++)
		{
			cin >> s;
			string q;
			for(int j = 0; j < s.size(); j++)
			{
				q += s[j];
				if((s[j] == '/' || j == s.size() - 1) && q != "/")
				{
					if(j == s.size() - 1)
						q += '/';
					int f = 0;
					for(int k = 0; k < v.size(); k++)
						if((int)v[k].find(q) == 0 && v[k][q.size() - 1] == '/')
							f = 1;
					if(f == 0)
					{
						ans++;
						v.push_back(q);
					}
				}
			}		
		}
		cout << "Case #"<< www++ <<": " << ans << endl;
	}


     return 0;
}
