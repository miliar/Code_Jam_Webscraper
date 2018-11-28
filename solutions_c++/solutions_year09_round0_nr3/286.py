#include <iostream>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <vector>
#include <deque>
#include <list>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <bitset>
#include <string>
#include <algorithm>
#include <functional>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <complex>
using namespace std;



int main()
{
	freopen("C-large.in", "r", stdin);freopen("Download C-small.out", "w", stdout);
	//freopen("Download A-large.in", "r", stdin);freopen("Download A-large.out", "w", stdout);
	int cas;scanf("%d\n", &cas);
	int caseid = 1;
	while (cas--)
	{
		string str;getline(cin, str);
		int dp[19] = {0};
		//cout << str << endl;
/*
w e l c o m e _ t o _   c   o   d  e   _   j   a   m
0 1 2 3 4 5 6 7 8 9 10  11  12  13 14  15  16  17  18
*/
		for (int i = 0; str[i]; ++i)
		{
			switch (str[i])
			{
			case 'w':dp[0] = (dp[0] + 1) % 10000;
			break;
			case 'e':dp[1] = (dp[1] + dp[0]) % 10000;
						dp[6] = (dp[6] + dp[5]) % 10000;
						dp[14] = (dp[14] + dp[13]) % 10000;
			break;
			case 'l':dp[2] = (dp[2] + dp[1]) % 10000;
			break;
			case 'c':dp[3] = (dp[3] + dp[2]) % 10000;
						dp[11] = (dp[11] + dp[10]) % 10000;
						break;
			case 'o':dp[4] = (dp[4] + dp[3]) % 10000;
						dp[9] = (dp[9] + dp[8]) % 10000;
						dp[12] = (dp[12] + dp[11]) % 10000;
			break;
			case 'm':dp[5] = (dp[5] + dp[4]) % 10000;
						dp[18] = (dp[18] + dp[17]) % 10000;
			break;
			case ' ':dp[7] = (dp[7] + dp[6]) % 10000;
						dp[10] = (dp[10] + dp[9]) % 10000;
						dp[15] = (dp[15] + dp[14]) % 10000;
			break;
			case 't':dp[8] = (dp[8] + dp[7]) % 10000;
			break;
			case 'd':dp[13] = (dp[13] + dp[12]) % 10000;
			break;
			case 'j':dp[16] = (dp[16] + dp[15]) % 10000;
			break;
			case 'a':dp[17] = (dp[17] + dp[16]) % 10000;
			break;
			}
		}
		printf("Case #%d: %04d\n", caseid++, dp[18]);
	}
	return 0;
}
