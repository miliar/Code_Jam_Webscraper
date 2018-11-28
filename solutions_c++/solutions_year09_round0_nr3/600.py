
#include<iostream>
#include<string>
#include<algorithm>
#include<vector>
using namespace std;
char str[505];
bool visit[505];
int DP[805][20];
int main()
{
	freopen("C-large.in" , "r" , stdin);
	freopen("ans.out" , "w" , stdout);
	int N;
	scanf("%d" , &N);
	getchar();
	int T = 0;
	while(N-- )
	{
		T++;
		gets(str);
		int i;
		int len = strlen(str);
		memset(DP , 0 , sizeof(DP));
		if(str[0] == 'w')
			DP[0][0] = 1;
		for(i = 1 ; i < len ; i++)
		{
			if(str[i] == 'w')
			{
				DP[i][0] += DP[i-1][0] +1 ;
				DP[i][0] %= 10000;
			}
			else
			{
				DP[i][0] = DP[i-1][0];
				DP[i][0] %= 10000;
			}
			if(str[i] == 'e')
			{
				DP[i][1] += DP[i-1][0] + DP[i-1][1];
				DP[i][1] %= 10000;
				DP[i][6] += DP[i-1][5] + DP[i-1][6];
				DP[i][6] %= 10000;
				DP[i][14] += DP[i-1][13] + DP[i-1][14];
				DP[i][14] %= 10000;
			}
			else
			{
				DP[i][1] = DP[i-1][1];
				DP[i][1] %= 10000;
				DP[i][6] = DP[i-1][6];
				DP[i][6] %= 10000;
				DP[i][14] = DP[i-1][14];
				DP[i][14] %= 10000;
			}
			if(str[i] == 'l')
			{
				DP[i][2] += DP[i-1][1] + DP[i-1][2];
				DP[i][2] %= 10000;
			}
			else
			{
				DP[i][2] = DP[i-1][2];
				DP[i][2] %= 10000;
			}
			if(str[i] == 'c')
			{
				DP[i][3] += DP[i-1][2] + DP[i-1][3];
				DP[i][3] %= 10000;
				DP[i][11] += DP[i-1][10] + DP[i-1][11];
				DP[i][11] %= 10000;
			}
			else
			{
				DP[i][3] = DP[i-1][3];
				DP[i][3] %= 10000;
				DP[i][11] = DP[i-1][11];
				DP[i][11] %= 10000;
			}
			if(str[i] == 'o')
			{
				DP[i][4] += DP[i-1][3] + DP[i-1][4];
				DP[i][4] %= 10000;
				DP[i][9] += DP[i-1][8] + DP[i-1][9];
				DP[i][9] %= 10000;
				DP[i][12] += DP[i-1][11] + DP[i-1][12];
				DP[i][12] %= 10000;
			}
			else
			{
				DP[i][4] = DP[i-1][4];
				DP[i][4] %= 10000;
				DP[i][9] = DP[i-1][9];
				DP[i][9] %= 10000;
				DP[i][12] = DP[i-1][12];
				DP[i][12] %= 10000;
			}
			if(str[i] == 'm')
			{
				DP[i][5] += DP[i-1][4] + DP[i-1][5];
				DP[i][5] %= 10000;
				DP[i][18] += DP[i-1][17] + DP[i-1][18];
				DP[i][18] %= 10000;
			}
			else
			{
				DP[i][5] = DP[i-1][5];
				DP[i][5] %= 10000;
				DP[i][18] = DP[i-1][18];
				DP[i][18] %= 10000;
			}
			if(str[i] == ' ')
			{
				DP[i][7] += DP[i-1][6] + DP[i-1][7];
				DP[i][7] %= 10000;
				DP[i][10] += DP[i-1][9] + DP[i-1][10];
				DP[i][10] %= 10000;
				DP[i][15] += DP[i-1][14] + DP[i-1][15];
				DP[i][15] %= 10000;
			}
			else
			{
				DP[i][7] = DP[i-1][7];
				DP[i][7] %= 10000;
				DP[i][10] =  DP[i-1][10];
				DP[i][10] %= 10000;
				DP[i][15] = DP[i-1][15];
				DP[i][15] %= 10000;
			}
			if(str[i] == 't')
			{
				DP[i][8] += DP[i-1][7] + DP[i-1][8];
				DP[i][8] %= 10000;
			}
			else
			{
				DP[i][8] = DP[i-1][8];
				DP[i][8] %= 10000;
			}
			if(str[i] == 'd')
			{
				DP[i][13] += DP[i-1][12] + DP[i-1][13];
				DP[i][13] %= 10000;
			}
			else
			{
				DP[i][13] = DP[i-1][13];
				DP[i][13] %= 10000;
			}
			if(str[i] == 'j')
			{
				DP[i][16] += DP[i-1][15] + DP[i-1][16];
				DP[i][16] %= 10000;
			}
			else
			{
				DP[i][16] = DP[i-1][16];
				DP[i][16] %= 10000;
			}
			if(str[i] == 'a')
			{
				DP[i][17] += DP[i-1][16] + DP[i-1][17];
				DP[i][17] %= 10000;
			}
			else
			{
				DP[i][17] = DP[i-1][17];
				DP[i][17] %= 10000;
			}

		}
		int ans = 0;
		for(i = len - 1; i >= 0 ; i--)
		{
			if(str[i] == 'm')
			{
				ans += DP[i][18];
				ans %= 10000;
				break;
			}
		}
		printf("Case #%d: "  , T);
		if(ans < 10)
		{
			printf("000");
			printf("%d\n" , ans);
			continue;
		}
		if(ans < 100)
		{
			printf("00");
			printf("%d\n" , ans);
			continue;
		}
		if(ans < 1000)
		{
			printf("0");
			printf("%d\n" , ans);
			continue;
		}
		printf("%d\n" , ans);
		
		
	}	
	
	
	return 0;
}

