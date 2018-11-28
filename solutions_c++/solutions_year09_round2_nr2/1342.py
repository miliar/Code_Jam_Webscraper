#include <stdio.h>
#include <string.h>

void sort( char *str , int beg , int end )
{
	int i , j;
	char tmp,key;

	key = str[(beg + end) / 2];

	i = beg;j = end;

	do
	{
		if( str[i] < key )
			++i;
		if( str[j] > key )
			--j;
		if( i <= j )
		{
			tmp = str[i];
			str[i] = str[j];
			str[j] = tmp;
			++i;
			--j;
		}
	}while( i <= j );
	if( beg < j )
		sort( str , beg , j );
	if( i < end )
		sort( str , i , end );
}

int main()
{
	int T,i,j,pos,len,pos2;
	char str[40];
	char tmp,max,min;
	
	scanf("%d",&T);

	for( i = 1 ; i <= T ; ++i )
	{
		scanf("%s",str);

		len = strlen( str );

		if( len == 1 )
		{
			printf("Case #%d: %c0\n",i,str[0]);
			continue;
		}

		max = str[len-1];
		for( j = len - 2 ; j >= 0 ; --j )
		{
			if( max > str[j] )
			{
				pos = j;
				break;
			}
			max = str[j];
		}
		if( j == -1 )
		{
			sort( str , 0 , len - 1 );
			for( j = 0 ; j < len ; ++j )
			{
				if( str[j] != '0' )
				{
					tmp = str[0];
					str[0] = str[j];
					str[j] = tmp;
					break;
				}
			}
			printf("Case #%d: ",i);
			for( j = 0 ; j < len ; ++j )
			{
				if( j != 1 )
					printf("%c",str[j]);
				else
				{
					printf("0%c",str[j]);
				}
			}
			printf("\n");
			continue;
		}
		else
		{
			min = str[pos+1];
			pos2 = pos+1;
			for( j = pos + 1 ; j < len ; ++j )
			{
				if( min > str[j] && str[j] > str[pos] )
				{
					min = str[j];
					pos2 = j;
				}
			}

			tmp = str[pos];
			str[pos] = str[pos2];
			str[pos2] = tmp;
			
			sort( str , pos + 1 , len - 1 );
		}
		printf("Case #%d: %s\n",i,str);
	}
}
