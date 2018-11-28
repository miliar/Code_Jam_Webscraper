#include <stdio.h>
#include <algorithm>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <utility>

using namespace std ;


int main(void){

	int t, Case=0 ;
	int N, S, P, x, res ;

	cin >> t ;
	while( t-- )
	{
		cin >> N >> S >> P ;
		res = 0 ;
		for(int i=0 ; i < N ; i++)
		{
			cin >> x ;
			if( x/3 >= P )
			{
				res++ ;
			}
			else
			{
				if( P - x/3 <= 2 )
				{
					if( P - x/3 == 2 )
					{
						if( S && x%3 == 2 )
						{
							S-- ;
							res++ ;
						}
					}
					if( P - x/3 == 1 )
					{
						if( x%3 >= 1 )
						{
							res++ ;
						}
						if( x && x%3 == 0 && S )
						{
							S-- ;
							res++ ;
						}
					}
				}
			}
		}
		printf("Case #%d: %d\n", ++Case, res) ;
	}

	return 0 ;
}



