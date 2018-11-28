#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

string mini(string s, int a, int b)
{
	string ret = "";
	for (int i = a; i <= b; i++)
		ret += s[i];
	sort(ret.begin(), ret.end());
	return ret;
}

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int T;
	cin >> T;
	string s;
	getline(cin, s);
	for (int tt = 1; tt <= T; tt++)
	{
		getline(cin, s);
		bool flag = true;
		for (int i = 1; i < s.length(); i++)
			if (s[i] > s[i-1]) flag = false;
		if (flag)
		{
			cout << "Case #" << tt << ": ";
			int k;
			for (int i = s.length()-1; i >= 0; i--)
				if (s[i] != '0')
				{
					k = i;
					break;
				}
			cout << s[k] << '0';
			for (int i = s.length()-1; i >= 0; i--)
				if (i != k)
					cout << s[i];
			cout << endl;
		}
		else
		{
			for (int i = s.length()-2; i >= 0; i--)
			{
				char ch = '9';
				int k = -1;
				for (int j = i+1; j < s.length(); j++)
					if (s[j] > s[i] && s[j] <= ch)
					{
						ch = s[j];
						k = j;
					}
				if (k >= 0)
				{
					char tmp = s[i];
					s[i] = s[k];
					s[k] = tmp;
					cout << "Case #" << tt << ": ";
					for (int j = 0; j <= i; j++)
						cout << s[j];
					cout << mini(s, i+1, s.length()-1) << endl;
					break;
				}
			}
		}
	}
}