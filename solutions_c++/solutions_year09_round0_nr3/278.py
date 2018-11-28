#include "stdio.h"
#include <vector>
using namespace std;

int ans[1000][20];
char w[1000];
const char *welcome = "welcome to code jam";

int main()
{
	freopen( "test.in", "r", stdin );
	freopen( "test.out", "w", stdout );
	int caseNum;
	scanf( "%d", &caseNum );
	getchar();
	for( int ci=0; ci<caseNum; ++ci )
	{
		memset( w, 0, sizeof(w) );
		gets( w+1 );
		memset( ans, 0, sizeof(ans) );

		int i;
		for( i=1; w[i]; ++i )
		{
			ans[i][0] = (ans[i-1][0] + (int)( w[i] == welcome[0] ))%10000;
			for( int j=1; j<19; ++j )
			{
				ans[i][j] = (ans[i-1][j] + (  w[i] == welcome[j] ? ans[i-1][j-1] : 0 ) ) % 10000;
			}
		}
		printf( "Case #%d: %04d\n", ci+1, ans[i-1][18] );
	}
	return 0;

}