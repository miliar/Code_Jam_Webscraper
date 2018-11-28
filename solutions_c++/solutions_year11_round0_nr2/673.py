#include <iostream>
#include <string>
#include <map>
#include <algorithm>
using namespace std;

string getList (string a)
{
	if (a.size() == 0) return "[]";
	string ret = "[";
	for (int i = 0; i < a.size()-1; i++) 
	{
		ret += a[i];
		ret += ", ";
	}
	ret += a[a.size()-1];
	ret += "]";
	return ret;
}

main()
{
	int t;
	cin >> t;

	for (int T = 1; T <= t; T++)
	{
		int c;
		cin >> c;

		map <string,char> combo;
		string s;
		for (int i = 0; i < c; i++)
		{
			cin >> s;
			string s1 = s.substr(0,2);
			combo[s1] = s[2];
			reverse(s1.begin(),s1.end());	
			combo[s1] = s[2];
		}

		int d;
		cin >> d;
		
		map < string, bool > opposed;
		for (int i = 0; i < d; i++)
		{
			cin >> s;
			opposed[s] = true;
			reverse(s.begin(),s.end());
			opposed[s] = true;
		}

		int n;
		cin >> n;

		string invoke;
		cin >> invoke;

		string final = "";
		final += invoke[0];
		for (int i = 1; i < n; i++)
		{
			final += invoke[i];
			if (final.size() == 1) continue;
			string sub = final.substr(final.size()-2);
			if (combo.find(sub) != combo.end())
			{
				final = final.substr(0,final.size()-2) + combo[sub];
			} else
			{
				for (int j = 0; j < final.size()-1; j++)
				{
					string tmp;
					tmp += final[j];
					tmp += invoke[i];
					if (opposed.find(tmp) != opposed.end())
					{
						final = "";
						break;
					}
				}
			}			
		}
		cout << "Case #" << T << ": " << getList(final) << "\n";
	}
}
