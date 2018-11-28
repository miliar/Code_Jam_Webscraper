#include <vector>
#include <cstdio>
#include <set>
#include <map>
#include <ctime>
#include <string>
#include <sstream>
#include <cstdlib>
#include <iostream>
#include <cmath>
#include <cstring>
#include <cctype>

#define inputfilename "input"
#define outputfilename "a.out"

using namespace std;

string sen="welcome to code jam";
int main ()
{
	/*freopen(inputfilename , "r" , stdin);*/
	/*freopen(outputfilename , "w" , stdout);*/
	
	int number, times;
	cin >> number;getchar();
	for (times = 0 ; times < number ;times++)
	{
		char buf[1000];
		cin.getline(buf , 800);
		string s(buf);
		int dp[1000][20];
		memset(dp , 0 , sizeof(dp));
		int ans = 0;
		int i , j , l;
		for (i = 0 ; i < s.length(); i++)
		{
			for (j = 0 ; j < 19 ; j++)
			{
				if (sen[j] == s[i])
				{
					int v = 0 ;
					if (j == 0) {dp[i][j] = 1;continue;}
					for (l = 0 ; l < i ; l++)
					{
						v = (v + dp[l][j-1]) % 10000;
					}
					dp[i][j] = v;
					if (j == 18) ans = (ans + v) % 10000 ;
				}
			}
		}
		printf("Case #%d: " , times+1);
		if (ans / 1000 == 0) putchar('0');
		if (ans / 100  == 0) putchar('0');
		if (ans / 10   == 0) putchar('0');
		printf("%d\n" , ans);
	}


	return 0;
}

 
