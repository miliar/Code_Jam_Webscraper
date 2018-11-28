#include <vector>
#include <string>
#include <list>
#include <map>
#include <utility>
#include <cmath>
#include <algorithm>
#include <sstream>
#include<iostream>
using namespace std;
int N;
char s[501];
int dp[501][19];
int main()
{
	freopen("..\\C-large.in","r",stdin);
	freopen("..\\C-large.out","w",stdout);
	char qqq;
	scanf("%d%c",&N,&qqq);
	for(int i = 1;i <= N;i++)
	{
		int res = 1;
		//getchar();
		cin.getline(s,501);
		memset(dp,0,sizeof(dp));
		int j = strlen(s) - 1;
		for(;j >= 0;j--)
			if(s[j] == 'm') break;
		dp[j][18] = 1;
		j--;
		for(;j >= 0;j--)
		{
			for(int k = 0;k < 19;k++)
				dp[j][k] = dp[j + 1][k];
			switch (s[j])
			{
			    case 'm':
				    dp[j][18]++;
				    dp[j][5] = (dp[j][5] + dp[j + 1][6]) % 10000;
				    break;
				case 'w':
					dp[j][0] = (dp[j][0] + dp[j + 1][1]) % 10000;
					break;
				case 'e':
					dp[j][1] = (dp[j][1] + dp[j + 1][2]) % 10000;
					dp[j][6] = (dp[j][6] + dp[j + 1][7]) % 10000;
					dp[j][14] = (dp[j][14] + dp[j + 1][15]) % 10000;
					break;
				case 'l':
					dp[j][2] = (dp[j][2] + dp[j + 1][3]) % 10000;
					break;
				case 'c':
					dp[j][3] = (dp[j][3] + dp[j + 1][4]) % 10000;
					dp[j][11] = (dp[j][11] + dp[j + 1][12]) % 10000;
					break;
				case 'o':
					dp[j][4] = (dp[j][4] + dp[j + 1][5]) % 10000;;
					dp[j][9] = (dp[j][9] + dp[j + 1][10]) % 10000;;
					dp[j][12] = (dp[j][12] + dp[j + 1][13]) % 10000;;
					break;
				case ' ':
					dp[j][7] = (dp[j][7] + dp[j + 1][8]) % 10000;;
					dp[j][10] = (dp[j][10] + dp[j + 1][11]) % 10000;;
					dp[j][15] = (dp[j][15] + dp[j + 1][16]) % 10000;;
					break;
				case 't':
					dp[j][8] = (dp[j][8] + dp[j + 1][9]) % 10000;;
					break;
				case 'd':
					dp[j][13] = (dp[j][13] + dp[j + 1][14]) % 10000;;
					break;
				case 'j':
					dp[j][16] = (dp[j][16] + dp[j + 1][17]) % 10000;;
					break;
				case 'a':
					dp[j][17] = (dp[j][17] + dp[j + 1][18]) % 10000;;
					break;
			}
		}
		printf("Case #%d: ",i);
		string tmp = "";
		for(int q = 0;q < 4;q++) 
		{
			char cc = dp[0][0] % 10 + '0';
			tmp.append(1,cc);
			dp[0][0] /= 10;
		}
		reverse(tmp.begin(),tmp.end());
        cout<<tmp<<endl;
	}
	return 0;
}