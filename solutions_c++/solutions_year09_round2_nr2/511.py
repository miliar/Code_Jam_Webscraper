#include <iostream>
#include <string>
#include <algorithm>
using namespace std ;
int list[1000] ;

int main()
{
	freopen("B-large.in" , "r" , stdin) ;
	freopen("B-large.out" , "w" , stdout) ;
	int T , t ; 
	char str[1000] ;
	int i , len ;
	scanf("%d" , &T) ;
	for(t = 1 ; t <= T; t++)
	{
		scanf("%s" , str) ;
		printf("Case #%d: " , t) ;
		len = strlen(str) ;
		if( len == 1 )
		{
			printf("%d0\n" , str[0]-'0') ;
			continue ;
		}
		for(i = 0 ;i < len ; i++)
			list[i] = str[i] - '0' ;
		for(i = 1; i < len ; i++)
			if( list[i-1] < list[i] )  break ;

		if( i == len )
		{
			sort(list , list+len) ;
			for(i = 0 ; i < len ; i++)
				if( list[i] != 0 ) break ; 
			swap(list[0] , list[i]) ;
			printf("%d0" , list[0]) ;
			for(i = 1 ; i < len ; i++)
				printf("%d" , list[i]);
			printf("\n") ;
			continue ;
		}
		//bool flag = false;
		//for(int k = len-1 ; k >= 0 ; k--)
		//{
		//	for(i = len-2 ; i >= 0 ; i--)
		//	{
		//		if( list[i] < list[k] )
		//		{
		//			list[len] = list[k] ;
		//			for(int j = k ; j >= i+1 ; j--)
		//				list[j] = list[j-1] ;
		//			list[i]= list[len] ;
		//			flag = true ;
		//			break ;
		//		}
		//	}
		//	if( flag ) break ;
		//}
		next_permutation(list , list+len) ;
		for(i = 0 ;i < len ; i++)
			printf("%d" , list[i]) ;
		printf("\n") ;
	}
	return 0 ;
}