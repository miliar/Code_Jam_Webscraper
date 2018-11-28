#pragma comment(linker, "/STACK:256000000")

#include <vector>
#include <stdlib.h>
#include <list>
#include <algorithm>
#include <stack>
#include <string>
#include <iostream>
#include <stdio.h>
#include <math.h>
#include <map>
#include <string.h>
#include <queue>

using namespace std;

int compare( const void* a, const void* b)
{
	long long aa = *((long long*)a);
	long long bb = *((long long*)b);
	if ( aa - bb < 0 ) return -1;
	else if ( aa == bb ) return 0; 
	else return 1;
}

int compare_i( const void* a, const void* b)
{
	return *(int*)a - *(int*)b;
}

int main()
{
	freopen("in.txt","r",stdin);  //(!!!!!!!!!!!!!!!!!!!!!!!!!!)
	freopen("out.txt","w",stdout);

	int T;
	cin>>T;
	for( int test = 1 ; test <= T ; test++ )
	{
		unsigned long long n,l,h;
		cin>>n>>l>>h;

		unsigned long long fr[10000];

		for (int x = 0 ; x < n ; x++) cin>>fr[x];

		for (int x = l ; x <= h ; x++)
		{
			for (int y = 0 ; y < n ; y++)
			{
				if ( fr[y] % x && x % fr[y] ) break;
				if ( y == n - 1 )
				{
					printf("Case #%d: %d\n",test,x);
					goto end;
				}
			}
		}

		printf("Case #%d: NO\n",test);

end:;



		
	}
	return 0;
}

