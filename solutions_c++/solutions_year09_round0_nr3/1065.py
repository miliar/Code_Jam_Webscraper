#include <cstdio>
#include <iostream>
#include <cstring>
using namespace std;

char* welcome = "welcome to code jam";
char str[512];
int len;
int table[20][512];

int solve(int a, int b)
{
	if ( a == 0 ) return 1;
	else if ( b == 0 ) return 0;
	int& res = table[a][b];
	if ( res != -1 ) return res;
	res = 0;
	for ( int i=1 ; i<=b ; ++i )
	{
		if ( welcome[a-1] == str[i-1] ) 
		{
			res = (res + solve(a-1, i-1)) % 10000;
		}
	}
	return res;
}

int main()
{
	int T;
	scanf("%d ", &T);

	for ( int t=1 ; t<=T ; ++t )
	{
		gets(str);
		len = strlen(str);
		memset(table, -1, sizeof(table));
		printf("Case #%d: %04d\n", t, solve(19, len));
	}

	return 0;
}
