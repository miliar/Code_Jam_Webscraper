#include<queue>
char t[50] = "welcome to code jam";
const int n = 19, mod = 10000;
char str[1000];
int f[20][1000];

int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	int ncase;
	scanf("%d\n", &ncase);
	for(int c = 0; c < ncase; c++)
	{
		printf("Case #%d: ", c + 1);
		memset(f, 0, sizeof(f));
		for(int i = 0; i < 1000; i++)
			f[0][i] = 1;
		gets(str);
		int l = strlen(str);
		for(int i = 1; i < 20; i++)
			for(int j = 1; j <= l; j++)
				if(str[j - 1] == t[i - 1])
					f[i][j] = (f[i][j - 1] + f[i - 1][j]) % mod;
				else
					f[i][j] = f[i][j - 1];
		int ans = f[19][l], d = mod / 10;
		while(d > ans)
		{
			printf("0");
			d /= 10;
		}
		if(ans != 0)
			printf("%d\n", ans);
		else
			printf("\n");
	}
	return 0;
}
