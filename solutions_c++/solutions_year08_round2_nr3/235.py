#include <iostream>
#include <list>
using namespace std ;

int a[5005] ;
list<int>b ;
int main(){
	int test ;
	freopen( "C-small-attempt1.in" , "r" , stdin ) ;
	freopen( "C-small-attempt1.out" , "w" , stdout ) ;
	scanf("%d" , &test ) ;
	int t = 1 ;
	while( test -- )
	{
		int i , n;
		scanf("%d" , &n ) ;
		memset( a , 0 , sizeof(a) ) ;
		int num = 1 ;
		i = 1 ;
		for( i = 1 ; i <= n ;i ++ )
			b.push_back( i ) ;

		int val , m ;
		list<int>::iterator iter ;
		iter = b.begin () ;
		int cnt = 0 ;
		while( num <= n )
		{
			while( cnt -- )
			{
				iter ++ ;
				if( iter == b.end () )
					iter = b.begin () ;
			}
			a[*iter] = num ;
			num ++ ;
			cnt = num - 1 ;
			b.erase(iter++) ;
			if( iter == b.end () )
				iter = b.begin() ;
		}
		scanf("%d" , &m ) ;
		printf("Case #%d:" , t ++ ) ;
		for( i = 0 ; i < m ; i ++ )
		{
			scanf("%d" , &val ) ;
			printf(" %d" , a[val] ) ;
		}
		printf("\n" ) ;
	}
	return 0 ;
}