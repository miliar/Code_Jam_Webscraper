#include <iostream>
#include <string>
#include <cstring>
#include <cstdio>

using namespace std;
const int MOD = 10000;
const int MAXLEN = 510;
string dst("welcome to code jam");

int opt[MAXLEN][30];

int dp(string str)
{
	memset(opt, 0, sizeof(opt));
	opt[0][0] = 1;
	int res = 0;
	for(int i = 0; i < str.length(); i++)
	{
		for(int j = 0; j < dst.length(); j++)
		{
			opt[i][j] %= MOD;
			opt[i + 1][j] += opt[i][j];
			if(str[i] == dst[j]) opt[i + 1][j + 1] += opt[i][j];
		}
		res += opt[i][dst.length()];
		res %= MOD;
	}
	return (res + opt[str.length()][dst.length()]) % MOD;
}

void output(int a)
{
	int x = 1, cnt = 0;
	while(x <= a) x *= 10, ++cnt;
	for(; cnt < 4; cnt++) cout << 0;
	if(a) cout << a;
	cout << endl;
}

int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	int ncase;
	cin >> ncase;
	getchar();
	for(int i = 1; i <= ncase; i++)
	{
		string str;
		getline(cin, str, '\n');
		cout << "Case #" << i << ": ";
		output(dp(str));
	}
	return 0;
}
