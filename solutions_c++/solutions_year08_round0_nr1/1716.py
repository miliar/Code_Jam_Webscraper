#include <iostream>
#include <string>
#include <set>
#include <cstdio>
using namespace std;
const int MAXC = 100+1;
char cstr[MAXC];
int main()
{
	int n;
	scanf("%d\n",&n);
	for (int a = 1; a <= n; ++a)
	{
		int s, q;
		string str;
		scanf("%d\n",&s);
		for (int i = 0; i < s; ++i)	{ cin.getline(cstr,MAXC); }
		scanf("%d\n",&q);
		int swp = 0;
		set<string> st;
		for (int j = 0; j < q; j++)
		{
			cin.getline(cstr,MAXC);
			str = string(cstr);
			if (st.find(str) == st.end())
			{
				if (st.size() == s-1)
				{
					swp++;
					st.clear();
				}
				st.insert(str);
			}
		}
		cout << "Case #" << a << ": " << swp << endl;
		st.clear();
	}
	return 0;
}
