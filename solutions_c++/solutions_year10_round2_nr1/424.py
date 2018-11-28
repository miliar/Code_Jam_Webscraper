#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cstring>

using namespace std;

vector< string > d;

bool check(string p)
{
	for (int i = 0; i < d.size(); ++i)
		if (d[i] == p) return true;
	return false;
}

int main()
{
	int nTests;
	int n, m;
	string path;
	cin >> nTests;
	for (int run = 1; run <= nTests; ++run)
	{
		cin >> n >> m;
		d.clear();
		for (int i = 0; i < n; ++i)
		{
			string path;
			string x = "";
			cin >> path;
			int j = 0;
			while (j < path.length())
			{
				if (path[j] == '/') 
				{
					if (x != "") d.push_back(x);
				}
				x += path[j++];
			}
			if (x != "/") d.push_back(x);
		}
		int dem = 0;
		for (int i = 0; i < m; ++i)
		{
			string path;
			cin >> path;
			int j = 0;
			string x;			
			while (j < path.length())
			{
				if (path[j] == '/') 
				{
					if (x != "") 
					{
						if (!check(x))
						{
							++dem;
							d.push_back(x);
						}
					}
				}
				x += path[j++];
			}
			if (x != "/") 
				if (!check(x))
				{
					++dem;
					d.push_back(x);
				}
		}
		cout << "Case #" << run << ": " << dem << endl;
	}
	return 0;
}
