#include <cstdio>
#include <algorithm>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <utility>

using namespace std ;


char t[6][6] ;

bool X(char c){ return c == 'X' || c == 'T' ; }
bool O(char c){ return c == 'O' || c == 'T' ; }

int main(void)
{
	int T, cases = 1 ;

	scanf("%d", &T) ;
	gets(t[0]) ;

	while( T-- )
	{
		gets(t[0]) ;
		gets(t[1]) ;
		gets(t[2]) ;
		gets(t[3]) ;

		if( (X(t[0][0]) && X(t[0][1]) && X(t[0][2]) && X(t[0][3])) ||
				(X(t[1][0]) && X(t[1][1]) && X(t[1][2]) && X(t[1][3])) ||
				(X(t[2][0]) && X(t[2][1]) && X(t[2][2]) && X(t[2][3])) ||
				(X(t[3][0]) && X(t[3][1]) && X(t[3][2]) && X(t[3][3])) ||

				(X(t[0][0]) && X(t[1][0]) && X(t[2][0]) && X(t[3][0])) ||
				(X(t[0][1]) && X(t[1][1]) && X(t[2][1]) && X(t[3][1])) ||
				(X(t[0][2]) && X(t[1][2]) && X(t[2][2]) && X(t[3][2])) ||
				(X(t[0][3]) && X(t[1][3]) && X(t[2][3]) && X(t[3][3])) ||

				(X(t[0][0]) && X(t[1][1]) && X(t[2][2]) && X(t[3][3])) ||
				(X(t[0][3]) && X(t[1][2]) && X(t[2][1]) && X(t[3][0])) )
		{
			printf("Case #%d: X won\n", cases++) ;
		}
		else if((O(t[0][0]) && O(t[0][1]) && O(t[0][2]) && O(t[0][3])) ||
				(O(t[1][0]) && O(t[1][1]) && O(t[1][2]) && O(t[1][3])) ||
				(O(t[2][0]) && O(t[2][1]) && O(t[2][2]) && O(t[2][3])) ||
				(O(t[3][0]) && O(t[3][1]) && O(t[3][2]) && O(t[3][3])) ||
				
				(O(t[0][0]) && O(t[1][0]) && O(t[2][0]) && O(t[3][0])) ||
				(O(t[0][1]) && O(t[1][1]) && O(t[2][1]) && O(t[3][1])) ||
				(O(t[0][2]) && O(t[1][2]) && O(t[2][2]) && O(t[3][2])) ||
				(O(t[0][3]) && O(t[1][3]) && O(t[2][3]) && O(t[3][3])) ||

				(O(t[0][0]) && O(t[1][1]) && O(t[2][2]) && O(t[3][3])) ||
				(O(t[0][3]) && O(t[1][2]) && O(t[2][1]) && O(t[3][0])) )
		{
			printf("Case #%d: O won\n", cases++) ;
		}
		else if( t[0][0] == '.' || t[0][1] == '.' || t[0][2] == '.' || t[0][3] == '.'
				|| t[1][0] == '.' || t[1][1] == '.' || t[1][2] == '.' || t[1][3] == '.'
				|| t[2][0] == '.' || t[2][1] == '.' || t[2][2] == '.' || t[2][3] == '.'
				|| t[3][0] == '.' || t[3][1] == '.' || t[3][2] == '.' || t[3][3] == '.' )
		{
			printf("Case #%d: Game has not completed\n", cases++) ;
		}
		else
		{
			printf("Case #%d: Draw\n", cases++) ;
		}

		gets(t[3]) ;
	}


	return 0 ;
}



