#include "stdio.h"
#include "string.h"
#include "iomanip.h"
#include "iostream"

using namespace std ;

int tot[110] , v[110] , size ;
int mat[110][110] ;
int link[110][110] ;

double WP[110] , OWP[110] , OOWP[110] ;

void Input()
{
	memset( v   , 0 , sizeof(v)   ) ;
	memset( tot , 0 , sizeof(tot) ) ;
	memset( mat , 0 , sizeof(mat) ) ;
	memset( link, 0 , sizeof(link)) ;

	memset( WP  , 0 , sizeof(WP)  ) ;
	memset( OWP , 0 , sizeof(OWP) ) ;
	memset( OOWP, 0 , sizeof(OOWP)) ;

	char str[1024] ;
	int  i,j;

	scanf( "%d" , & size );

	for( j = 1 ; j <= size ; ++j )
	{
		scanf( "%s" , str ) ;
		for( i = 0 ; str[i] ; ++i )
		{
			if( str[i] != '.' )
			{
				link[j][++tot[j]] = i+1 ;
				if( str[i] == '1' )  mat[j][i+1] = 1 , ++v[j] ;
			}
		}
	}	
}

void Cal()
{
	int i,j ;

	for( i = 1 ; i <= size ; ++i )
	{
		WP[i] = double( v[i]*1.0 / tot[i] ) ;
	}

	for( j = 1 ; j <= size ; ++j )
	{	
		double vtmp = 0 ;
		for( i = 1 ; i <= tot[j] ; ++i )
		{
			int num = link[j][i] ;
			int win = v[num] ;
			if( mat[num][j] ) -- win ;
			if( tot[num] != 1 )
				vtmp += double( win*1.0 / (tot[num]-1) ) ;
		}
		OWP[j] = vtmp / tot[j] ;
	}

	for( j = 1 ; j <= size ; ++j )
	{
		double vtmp = 0 ;
		for( i = 1 ; i <= tot[j] ; ++i )
		{
			int num = link[j][i] ;
			vtmp += OWP[num] ;
		}
		OOWP[j] = vtmp / tot[j] ;
	}
}

void Output()
{
	for( int i = 1 ; i <= size ; ++i )
	{
		printf( "%.10lf\n" , 0.25*WP[i] + 0.5*OWP[i] + 0.25*OOWP[i] ) ;
	//	cout << setprecision(6) 
	//		 << 0.25*WP[i] + 0.5*OWP[i] + 0.25*OOWP[i]
	//		 << endl ;
	}
}

int main()
{
	freopen( "A-big.in" , "r" , stdin ) ;	
	freopen( "A-big.out" , "w" , stdout ) ;	

	int i,cas ;
	scanf( "%d" , & cas ) ;

	for( i = 1 ; i <= cas ; ++i )
	{
		printf( "Case #%d:\n" , i ) ;
		Input() ;
		Cal() ;
		Output() ;
	}
	return 0 ;
}