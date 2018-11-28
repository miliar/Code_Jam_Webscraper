#include <iostream>
#include <stack>
#include <set>
#include <string>
#include <vector>

using namespace std;

set <string> arr;
set <string> now;

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int l, d, n;
	cin >> l >> d >> n;
	for(int i = 0; i < d; i++)
	{
		string s;
		cin >> s;
		arr.insert(s);
	}
	for(int i = 0; i < n; i++)
	{
		string p;
		cin >> p;
		now = arr;
		int c = 0;
		for(int j = 0; j < l; j++)
		{
			stack <string> st;
			vector <char> sym;
			if(p[c] == '(')
			{
				c++;
				while(p[c] != ')')
					sym.push_back(p[c++]);
				c++;
			}
			else
				sym.push_back(p[c++]);
			for(set <string>::iterator it = now.begin(); it != now.end(); it++)
				for(int k = 0; k < sym.size(); k++)
					if((*it)[j] == sym[k])
						st.push(*it);
			now.clear();
			while(!st.empty())
			{
				now.insert(st.top());
				st.pop();
			}
		}
		printf("Case #%d: %d\n", i + 1, now.size());
	}
	return 0;
}