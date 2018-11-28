#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>

using namespace std;

const char cstr[] = "welcome to code jam";

const int base = 10000;

char inp[550];
int cnt[550][30];

int N;

int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);

	scanf("%d\n", &N);

	for (int id = 1; id <= N; id++) 
	{
		fgets(inp, 550, stdin);

		memset(cnt, 0, sizeof cnt);
		
		int len = strlen(inp);

		cnt[0][0] = 1;

		for (int i = 0; i < len; i++)
		{
			cnt[i + 1][0] = 1;

			for (int k = 0; k < strlen(cstr); k++)
			{
				cnt[i + 1][k + 1] = cnt[i][k + 1];
				if (inp[i] == cstr[k]) cnt[i + 1][k + 1] += cnt[i][k];
				cnt[i + 1][k + 1] %= base;
			}
		}

		printf("Case #%d: %.4d\n", id, cnt[len][strlen(cstr)] % base);
	}

	return 0;
}
