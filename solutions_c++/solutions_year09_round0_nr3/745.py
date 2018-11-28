#include<iostream>
#include<cstring>
#include<stdio.h>
using namespace std;

#define sz 505
#define MOD 10000

int main ()
{
	freopen("C-large.in", "r", stdin);
	freopen("C-large-out.txt", "w", stdout);
	int t;
	scanf("%d\n", &t);
	char req[25] = "$welcome to code jam\0";
	for (int numb = 0; numb < t; numb++)
	{
		char str[sz];
		gets(str);
		int DP[sz][20];
		memset(DP, 0, sizeof(DP));
		DP[0][0] = 1;
		for (int i = 0; i < strlen(str); i++)
			for (int j = 0; j < 20; j++)
			{
				DP[i+1][j] = DP[i][j];
				if (j && str[i]==req[j]) DP[i+1][j] += DP[i][j-1];
				DP[i+1][j]%=MOD;
			}
		printf("Case #%d: ", numb+1);
		if (DP[strlen(str)][19] < 1000) printf("0");
		if (DP[strlen(str)][19] < 100) printf("0");
		if (DP[strlen(str)][19] < 10) printf("0");
		printf("%d\n", DP[strlen(str)][19]);
	}
	return 0;
}
