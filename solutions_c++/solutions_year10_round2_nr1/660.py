#include<cstdio>
#include <vector>
#include <string>
#include <iostream>
#include <map>
#include <algorithm>
#include <set>
#include <iostream>
#include <cmath>
#include <ctime>
using namespace std;

#define PB push_back
#define MP make_pair
#define X first
#define Y second
#define PII pair<int,int> 

int main() 
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t; cin >> t;
	for (int q=1; q<=t; q++)
	{
		set<string> ss;
		int cnt = 0;
		int a, b; cin >> a  >> b;
		for (int w=0; w < a; w++)
		{
			string s; cin >> s;
			ss.insert(s);
			for (int i=1; i < s.size(); i++)
			{
				if (s[i] == '/')
				{
					string sub =  s.substr(0, i);
		
					ss.insert(sub);
				}
			}
		}
		for (int w=0; w < b; w++)
		{
			string s; cin >> s;
			for (int i=1; i < s.size(); i++)
			{
				if (s[i] == '/')
				{
					string sub =  s.substr(0, i);
					if (ss.count(sub) == 0) cnt++;
					ss.insert(sub);
				}
			}
			if (ss.count(s) == 0) cnt++;
			ss.insert(s);
		}
		cout << "Case #" << q<<": " << cnt<<endl;
	}
	return 0;
}