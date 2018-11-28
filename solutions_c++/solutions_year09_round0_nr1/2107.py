#include <iostream>
#include <string>
using namespace std;

const int L = 20;
const int D = 5050;
const int N = 500;

string word[D], patten[N];
int l, d, n, cnt;

bool match(string &s, int is, string &t, int it)
{
	if (is == s.length()) return true;
	if (t[it] != '(')
	{
		if (s[is] == t[it]) return match(s, is+1, t, it+1);
		else return false;
	}
	else
	{
		++it;
		bool flag = false;
		while (t[it] != ')')
		{
			if (s[is] == t[it]) flag = true;
			++it;
		}
		if (flag)
			return match(s, is+1, t, it+1);
		else
			return false;
	}
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	cin >> l >> d >> n;
	for (int i = 1; i <= d; ++i)
		cin >> word[i];
	for (int i = 1; i <= n; ++i)
		cin >> patten[i];

	for (int j = 1; j <= n; ++j)
	{
		cnt = 0;
		for (int i = 1; i <= d; ++i)
			if (match(word[i], 0, patten[j], 0))
				++cnt;
		cout << "Case #" << j << ": " << cnt << endl;
	}
	fclose(stdin);
	fclose(stdout);
	//string s1, s2;
	//while (cin >> s1 >> s2)
	//	cout << match(s1, 0, s2, 0) << endl;
}
