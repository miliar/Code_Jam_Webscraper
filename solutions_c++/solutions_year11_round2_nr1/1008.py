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
		int n;
		cin>>n;
		char ch;
		char m[102][102];
		for (int x = 0 ; x < n ; x++)
		{
			for (int y = 0 ; y < n ; y++)
				cin>>m[x][y];
		}

		int win[102] = {0,},all[102] = {0,};

		double wp[102];

		for (int x = 0 ; x < n ; x++)
		{
			for (int y = 0 ; y < n ; y++)
			{
				if ( m[x][y] == '1' ) win[x]++;
				if ( m[x][y] != '.' ) all[x]++;
			}
			wp[x] = (double) win[x] / (double) all[x];
		}

		double wps = 0;

		double owp[102];

		double owpsum = 0;

		int k;


		for (int x = 0 ; x < n ; x++)
		{
			wps = 0;
			k = 0;
			for (int y = 0 ; y < n ; y++)
			{
				if ( y != x )
				{
					if ( m[y][x] == '1' )
					{
						wps += (double) ( win[y] - 1 ) / ( all[y] - 1 );
						k++;
					}
					if ( m[y][x] == '0' )
					{
						wps += (double) ( win[y] ) / ( all[y] - 1 );
						k++;
					}
					//if ( m[y][x] == '.' ) wps += wp[y];
				}
			}
			
			owp[x] = (double) wps / (double) k;			
		}

		double oowp[102];

		double owps;


		for (int x = 0 ; x < n ; x++)
		{
			k = 0;
			owps = 0;
			for (int y = 0 ; y < n ; y++)
			{
				if ( m[x][y] != '.' ) 
				{
					owps += owp[y];
					k++;
				}
			}

			oowp[x] = (double) owps / (double) k;
		}

		printf("Case #%d:\n",test);
		for (int x = 0 ; x < n ; x++)
			printf("%.12lf\n", 0.25 * (wp[x] + oowp[x] ) + 0.5 * owp[x] );
	}
	return 0;
}

