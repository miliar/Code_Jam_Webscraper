#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("answer.txt", "w", stdout);
	int tc;
	cin>>tc;
	for(int Case = 0; Case < tc; Case++)
	{
		int c, d;
		string str;
		map<string, char> mc;
		map<char, set<char> > md;
		cin >> c;
		for(int i = 0; i < c; ++i)
		{
			cin >> str;
			string c1 = str.substr(0,1);
			string c2 = str.substr(1,1);
			mc[c1+c2] = str[2];
			mc[c2+c1] = str[2];
		}
		cin >> d;
		for(int i = 0; i < d; ++i)
		{
			cin >> str;
			md[str[0]].insert(str[1]);
			md[str[1]].insert(str[0]);
		}
		deque<char> dq;
		int n;
		cin >> n;
		for(int i = 0; i< n; ++i)
		{
			string str(2, 0);
			cin >> str[0];
			if(dq.empty())
				dq.push_back(str[0]);
			else
			{
				str[1] = dq.back();
				if(mc.find(str) != mc.end())
				{
					dq.pop_back();
					dq.push_back(mc[str]);
				}
				else
				{
					bool clear = false;
					for(deque<char>::iterator it = dq.begin(); it != dq.end(); ++it)
					{
						if(md[str[0]].find(*it) != md[str[0]].end())
						{
							dq.clear();
							clear = true;
							break;
						}
					}
					if(!clear)
						dq.push_back(str[0]);
				}
			}
		}
		string ans;
		for(deque<char>::iterator it = dq.begin(); it != dq.end(); ++it)
		{
			ans += *it;
			ans += ", ";
		}
		if(!ans.empty())
			ans.resize(ans.length() - 2);
		cout << "Case #" << Case + 1 <<": [" << ans << "]" << endl;
	}

	return 0;
}
