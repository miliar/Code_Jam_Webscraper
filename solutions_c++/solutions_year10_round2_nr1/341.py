#include <vector>
#include <list>
#include <map>
#include <set>
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
#include <iomanip>
#include <climits>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
 
using namespace std;
 
#define Long long long

int main()
{
	freopen("data.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	int t, n, m;
	cin >> t;

	
	for (int x=1; x<=t; x++)
	{
		cin >> n >> m;
		
		set<string> have;
		for (int i=0; i<n; i++)
		{
			string str;
			cin >> str;
			
			str = str.substr(1) + "/";
			for (int j=0; j<str.length(); j++)
				if (str[j] == '/')
					have.insert(str.substr(0,j));	
		}
		
		int c = 0;		
		for (int i=0; i<m; i++)
		{
			string str;
			cin >> str;
			
			str = str.substr(1) + "/";
			for (int j=0; j<str.length(); j++)
				if (str[j] == '/')
				{
					string ss = str.substr(0,j);	
					if (have.find(ss) == have.end())
					{
						c++;
						//cout << ss << endl;
						have.insert(ss);
					}
				}
		}
		

		printf("Case #%d: %d\n", x, c);	
	}
		
}