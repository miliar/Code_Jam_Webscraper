#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <sstream>
using namespace std;

int main ()
{
	int t;
	cin >> t;

	for (int T = 1; T <= t; T++)
	{
		cout << "Case #" << T << ": ";
		int n,m;
		cin >> n >> m;

		map <string, bool> ma;
		string dic;
		for (int i = 0; i < n; i++)
		{
			cin >> dic;
			if (dic == "/") continue;
			for (int j = 0; j < dic.size(); j++)
			{
				if (dic[j] == '/') dic[j] = ' ';
			}
			stringstream ss(dic);
			string s;
			string path;
			while (ss >> s)
			{
				path += " " + s;
				if (ma.find(path) == ma.end()) ma[path] = true;
			}
		}
		int c = 0;
		for (int i = 0; i < m; i++)
		{
			cin >> dic;
			if (dic == "/") continue;
			for (int j = 0; j < dic.size(); j++)
			{
				if (dic[j] == '/') dic[j] = ' ';
			}
			stringstream ss(dic);
			string s;
			string path;
			while (ss >> s)
			{
				path += " " + s;
				if (ma.find(path) == ma.end()) { ma[path] = true; c++; }
			}
		}
		cout << c << "\n";
	}

	return 0;
}
