#include "stdio.h"
#include <vector>

class Path
{
public:
	int next;
	long long int money;
};

Path final[1000];
int finalR;
Path pathTable[30][1000];
int R , k , N;

void generate( int i , int p )
{
//printf("generate %d  %d\n",i,p);
	if( p > R )
		return;

	if( i > 0 ) //  generate next
	{
		for( int j = 0 ; j < N ; j++ )
		{
			pathTable[i][j].next = pathTable[ i-1 ] [ pathTable[ i-1 ][j].next ]. next;
			pathTable[i][j].money = pathTable[i-1][j].money + pathTable[ i-1 ] [ pathTable[ i-1 ][j].next ].money;
		}
	}

	generate( i+1 , p*2 );

	// when returning add if required
	if( finalR == 0 )
	{
		for( int j = 0 ; j < N ; j++ )
		{
			final[j] = pathTable[i][j];
		}

		finalR += p;
	}
	else if( finalR + p <= R )
	{
		for( int j = 0 ; j < N ; j++ )
		{
			Path temp = final[j];

			final[j].next = pathTable[i][ temp.next ].next;
			final[j].money = temp.money + pathTable[i][ temp.next ].money;
		}

		finalR += p;
	}


}

int main()
{
	int T;

	scanf(" %d", &T);

	for( int i = 1 ; i <= T ; i++ )
	{
		scanf(" %d %d %d", &R , &k , &N);
		
		std::vector<int> groupSizes;
		std::vector< Path > firstPaths;

		groupSizes.resize( N );

		for( int j = 0 ; j < N ; j++ )
		{
			int t;
			scanf(" %d",&t);
			groupSizes[j] = t;
		}

		for( int start = 0 ; start < N ; start++ )
		{
			// Startting from each group
			int totsize = groupSizes[ start ];
			int cur = start+1;
			if( cur >= N )
				cur = 0;

			while( cur != start )
			{
				if ( totsize + groupSizes[ cur ] > k )
					break;
				totsize += groupSizes[ cur ];

				cur++;
				if( cur >= N )
					cur = 0;
			}
			
			Path aq;
			aq.money = totsize;
			aq.next = cur;
			pathTable[0][ start ] = aq;

		}

		finalR = 0;
		generate( 0 , 1 );

	//	for( int start = 0 ; start < N ; start++ )
	//			printf("Path from %d gains %d$ next group is %d\n",start , final[start].money , final[start].next );
		printf("Case #%d: %lld\n",i,final[0].money );
	}


	return 0;
}
