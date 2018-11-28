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
		int r,c;
		cin>>r>>c;

		char p[55][55] = {0,};
		for (int x = 0 ; x < r ; x++)
			for (int y = 0 ; y < c ; y++) cin>>p[x][y];

		for (int x = 0 ; x < r ; x++)
			for (int y = 0 ; y < c ; y++)
				if ( p[x][y] == '#' && p[x+1][y] == '#' && p[x][y+1] == '#' && p[x+1][y+1] == '#' )
				{
					p[x][y] = '/';
					p[x+1][y] = '\\';
					p[x][y+1] = '\\';
					p[x+1][y+1] = '/';
				}

		bool bad = 0;

		for (int x = 0 ; x < r ; x++)
			for (int y = 0 ; y < c ; y++)
			{
				if ( p[x][y] == '#' ) 
				{
					bad = 1;
					break;
				}
			}

			printf("Case #%d:\n",test);
			if (bad) printf("Impossible\n");
			else for (int x = 0 ; x < r ; x++) 
				{
					for (int y = 0 ; y < c ; y++) 
						printf("%c",p[x][y]);
					printf("\n");
			}		
	}
	return 0;
}

