#include <stdio.h>
#include <iostream>
#include <memory.h>
#include <assert.h>
#include <algorithm>
#include <functional>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <deque>
#include <math.h>

using namespace std;


typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int,int> pii;
typedef map<string,int> msi;

int n, s , p, arr[100];

int main( )
{
	int t, tt, count = 0;

	freopen( "input.txt", "r", stdin );
	freopen( "output.txt", "w", stdout );

	scanf( "%d\n", &tt );
	for( t = 1; t <= tt; ++ t )
	{
		printf( "Case #%d: ", t );
        count  = 0;
		scanf("%d",&n);
		scanf("%d",&s);
		scanf("%d",&p);
        
        
		for ( int i = 0 ; i < n ; i++ )
		{
			scanf("%d",&arr[i]);
			if ( arr[i] >= 3*p - 2 ) 
				count++ ;
			else if ( arr[i] >= 3*p -4 && s && arr[i] > 1)
			{
				count++;
				s--;
			}
		}
		printf("%d\n",count);
        
        
	}

	return 0;
}
