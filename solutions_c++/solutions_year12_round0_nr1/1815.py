/*************************************
*Type         :
*Task         :
*Author       : This_poet
*Start Time   :
*Finish Time  :
*Result       :
*Algorithm    :
*************************************/
# include <cstdio>
# include <cstring>
# include <algorithm>
# include <iostream>
# include <cmath>
# define Debug puts("Orz!")
# define outit(x) cout<<#x<<" = "<<x<<endl
# define ps system("pause")
using namespace std;
typedef long long ll;
char s[1000];

int main()
{
	freopen( "in", "r", stdin );
	freopen( "out", "w", stdout );
	int test , flag = 1;
	scanf( "%d\n", &test );
	test = 1;
	char l[26] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
	while ( cin >> s )
	{
		if ( flag ) printf( "Case #%d: ", test ), flag = 0;
		int len = strlen( s );
		for ( int i = 0; i < len; i ++ )
			printf( "%c", l[s[i]-'a'] );
		char ch = getchar();
		if ( ch == ' ' ) printf( " " );
		else printf( "\n" ), test ++, flag = 1;
	}
	return 0;
}
