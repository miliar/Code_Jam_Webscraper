#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>

using namespace std;

const string T = "welcome to code jam";
string S;
int f[510][19];

int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	int N, ans;
	cin >> N;
	getline(cin, S);
	for (int i = 1; i <= N; i++)
	{
		getline(cin, S);
		ans = 0;
		memset(f, 0, sizeof(f));
		for (int j = 0; j < S.length(); j++)
		{
			if (S[j] == 'w') f[j][0] = 1;
			for (int k = 1; k < 19; k++)
			{
				if (S[j] != T[k]) continue;
				for (int l = 0; l < j; l++)
					f[j][k] = (f[j][k]+f[l][k-1])%10000;
			}
			ans = (ans+f[j][18])%10000;
		}
		printf("Case #%d: ", i);
		int len = 0, tmp = ans;
		while (tmp > 0)
		{
			len++;
			tmp /= 10;
		}
		if (ans == 0) len = 1;
		for (int j = 0; j < 4-len; j++)
			printf("0");
		printf("%d\n", ans);
	}
}