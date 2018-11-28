#include <stdio.h>
#include <string.h>

int main()
{
	int T,k,i,j,len,flag,u;
	int arr[100],opt[100];
	char str[100];

	scanf("%d",&T);
	for( u = 1 ; u <= T ; ++u )
	{
		scanf("%s",str);
		len = strlen( str );

		flag = 0;
		memset( opt , 0 , sizeof( opt ) );
		k = 1;
		for( i = 0 ; i < len ; ++i )
		{
			if( opt[i] != 0 )
				continue;
			if( k == 2 && flag == 0 )
			{
				arr[i] = 0;
				flag = 1;
			}
			else
			{
				arr[i] = k;
				k++;
			}
			opt[i] = 1;
			for( j = i + 1 ; j < len ; ++j )
			{
				if( str[j] == str[i] )
				{
					arr[j] = arr[i];
					opt[j] = 1;
				}
			}
		}
		long long sum;
		long long s;
		
		s = 1;
		sum = arr[len-1];

		for( i = len - 2 ; i >= 0 ; --i )
		{
			s = s*k;
			sum += arr[i] * s;
		}
		printf("Case #%d: %lld\n",u,sum);
	}
}
