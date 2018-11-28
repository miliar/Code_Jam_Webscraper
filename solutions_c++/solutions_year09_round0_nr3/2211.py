#include <stdio.h>
#include <string.h>

const int MaxN=101;
const int MaxLen=501;
const int MaxM=19;
const char jam[]="welcome to code jam";

bool code[MaxLen];
int dp[MaxLen][MaxN];

inline void ini();

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	char str[MaxLen];
	ini();
	int n;
	scanf("%d", &n);
	getchar();
	for(int iCase=1; iCase<=n; iCase++)
	{
		gets(str);
		int i=0, m=0;
		while(str[i]!='\0')
		{
			if(code[str[i]])	str[m++]=str[i];
			i++;
		}
		for(int t=0; t<MaxN; t++)	dp[0][t]=0;
		for(int t=0; t<MaxLen; t++) dp[t][0]=1;

		for(i=1; i<=m; i++)
			for(int j=1; j<=MaxM&&j<=i; j++)
			{
				dp[i][j]=dp[i-1][j]+(str[i-1]==jam[j-1])*dp[i-1][j-1];
				dp[i][j]%=10000;
			}
			printf("Case #%d: %04d\n", iCase, dp[m][MaxM]);
	}
	return 0;
}
inline void ini()
{
	memset(code, false, sizeof(code));
	int i=0;
	while(jam[i]!='\0')	code[jam[i++]]=true;
}