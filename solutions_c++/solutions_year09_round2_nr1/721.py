
#include <stdio.h>
#include <string.h>
#include <assert.h>

struct NODE
{
	char f[20] ;
	double p ;
	NODE *left , *right , *parent ;
} ;

int main()
{
	int T , caseT ;
	int i , j , n , a , l , num , len ;
	char ch , str[100] , last ;
	char feature[110][20] ;
	NODE *root , *pn ;
	
	freopen( "A-large.in" , "r" , stdin ) ;
	freopen( "A-large.out" , "w" , stdout ) ;
	scanf( "%d" , &T ) ;
	for ( caseT=1 ; caseT<=T ; ++caseT )
	{
		scanf( "%d" , &l ) ; 
		while ( (ch=getchar()) != '(' ) ;
		pn = new NODE ;
		pn->left = NULL ;
		pn->right = NULL ;
		scanf( "%lf" , &pn->p ) ;
		memset( pn->f , 0 , sizeof(pn->f) ) ;
		ch = getchar() ;
		num = 1 ;		
		while ( ch<'a' || ch>'z' )
		{
			if ( ch==')' )
			{
				--num ;
				goto label1 ;
			}
			ch = getchar() ;
		}
		len = 0 ;
		while ( ch>='a' && ch<='z' ) 
		{
			pn->f[len++] = ch ;
			ch = getchar() ;
		}
		if ( ch==')' ) --num ;
label1:	root = pn ;
		root->parent = NULL ;
		if ( num>0 ) last = '(' ;
		while ( num>0 )
		{
			ch=getchar() ;
			if ( ch=='(' ) 
			{
				pn = new NODE ;
				pn->left = NULL ;
				pn->right = NULL ;
				scanf( "%lf" , &pn->p ) ;
				if ( last == '(' ) root->left = pn ;
				else root->right = pn ;		
				pn->parent = root ;			
				++num ;			
				memset( pn->f , 0 , sizeof(pn->f) ) ;
				ch = getchar() ;	
				while ( ch<'a' || ch>'z' )
				{
					if ( ch==')' )
					{
						--num ;
						last = ')' ;
						goto next ;
					}
					ch = getchar() ;
				}
				len = 0 ;
				while ( ch>='a' && ch<='z' ) 
				{
					pn->f[len++] = ch ;
					ch = getchar() ;
				}
				if ( ch==')' )
				{
					--num ;
					last = ')' ;
					goto next ;
				}
				root = pn ;
				last = '(' ;
next:;			
			}
			else if ( ch == ')' ) 
			{
				if ( num>1 ) root = root->parent ;
				last = ')' ;
				--num ;
			}
		}

		assert( root->parent == NULL ) ;
		printf( "Case #%d: \n" , caseT ) ;
		scanf( "%d" , &a ) ;
		for ( i=0 ; i<a ; ++i ) 
		{
			scanf( "%s %d" , str , &n ) ;
			for ( j=0 ; j<n ; ++j ) scanf( "%s" , feature[j] ) ;
			double ans = 1.0 ;
			pn = root ;
			while ( pn ) 
			{
				ans *= pn->p ;
				for ( j=0 ; j<n ; ++j )
					if ( !strcmp( feature[j] , pn->f ) ) break ;
				if ( j<n ) pn = pn->left ;
				else pn = pn->right ;
			}
			printf( "%.7f\n" , ans ) ;
		}

	}
	return 0 ;
}