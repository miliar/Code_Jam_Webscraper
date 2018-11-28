#include <iostream>
#include <cstdio>
#include <cmath>
#include <string>
#include <vector>

using namespace std;

char g[255][255];
vector <char> g2[255];

inline string format(string s)
{
	string r = "[";
	for (int i = 0, l = s.size(); i < l; ++i)
	{
		r += s[i];
		if (i + 1 < l) r += ", ";
	}
	r += "]";
	return r;
}

int main()
{
	freopen("input","r",stdin);
	freopen("output","w",stdout);
	int tt;
	scanf("%d", &tt);
	for (int t = 0; t < tt; ++t)
	{
		memset(g, 0, sizeof(g));
		for (int i = 0; i < 255; ++i)
			g2[i].clear();
			
		int c, d, n;
		scanf("%d", &c);
		for (int i = 0; i < c; ++i)
		{
			char ch[10];
			scanf("%s", ch);
			g[ch[0]][ch[1]] = ch[2];
			g[ch[1]][ch[0]] = ch[2];
		}
		scanf("%d", &d);
		for (int i = 0; i < d; ++i)
		{
			char ch[10];
			scanf("%s", ch);
			g2[ch[0]].push_back(ch[1]);
			g2[ch[1]].push_back(ch[0]);
		}
		char cc[101];
		scanf("%*d%s", cc);
		string s = cc;
		string ans = "";
		for (int i = 0, l = s.size(); i < l; ++i)
		{
			if (ans.size() > 0 && g[s[i]][ans[ans.size() - 1]] > 0)
				ans[ans.size() - 1] = g[s[i]][ans[ans.size() - 1]];
			else if (ans.size() > 0 && g2[s[i]].size() > 0)
			{
				bool z = 0;							
				for (int j = ans.size() - 1; j >= 0 && !z; --j)
				{
					for (int k = 0; k < g2[s[i]].size(); ++k)
						if (ans[j] == g2[s[i]][k]) z = 1;
				}
				if (!z)
					ans += s[i];
				else
					ans = "";
			}
			else
				ans += s[i];
		}
		printf("Case #%d: %s\n", t + 1, format(ans).c_str());
	}
	return 0;
}
