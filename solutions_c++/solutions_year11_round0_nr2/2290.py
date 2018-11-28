#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>

using namespace std;

int
main()
{
	freopen("1.IN", "r", stdin);
	freopen("B-small-attempt0.txt", "w", stdout);
	int t;
	cin >> t;
	for(int q = 0; q < t; ++q)
	{
		int c;
		cin >> c;
		map<string, char> a1;
		set<string> a2;
		for(int i = 0; i < c; ++i)
		{
			string str;
			cin >> str;
			string s;
			s+= str[0]; 
			s+= str[1];
			a2.insert(s);
			if(str.length() == 3)
			{
				a1[s] = str[2];
				s.clear();
				s += str[1];
				s += str[0];
				a1[s] = str[2];
			}
			else
			{
				a1[s] = '0';
				s.clear();
				s += str[1];
				s += str[0];
				a1[s] = '0';
			}
			a2.insert(s);
		}
		int d;
		cin >> d;
		set<string> b;
		for(int i = 0; i < d; ++i)
		{
			string str;
			cin >> str;
			b.insert(str);
			string s;
			s += str[1];
			s += str[0];
			b.insert(s);
		}
		int n;
		cin >> n;
		vector <char> ans;
		
		for(int i = 0; i < n; ++i)
		{
			char sym;
			cin >> sym;
			ans.push_back(sym);
			if(ans.size() > 1)
			{
				string s;
				s += ans[ans.size() - 2];
				s += ans[ans.size() - 1];
				if(a2.find(s) != a2.end())
				{
					ans[ans.size() - 2] = '0';
					ans[ans.size() - 1] = a1[s];
				}
				else
				{
					for(int w = 0; w < ans.size(); ++w)
					{
						for(int v = w + 1; v < ans.size(); ++v)
						{
							s.clear();
							s += ans[w];
							s += ans[v];
							if(b.find(s) != b.end())
							{
								ans.resize(0);
								break;
							}
						}
					}
				}
			}
		}
		bool f = false;
		cout << "Case #" <<q + 1 <<": [";
		for(int i = 0; i < ans.size(); ++i)
		{
			if(ans[i] != '0')
			{
				if(f == false)
				{
					cout << ans[i];
					f = true;
				}
				else
				{
					cout <<", "<<ans[i];
				}				
			}
		}
		cout <<']'<<endl;
	}
	return 0;
}