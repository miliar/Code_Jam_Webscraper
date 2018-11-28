#include <iostream>
#include <string>

using namespace std;

typedef long long ll;
int T;

ll toInt(char c)
{
	if (c <= 'z' && c >= 'a')
		return c - 'a' + 10;
	return c - '0';
}

int main()
{
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);

	cin >> T;

	for (int I = 0 ; I < T; I++)
	{
		ll res = 0;
		string str;
		cin >> str;
		ll a[100];
		for (int i = 0 ;  i < 50; i++) a[i] = -1;

		a[toInt(str[0])] = 1;
		int ans = 0;
		for (int i = 1 ; i < str.size(); i++)
		{
			if (a[toInt(str[i])] < 0)
			{
				a[toInt(str[i])] = ans;
				if (ans == 0) ans = 2;
				else ans++;
			}
		}
		if (ans == 0)
		{
			for (int j = 0 ; j < str.size(); j++)
				res += 1 << j;
		}
		else
		{
			ll pr = 1;
			for (int j = str.size() - 1 ; j >= 0; j--)
			{
				res += a[toInt(str[j])] * pr;
				pr *= ans;
			}
				
		}
		cout << "Case #" << I+1 << ": " << res << endl;
	}

	return 0;
}