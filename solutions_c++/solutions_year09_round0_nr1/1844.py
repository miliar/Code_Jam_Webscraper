#include <iostream>
#include <cmath>
#include <cstring>
#include <string>
#include <vector>
using namespace std;

int n,d,l;
vector < string > vs;
string s;
int was[256][256];

int main()
{
	freopen( "input.txt", "r", stdin );
	freopen( "output.txt", "w", stdout );
	
	scanf("%d%d%d\n",&l,&d,&n);
	vs.assign( d, "" );
	
	for(int i = 0; i < d; i++)
	{
		getline( cin, vs[i] );
	}
	
	for(int i = 0; i < n; i++)
	{
		getline( cin, s );
		memset( was, 0, sizeof was );
		
		int m = 0;
		for(int j = 0; j < (int)s.length(); j++)
		{
			was[m][ s[j] ] = 1;
			if( s[j] == '(' )
			{
				while( s[j] != ')' )
				{
					j++;
					was[m][ s[j] ] = 1;
				}
			}
			m++;
		}
		
		if( m != l )
		{
			printf("Case #%d: %d\n",i+1,0);
			continue;
		}
		
		int res = 0;
		for(int j = 0; j < d; j++)
		{
			res++;
			for(int x = 0; x < (int)vs[j].length(); x++)
				if( was[x][ vs[j][x] ] == 0  )
				{
					res--;
					break;
				}
		}
		
		printf("Case #%d: %d\n",i+1,res);
		
	}
	
	return 0;
}
