#include<cstdio>
#include<cstring>
#include<cstdlib>

#define MESSAGE_LENGHT 20

char message[MESSAGE_LENGHT + 1] = "welcome to code jam";
int dp[MESSAGE_LENGHT + 1][1010];
int n;
void clear()
{
	for(int i = 0; i < 25; i++)
		for(int j = 0; j < 1000; j++)
			dp[i][j] = 0;
}

int solve(char * line)
{
	int ans = 0;
	int len = strlen(line);
	int message_len = strlen(message);
	if (message[0] == line[0])
		dp[0][0] = 1;
	for(int i = 0; i < len; i++)
	{
		if(line[i] == message[0])
		{
			dp[0][i] = dp[0][i-1] + 1;
		}
		else 
		{
			dp[0][i] = dp[0][i-1];
		}
	}

	for(int i = 1; i < len; i++)
	{
		for(int j = 1; j < message_len; j++)
		{
			if(line[i] == message[j]) 
			{
				dp[j][i] = (dp[j][i] + dp[j-1][i-1])%10000;
				dp[j][i] = (dp[j][i] + dp[j][i-1])%10000;
			}
			else
			{
				dp[j][i] = dp[j][i-1];
			}
		}
	}
	for(int i = 0; i < len; i++)
	{
		ans = (ans + dp[message_len - 1][i]) % 10000;
	}
	return (dp[message_len-1][len-1] % 10000);
}
int main()
{
	char input_line[1010];
	int ans;
	char anss[5];
	char buf[5];
	int zeroes;
	freopen("c-small.in", "r", stdin);
	freopen("c-small.out", "w", stdout);
	scanf("%d\n",&n);
	for(int tests = 0; tests < n; tests++)
	{
		gets(input_line);
		clear();
		ans = solve(input_line);
		itoa(ans, buf, 10);
		zeroes = 4-strlen(buf);
		for(int i = 0; i < zeroes; i++)
			anss[i] = '0';
		anss[zeroes]='\0';
		printf("Case #%d: %s%d\n",tests+1, anss, ans);
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}