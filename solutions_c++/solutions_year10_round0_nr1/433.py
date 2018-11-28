
#include "stdio.h"


int main()
{

	int N , K , pow;

	int num;

	scanf(" %d",&num);


	for( int i = 1 ; i <= num ; i++ )
	{
		scanf(" %d %d", &N , &K);

		pow = 1;
		for( int j = 1 ; j <= N ; j++ )
			pow *= 2;

		if( K % pow == pow - 1 )
			printf("Case #%d: ON\n",i);
		else
			printf("Case #%d: OFF\n",i);
	}

return 0;
}


