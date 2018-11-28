#include <iostream>
#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <algorithm>
#include <cmath>

using namespace std ;
const char to[31] = { 'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q' } ; 

int T, C, L ;
char s[201] ;

int main()
{
	int C = 0, i ; 
	
//	freopen("A0.in","r",stdin) ;
//	freopen("A.out","w",stdout) ;
	
	for( scanf("%d\n", &T) ; T-- ; ) 
	{
		++ C ; 
		printf("Case #%d: ",C) ; 
		gets(s);
		L = strlen( s ) ; 
		for( i = 0 ; i < L ; ++i ) 
		{
			if( s[i] <= 'z' && s[i] >= 'a' )
				printf("%c", to[s[i]-'a'] ) ;
			else 
				printf(" ") ;	
		}
		printf("\n") ; 
	}
//	system("pause") ;
	return 0 ; 
}
