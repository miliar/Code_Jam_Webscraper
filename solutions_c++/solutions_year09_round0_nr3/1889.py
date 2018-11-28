#include<cstdio>
#include<string>
using namespace std;

const int maxn = 555;
const int maxm = 22;

int f[maxn][maxm];
char a[maxm] = "welcome to code jam";
char s[maxn];
int n, m, k, ans;

int write(int x, int p)
{
	if (p == 0)
		return 0;
	write(x / 10, p - 1);
	printf("%d", x % 10);
	return 0;
}


int main()
{
	freopen(".in","r",stdin);
	freopen(".out","w",stdout);
	scanf("%d\n", &k);
	for (int test = 0; test < k; test++)
	{
		gets(s);
		n = strlen(s);
		m = strlen(a);
		memset(f, 0, sizeof(f));
		f[0][0] = 1;
		ans = 0;
		for (int i = 0; i < n; i++)
		{
			ans =  (ans + f[i][m]) % 1000;
			for (int j = 0; j < m; j++)
				if (f[i][j])
				{
					for (int z = i; z < n; z++)
						if (a[j] == s[z])
							f[z][j + 1] = (f[z][j + 1] + f[i][j]) % 1000;
				}
		}
		printf("Case #%d: ", test + 1);
		write(ans, 4);
		printf("\n");
	}

	
	return 0;
}
