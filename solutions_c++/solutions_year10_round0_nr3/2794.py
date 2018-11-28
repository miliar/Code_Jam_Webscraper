#include <stdio.h>
#include <string.h>

#define MAX_GROUP 1010

struct group_node
{
	int next_index ;
	int profit ;
	int round_no ;
	bool flag ;
} ;

group_node g_info[MAX_GROUP] ;
int g[MAX_GROUP] ;

int main()
{
	int R , limit , N , caseT , case_num , i , j ;

	freopen( "C-large.in" , "r" , stdin ) ;
	freopen( "C-large.out" , "w" , stdout ) ;

	scanf( "%d" , &case_num ) ;
	for ( caseT=1 ; caseT<=case_num ; ++caseT ) 
	{
		scanf( "%d%d%d" , &R , &limit , &N ) ;
		for ( i=0 ; i<N ; ++i )
		{
			scanf( "%d" , &g[i] ) ;
			g_info[i].flag = 0 ;
			g_info[i].next_index = -1 ;
			g_info[i].profit = -1 ;
		}

		long long cycle_profit = 0 , sum_profit = 0 ;
		int cycle_round , last ;
		
		for ( last=0 , cycle_round = 0 ; (cycle_round<R) && (g_info[last].flag==0) ; ++cycle_round )
		{
			int temp = 0 ;
			i = last ;
			while ( 1 )
			{
				if ( temp+g[i]>limit ) break ;
				temp += g[i] ;
				i = (i+1)%N ;
				if ( i == last ) break ;
			}
			g_info[last].flag = 1 ;
			g_info[last].next_index = i ;
			g_info[last].profit = temp ;
			g_info[last].round_no = cycle_round ;
			sum_profit += (long long)temp ;
			last = i ;
		}
		
		int remain_round = R-cycle_round ;
		
		if ( remain_round <= 0 )
		{
			printf( "Case #%d: %lld\n" , caseT , sum_profit ) ;
			continue ;
		}

		cycle_round = cycle_round-g_info[last].round_no ;
		cycle_profit = g_info[last].profit ;
		for ( i=g_info[last].next_index ; i!=last ; )
		{
			cycle_profit += g_info[i].profit ;
			i = g_info[i].next_index ;
		}

		sum_profit += cycle_profit*(long long)(remain_round/cycle_round) ;
		remain_round %= cycle_round ;

		while ( remain_round-- )
		{
			sum_profit += (long long)g_info[last].profit ;
			last = g_info[last].next_index ;
		}

		printf( "Case #%d: %lld\n" , caseT , sum_profit ) ;
	}
	return 0 ;
}

