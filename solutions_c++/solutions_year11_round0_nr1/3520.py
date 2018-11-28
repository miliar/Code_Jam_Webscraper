#include "stdio.h"
#include "math.h"

#define		MIN(a,b)	(a) < (b) ? (a) : (b)

struct node
{
	int kind,pos ;

	node() {}
	node( int _kind , int _pos ):kind(_kind),pos(_pos) {}

} seq[1024] ;

int		size ;
int		seqo[1024] , seqb[1024] ;
int     sizeo , sizeb ;

void Input()
{
	int		i,pos ;
	char	s[12] ;

	scanf( "%d" , & size ) ;

	sizeo = sizeb = 0 ;

	for( i = 1 ; i <= size ; ++i )
	{
		scanf( "%s%d" , s , & pos ) ;
		seq[i] = node( s[0] == 'O' ?1:2 , pos ) ;
		s[0] == 'O' ? seqo[++sizeo] = pos : seqb[++sizeb] = pos ;
	}
	seqo[0] = seqb[0] = 1 ;
}

int GetStep()
{
	int i,poso,posb,idxo,idxb ;
	int step,cnt = 0 ;

	poso = posb = 1 ;
	idxo = idxb = 0 ;
	
	for( i = 1 ; i <= size ; )
	{
		int idx = seq[i].kind ;

		if( idx&1 )
		{
			if( poso == seq[i].pos ) 
			{
				++cnt , ++i , ++idxo ;
				step = 1 ;
			//	printf( "Orange Press %d\n" , poso ) ;
			}
			else
			{
				step = abs( poso-seq[i].pos ) ;
				cnt += step ;
				poso = seq[i].pos ;
				if( idxb+1 <= sizeb )
				{
					step = MIN( step,abs( seqb[idxb] - seqb[idxb+1] ) ) ;
				}
				else
					step = 0 ;
			}

			while( step-- )
			{
				if( idxb+1 <= sizeb )
				{
					if( seqb[idxb] < seqb[idxb+1] && posb < seqb[idxb+1] ) ++ posb ;
					if( seqb[idxb] > seqb[idxb+1] && posb > seqb[idxb+1] ) -- posb ;					
				}
				if( posb == seqb[idxb+1] ) break ;				
			}
		}
		else
		{
			if( posb == seq[i].pos )
			{
				++cnt , ++i , ++idxb ;
				step = 1 ;
			//	printf( "Blue Press %d\n" , posb ) ;
			}
			else
			{
				step = abs( posb-seq[i].pos ) ;
				cnt += step ;
				posb = seq[i].pos ;
				if( idxo+1 <= sizeo )
				{
					step = MIN( step,abs( seqo[idxo] - seqo[idxo+1] ) ) ;
				}
				else
					step = 0 ;
			}	
			
			while( step-- )
			{
				if( idxo+1 <= sizeo )
				{
					if( seqo[idxo] < seqo[idxo+1] && poso < seqo[idxo+1] ) ++ poso ;
					if( seqo[idxo] > seqo[idxo+1] && poso > seqo[idxo+1] ) -- poso ;
				}
				if( poso == seqo[idxo+1] ) break ;
			}
		}
	}
	return cnt ;
}

int Solve()
{
	Input() ;
	return GetStep() ;
}

int main()
{
	freopen( "A-large.in" , "r" , stdin ) ;
	freopen( "A-large.out" , "w" , stdout ) ;

	int i=1, cas ;	
	for( scanf( "%d" , & cas ) ; i <= cas ; ++i )
	{	
		printf( "Case #%d: %d\n" , i, Solve() ) ;
	}
	return 0 ;
}