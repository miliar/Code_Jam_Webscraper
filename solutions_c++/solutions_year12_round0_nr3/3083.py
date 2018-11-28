#include <stdio.h>
#include <iostream>
#include <bitset> 
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


int m,n;
char ms[8], ns[8];
int tempm, tempn;
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
		scanf("%d",&m);
		scanf("%d",&n);

		for ( int i = m ; i < n ; i++ )
		{
			for ( int j = i + 1 ; j <= n ; j++ )
			{
				itoa (i,ms,10);
				itoa (j,ns,10);
				tempm = i;
				tempn = j;
				
				int k = 0;
				if ( strlen(ms) == strlen(ns) )
					while ( k < strlen(ms)-1 )
					{

						int last = tempm%10;
						tempm = tempm/10 + last*pow(10,strlen(ms)-1);
						k++;
						//cout<<i<<" "<<j<<" "<<tempm<<endl;
						if ( tempm==tempn )
						{
							count++;
							break;
						}
					}
			}
		}
		printf("%d\n",count);
        
        
	}

	return 0;
}
