#include<stdio.h>
#include<iostream>
#include<map>
#include<vector>
#include<algorithm>
#include<stdlib.h>
#include<string>
#include<string.h>
#include<math.h>
#include<stack>
#include<queue>

using namespace std;


int main()
{
      long long int tc , min , candies , candy , ans , calc ;
      scanf("%lld",&tc);
      for(int i=1 ; i<=tc ; i++)
      {
	    calc = 0;
	    min = 1000000000000000000.0;
	    ans =0 ;
	    scanf("%lld",&candies);
	    for(int j=0 ; j<candies ; j++)
	    {

		  scanf("%lld",&candy);
		  if(candy < min)
			min = candy;
		  ans += candy;
		  calc = calc ^ candy;
	    }

	    if(calc != 0)
	    {
		  printf("Case #%d: NO\n",i);
	    }
	    else
		  printf("Case #%d: %lld\n",i , ans - min);

      }
      return 0;
}
