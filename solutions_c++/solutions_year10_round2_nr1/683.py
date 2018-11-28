#include <iostream>
#include <fstream>
#include <string>
#include <set>

using namespace std;

void decompose(string& str, set<string>& paths, int& cnt, bool init)
{
	string t;
	for(int i=0; i<str.size(); ++i)
	{
		if (str[i]=='/' || i==str.size()-1)
		{
			t = string(str,0,i+1);
			if (i==str.size()-1)
				t += "/";
			//cout << t << endl;
			if (init)
				paths.insert(t);
			else
			{
				if (paths.find(t) == paths.end())
				{
					cnt++;
					paths.insert(t);					
				}
			}
		}
	}		
}

void iter(int ind)
{
   	int n,m;
	cin >> n >> m;

	set<string> paths;
	paths.insert("/");

	int cnt = 0;

	for(int i=0; i<n; ++i)
	{
		string str;
		cin >> str;
		decompose(str, paths, cnt, true);
	}

	for(int i=0; i<m; ++i)
	{
		string str;
		cin >> str;
		decompose(str, paths, cnt, false);		
	}

	cout << "Case #" << ind << ": " << cnt << endl;	
}

int main()
{
	int t;
	cin >> t;

	for(int i=0; i<t; ++i)
		iter(i+1);

	return 0;
}
