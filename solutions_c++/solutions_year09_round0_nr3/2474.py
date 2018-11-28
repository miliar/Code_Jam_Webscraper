#include <iostream>
#define MAX 520
using namespace std;

const int mm = 28;
char str[] = "welcome to code jam";
int num[mm][mm], len[mm];
int dp[mm];
int slen;
char ss[MAX];

int f(char ca)
{
	if(ca == ' ')
		return 0;
	else
		return ca - 'a' + 1;
}


void solve()
{
	int i, j, t;
	memset(dp, 0, sizeof(dp));
	for(i = 0; i < strlen(ss); i++)
	{
	
		t = f(ss[i]);
		for(j = len[t]-1; j >= 0; j--)
		{
			if(num[t][j] == 0)
				dp[num[t][j]]++;
			else
				dp[num[t][j]] += dp[num[t][j]-1];
			 dp[num[t][j]] = dp[num[t][j]]%10000;
		}
	}
}

int main()
{
//	freopen("C-large.in", "r", stdin);
//	freopen("out.txt", "w", stdout);
	int cas;
	int kk = 0, i, j;
	scanf("%d%*c", &cas);
	memset(num, 0, sizeof(num));
	memset(len, 0, sizeof(len));
	slen = strlen(str);
	for(i = 0; i < slen; i++)
	{
		j = f(str[i]);
		num[j][len[j]++] = i;
	}
	while(kk < cas)
	{
		gets(ss);
		solve();	
		printf("Case #%d: %04d\n", kk+1, dp[slen-1]);
		kk++;
	}
return 0;
}