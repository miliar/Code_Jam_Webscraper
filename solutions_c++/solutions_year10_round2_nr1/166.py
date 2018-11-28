#include <iostream>
#include <string>
#include <set>
using namespace std;

int N, M, ans;
string S[105];
set<string> Dic;

void build(string s)
{
	string tmp = "";
	for (int i = 0; i < s.size(); i ++)
	{
		tmp += s[i];
		if (s[i] == '/') Dic.insert(tmp);
	}
}

void solve()
{
	string tmp;
	for (int i = 0; i < M; i ++)
	{
		tmp = "";
		for (int j = 0; j < S[i].size(); j ++)
		{
			tmp += S[i][j];
			if (S[i][j] == '/')
			{
				ans += (1- Dic.count(tmp));
				Dic.insert(tmp);
			}
		}
	}
}

void init()
{
	Dic.clear();
	Dic.insert("/");
	ans = 0;
	cin >> N >> M;
	string s;
	for (int i = 0; i < N; i ++)
	{
		cin >> s;
		s += '/';
		build(s);
	}
	for (int i = 0; i < M; i ++)
	{
		cin >> S[i];
		S[i] += '/';
	}
	sort(S, S + M);
}

int main()
{
	int T;
	cin >> T;
	for (int _T = 1; _T <= T; _T ++)
	{
		init();
		solve();
		printf("Case #%d: %d\n", _T, ans);
	}
}
