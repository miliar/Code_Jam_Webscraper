#include <cstdio>
#include <cstring>
#include <algorithm>
#define MAXN 50000+10
#define MAX 1000000000
using namespace std;


int t[ 5 ];
int dl;
int k;
char s[ MAXN ];
char s2[ MAXN ];
int result;


void go()
{
	int res = 1;
	for(int x=0; x<dl; x+=k)
		for(int y=0; y<k; y++)
		{
			s2[ x + y ] = s[ x + t[ y ] ];
			if( x + y > 0  &&  s2[ x + y ] != s2[ x + y - 1 ] )
				res++;
	}
	
	result = min( result, res );
}


int main()
{
  int ilz;
  scanf("%i", &ilz);
  for(int xz=1; xz<=ilz; xz++)
  {
		scanf("%i", &k);
		scanf("%s", s);
		
		dl = strlen( s );
		
		for(int x=0; x<5; x++)
			t[ x ] = x;
		
		result = MAX;
		while ( next_permutation( t, t + k ) )
			go();
		go();
		
		printf("Case #%i: %i\n", xz, result);
	}
	return 0;
}