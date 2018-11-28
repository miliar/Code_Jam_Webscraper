#include <iostream>
#include <cstdio>
#include <map>
#include <set>
#include <string>
#include <vector>
#include <memory.h>

using namespace std;

map<char, char> o;
map<pair<char, char>, char> cm;
int z[1005];

void solve(int TCase, string s)
{
	memset(z, 0, sizeof(z));
	vector<char> ans;
	ans.push_back(s[0]);
	z[(int)s[0]] = 1;
	for (int i = 1; i < (int)s.size(); ++i)
	{
		int l = ans.size() - 1;
		if (cm.find(make_pair(ans[l], s[i])) != cm.end())
		{
			z[(int)ans[l]]--;
			ans.pop_back();
			ans.push_back(cm[make_pair(ans[l], s[i])]);
			z[(int)ans[ans.size() - 1]]++;
		} else
		if (cm.find(make_pair(s[i], ans[l])) != cm.end())
		{
			z[(int)ans[l]]--;
			ans.pop_back();
			ans.push_back(cm[make_pair(s[i], ans[l])]);
			z[(int)ans[ans.size() - 1]]++;
		} else
		{
			if (z[(int)o[s[i]]] != 0)
			{
				memset(z, 0, sizeof(z));
				ans.clear();
			}
			else
			{
				ans.push_back(s[i]);
				z[(int)s[i]]++;
			}
		}
	}
	
//	cout << "Case #" << TCase + 1 << ": [";
	printf("Case #%d: [", TCase + 1);
	for (int i = 0; i < (int)ans.size() - 1; ++i)
		printf("%c, ", ans[i]);
//		cout << ans[i] << ", ";
//	cout << ans[ans.size() - 1] << "]";
	if (ans.size() != 0)
		printf("%c]\n", ans[ans.size() - 1]);
	else
		printf("]\n");
	
}

int main()
{
	freopen("input","r",stdin);
	freopen("output","w",stdout);
	int T;
	cin >> T;
	for (int i = 0; i < T; ++i)
	{
		o.clear();
		cm.clear();
		int c;
		cin >> c;
		for (int j = 0; j < c; ++j)
		{
			char c1, c2, c3;
			cin >> c1 >> c2 >> c3;
			cm[make_pair(c1, c2)] = c3;
			cm[make_pair(c2, c1)] = c3;
		}
		int d;
		cin >> d;
		for (int j = 0; j < d; ++j)
		{
			char c1, c2;
			cin >> c1 >> c2;
			o[c1] = c2;
			o[c2] = c1;
		}
		int n;
		cin >> n;
		string s;
		cin >> s;
		solve(i, s);
//		if (i != T - 1)
//			cout << endl;
	}
	cerr << (char)93 << endl;
}
