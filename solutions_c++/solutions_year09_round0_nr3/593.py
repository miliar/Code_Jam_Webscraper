#include <iostream>
#include <string>

using namespace std;

char str[] = "welcome to code jam";
char buf[1000];
int len, buflen;

int dp[100];
int M = 10000;

string to4Char(int i)
{
	char out[5];
	if(i < 10)
	{
		sprintf(out, "000%d", i);
	}
	else if(i < 100)
	{
		sprintf(out, "00%d", i);
	}
	else if(i < 1000)
	{
		sprintf(out, "0%d", i);
	}
	else
	{
		sprintf(out, "%d", i);
	}
	return string(out);
}

int main()
{
	len = strlen(str);
	char out[5];
	gets(out);
	int N = atoi(out);
	for(int NN = 1; NN <= N; NN++)
	{
		memset(dp, 0, sizeof(dp));
		gets(buf);
		buflen = strlen(buf);
		for(int i = 0; i < buflen; i++)
		{
			if(buf[i] == str[0])
			{
				dp[0] = (dp[0] + 1) % M;
			}
			for(int j = 1; j < len; j++)
			{
				if(buf[i] == str[j])
				{
					dp[j] = (dp[j] + dp[j-1]) % M;
				}
			}
		}
		cout << "Case #" << NN << ": " << to4Char(dp[len-1]%M) << endl;
	}
	return 0;
}
