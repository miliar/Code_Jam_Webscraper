#include <stdio.h>
#include <string>
#include <iostream>
#include <string.h>

using namespace std;

const int maxn = 1100;
int a[maxn][maxn];
char buf[1000];
string s1 = "welcome to code jam";
string s2;


int main()
{
	int n;
	freopen("input.txt", "r" , stdin);
	freopen("output.txt" , "w" , stdout);
	scanf("%d\n"  , &n);
	for (int i = 0; i < n; i++)
	{
		gets(buf);
		s2 = (string)buf;
		memset(a, 0, sizeof(a));			
		for (int k = 0; k <= s2.length(); k++)
			a[0][k] = 1;
		for (int j = 1; j <= s1.length(); j++)
		{
		 for (int k = 1; k <= s2.length(); k++)
		 {
		   int out = 0;
		   for (int l = 1; l <= k; l++)
		   	if (s1[j - 1] == s2[l - 1])
		   	{
		   		out = (out + a[j - 1][l - 1]) % 10000;
		   	}
		   a[j][k] = out;
		}
		}
		

	  printf("Case #%d: %.4d\n", 1 + i, a[s1.length()][s2.length()]);
	}
	return 0;
}