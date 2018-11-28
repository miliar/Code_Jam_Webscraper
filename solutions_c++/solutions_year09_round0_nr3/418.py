#include <iostream>
#include <algorithm>

using namespace std;

long long dp[500][20];

int main()
{
	int tcase;
	cin >> tcase;
	char a[502];
	cin.getline(a,500);
	for(int t = 1; t <= tcase; t++)
	{
		memset(dp,0,sizeof(dp));
		fill(a,a+502,'Z');
		cin.getline(a,501);
		if(a[0] == 'w') dp[0][1] = 1;
		int length = 0;

		for(int i = 0; a[i] != '\0'; i++)
		{
			length = i;
			for(int j = i+1; a[j] != '\0'; j++)
			{
				if(a[j] == 'w')
					dp[j][1] = 1;
				else if(a[j] == 'e')
				{
					dp[j][2] += dp[i][1]%10000;
					dp[j][7] += dp[i][6]%10000;
					dp[j][15] += dp[i][14]%10000;
				}
				else if(a[j] == 'l')
					dp[j][3] += dp[i][2]%10000;
				else if(a[j] == 'c')
				{
					dp[j][4] += dp[i][3]%10000;
					dp[j][12] += dp[i][11]%10000;
				}
				else if(a[j] == 'o')
				{
					dp[j][5] += dp[i][4]%10000;
					dp[j][10] += dp[i][9]%10000;
					dp[j][13] += dp[i][12]%10000;
				}
				else if(a[j] == 'm')
				{
					dp[j][6] += dp[i][5]%10000;
					dp[j][19] += dp[i][18]%10000;
				}
				else if(a[j] == ' ')
				{
					dp[j][8] += dp[i][7]%10000;
					dp[j][11] += dp[i][10]%10000;
					dp[j][16] += dp[i][15]%10000;
				}
				else if(a[j] == 't')
					dp[j][9] += dp[i][8];
				else if(a[j] == 'd')
					dp[j][14] += dp[i][13]%10000;
				else if(a[j] == 'j')
					dp[j][17] += dp[i][16]%10000;
				else if(a[j] == 'a')
					dp[j][18] += dp[i][17]%10000;
			}
		}
		cout << "Case #" << t << ": ";
		long long tot = 0;
		for(int i = 0; i < length+1; i++)
			tot += dp[i][19]%10000;

		tot %= 10000;
		if(tot < 1000)
		{
			int temp = tot;
			if(temp == 0) temp = 1;
			while(temp < 1000)
			{
				cout << "0";
				temp *= 10;
			}
		}
		cout << tot%10000 << endl;
	}
	return 0;
}