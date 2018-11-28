#include <stdio.h>
#include <string.h>

char str[5002][16];
char tmpStr[500];
int L,D,N,sum;

void sort( int beg , int end )
{
	char key[20],tmp[20];
	int i,j;
	i = beg;
	j = end;
	strcpy( key , str[( i + j ) / 2] );

	do
	{
		while( strcmp( key , str[i] ) > 0 )
			++i;
		while( strcmp( key , str[j] ) < 0 )
			--j;
		if( i <= j )
		{
			strcpy( tmp , str[i] );
			strcpy( str[i] , str[j] );
			strcpy( str[j] , tmp );
			++i;
			--j;
		}
	}while( i <= j );
	if( beg < j )
		sort( beg , j );
	if( i < end )
		sort( i , end );
}

bool find( int count , int pos , int beg , int end , int &newBeg , int &newEnd )
{
	char key;
	int i,j,tmpPos,k;

	i = beg;
	j = end;

	key = tmpStr[pos];

	tmpPos = -1;
	while( i <= j )
	{
		if( key == str[( i + j ) / 2][count] )
		{
			tmpPos = ( i + j ) / 2;
			break;
		}
		if( key < str[( i + j ) / 2][count] )
		{
			j = ( i + j ) / 2 - 1;
		}
		else
		{
			i = ( i + j ) / 2 + 1;
		}
	}

	if( tmpPos != -1 )
	{
		for( k = tmpPos ; k >= beg ; --k )
		{
			if( str[k][count] != key )
			{
				newBeg = k + 1;
				break;
			}
		}
		if( k < beg )
			newBeg = beg;
		for( k = tmpPos ; k <= end ; ++k )
		{
			if( str[k][count] != key )
			{
				newEnd = k - 1;
				break;
			}
		}
		if( k > end )
			newEnd = end;
		return true;
	}
	return false;
}

void search( int count , int pos , int beg , int end ,int len )
{
	int i,k,newBeg,newEnd;
	if( count == L  )
	{
		++sum;
		return ;
	}
	if( tmpStr[pos] == '(' )
	{
		for( i = pos + 2 ; i < len ; ++i )
		{
			if( tmpStr[i] == ')' )
			{
				k = i;
				break;
			}
		}
		for( i = pos + 1 ; i < k ; ++i )
		{
			if( find( count , i , beg , end , newBeg , newEnd ) )
			{
				search( count + 1 , k + 1 , newBeg , newEnd , len );
			}
		}
	}
	if( find( count , pos , beg , end , newBeg , newEnd ) )
	{
		search( count + 1 , pos + 1 , newBeg , newEnd , len );
	}
}

int main()
{
	int len,i;
	
	scanf("%d%d%d",&L,&D,&N);

	for( i = 0 ; i < D ; ++i )
	{
		scanf("%s",str[i]);
	}
	sort( 0 , D - 1 );
	for( i = 0 ; i < N ; ++i )
	{
		scanf("%s",tmpStr);

		len = strlen( tmpStr );
		sum = 0;
		search( 0 , 0 , 0 , D - 1 , len );
		printf("Case #%d: %d\n",i+1,sum);
	}
}
