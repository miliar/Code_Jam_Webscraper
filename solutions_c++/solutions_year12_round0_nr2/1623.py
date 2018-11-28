#include <cstdio>
#include <cstdlib>
#include <algorithm>

#define SIZE_N 110

FILE *in , *out ;

int T , n , p , s ;
int ary[SIZE_N] ;

int dan[SIZE_N] , can[SIZE_N] ;

int main(void)
{
	in = fopen("B-large.in" , "r") ;
	out = fopen("B-large.out" , "w") ;
	
	fscanf(in , "%d" , &T) ;
	for(int count = 1 ; count <= T ; ++count)
	{
		for(int i = 0 ; i < SIZE_N ; ++i)
			dan[i] = can[i] = 0 ;
		
		fscanf(in , "%d%d%d" , &n , &s , &p) ;
		for(int i = 0 ; i < n ; ++i)
			fscanf(in , "%d" , &ary[i]) ;
		
		for(int i = 0 ; i < n ; ++i)
		{
			dan[i] = ary[i] / 3 ;
			
			if(ary[i] % 3 == 1)
			{
				if(dan[i] + 1 >= p) can[i] = 1 ;
			}
			else if(ary[i] % 3 == 2)
			{
				++dan[i] ;
				if(dan[i] >= p) can[i] = 1 ;
				else if(s > 0)
				{
					if(dan[i] + 1 <= 10 && dan[i] + 1 >= p)
						--s , can[i] = 1 ;
				}
			}
			else
			{
				if(dan[i] >= p) can[i] = 1 ;
				else if(s > 0)
				{
					if(dan[i] + 1 <= 10 && dan[i] - 1 >= 0 && dan[i] + 1 >= p)
						--s , can[i] = 1 ;
				}
			}
		}
		
		int ans = 0 ;
		for(int i = 0 ; i < n ; ++i)
			ans += can[i] ;
		
		fprintf(out , "Case #%d: %d\n" , count , ans) ;
	}
	
	fclose(in) , fclose(out) ;
	
	return 0 ;
}
