#include <iostream>

using namespace std;

int N;
char pattern[100] = "welcome to code jam";
char sen[1024];
int f[1024][32];

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	scanf("%d", &N);
	int plen = strlen(pattern);
    gets(sen);
	for (int i = 0; i < N; i++)
	{
		gets(sen);
		int len = strlen(sen);
		memset(f, 0, sizeof(f));
		for (int j = 0; j < len; j++)
		{
			for (int k = 0; k < plen; k++)
				if (sen[j] == pattern[k])
				{
					if (k == 0)
						f[j][k]++;
					else
						for (int p = j-1; p >= 0; p--)
						{
							f[j][k] += f[p][k-1];
							if (f[j][k] > 100000)
								f[j][k] %= 100000;
						}
				}
		}
		printf("Case #%d: ", i+1);
		int res = 0;
		for (int i = 0; i < len; i++)
		{
			res += f[i][plen-1];
			if (res > 10000) res %= 10000;
		}
		//printf("%d\n", res);
		if (res < 10) printf("000");
		else
			if (res < 100) printf("00");
			else
				if (res < 1000) printf("0");
		printf("%d\n", res);
	}
	return 0;
}