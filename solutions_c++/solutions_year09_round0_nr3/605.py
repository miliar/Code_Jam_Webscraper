#include<iostream>
using namespace std;

const char*c="welcome to code jam";
char s[501];
int f[501][21];
int n;

int main()
{
	freopen("test.in","r",stdin);
	freopen("test.out","w",stdout);
	scanf("%d\n",&n);
	for (int T=1;T<=n;T++)
	{
		gets(s);
		int len=strlen(s);
		int len2=strlen(c);
		for (int i=0;i<=len;i++)
			f[i][0]=1;
		for (int i=1;i<=len;i++)
			for (int j=1;j<=len2;j++)
			{
				f[i][j]=f[i-1][j];
				if (s[i-1]==c[j-1])
					f[i][j]=(f[i][j]+f[i-1][j-1])%10000;
			}
		printf("Case #%d: ",T);
		if (f[len][len2]<1000) printf("0");
		if (f[len][len2]<100) printf("0");
		if (f[len][len2]<10) printf("0");
		printf("%d\n",f[len][len2]);
	}
}