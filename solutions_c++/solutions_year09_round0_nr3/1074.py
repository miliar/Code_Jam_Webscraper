#include<cstdio>
#include<cstring>
char pat[50] = " welcome to code jam";
char str[10000];
int f[10000][50];

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	int ca;
	scanf("%d" , &ca); gets(str);
	int l = strlen(pat); str[0] = ' ';
	for (int cases = 1; cases <= ca; ++cases)
	{
		gets(str + 1);
		int len = strlen(str);
		memset(f, 0 , sizeof(f));
		f[0][0] = 1;
		for (int i = 1; i < len; ++i)
			for (int j = 1; j < l; ++j)
				if (str[i] == pat[j])
					for (int k = 0; k < i; ++k)
						f[i][j] = (f[i][j] + f[k][j - 1]) % 10000;
		int ans = 0;
		for (int i = 1; i < len; ++i)
		   ans = (ans + f[i][l - 1]) % 10000;
		printf("Case #%d: %04d\n", cases, ans);
	}
}
