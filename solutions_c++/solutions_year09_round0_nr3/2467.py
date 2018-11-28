#include <stdio.h>
#include <string.h>

char s[22] = "welcome to code jam";
char str[510];
int len,lenS,sum;

void search( int pos , int count )
{
	int i;
	
	if( count == lenS )
	{
		++sum;
	}

	for( i = pos ; i < len ; ++i )
	{
		if( str[i] == s[count] )
		{
			search( i + 1 , count + 1 );
		}
	}
}

int main()
{
	int N,i;
	scanf("%d",&N);
	while( getchar() != '\n' );

	lenS = strlen( s );
	for( i = 1 ; i <= N ; ++i )
	{
		int k = 0;
		char c;
		while( ( c = getchar() ) != '\n' )
		{
			str[k] = c;
			++k;
		}
		str[k] = '\0';
		len = strlen( str );
		sum = 0;
		search( 0 , 0 );
		printf("Case #%d: ",i);
		if( sum < 10 )
			printf("000%d\n",sum);
		else if( sum < 100 )
			printf("00%d\n",sum);
		else if( sum < 1000 )
			printf("0%d\n",sum);
		else
			printf("%d\n",sum);
	}
}
