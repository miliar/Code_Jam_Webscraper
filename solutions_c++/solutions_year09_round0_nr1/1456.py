#include <cstdio>
#include <cstring>

using namespace std;

int L, D, N;
char word[5000][16];

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	scanf("%d%d%d", &L, &D, &N);
	for (int i = 0; i < D; i++)
		scanf("%s", word[i]);
	bool have[16][26];
	char s[1000];
	for (int i = 1; i <= N; i++)
	{
		memset(have, 0, sizeof(have));
		scanf("%s", s);
		int now = 0;
		bool flag = false;
		for (int j = 0; j < strlen(s); j++)
		{
			if (s[j] == '(') 
				flag = true;
			else
			{
				if (s[j] == ')')
				{
					flag = false;
					now++;
				}
				else
				{
					have[now][s[j]-'a'] = true;
					if (!flag) now++;
				}
			}
		}
		int ans = 0;
		for (int j = 0; j < D; j++)
		{
			bool flag = true;
			for (int k = 0; k < L; k++)
				if (!have[k][word[j][k]-'a']) flag = false;
			if (flag) ans++;
		}
		printf("Case #%d: %d\n", i, ans);
	}
}