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
		unsigned long long l,t,n,c;
		cin>>l>>t>>n>>c;
		unsigned long long a[1001];
		for (int x = 0 ; x < c ; x++) cin>>a[x];

		unsigned long long time[2][100003]={0,};

		unsigned long long *t1,*t2;

		t1 = &time[0][0];
		t2 = &time[1][0];

		int tel = 0;
		
		for (int x = 0 ; x < n ; x++)
		{
			t2[0] = t1[0] + a[x % c] * 2;
			for (int y = 0 ; y <= tel && y < l; y++)
			{
				if ( t <= t1[y] )
				{
					t2[y+1] = min( t1[y] + a[x%c] , ((t1[y+1] == 0)?(t1[y] + a[x%c]):( t1[y+1] + a[x%c] * 2)));
				
					if ( y == tel ) 
					{
						tel++;
						break;
					}
				} else
				{
					if ( t < a[x%c] * 2 + t1[y] )
					{
						t2[y + 1 ] = t + (a[x%c] - (t-t1[y])/2);
						if ( y == tel ) 
						{
							tel++;
							break;
						}
					}					
				}
			}
			/*
			printf("from ");
			for (int y = 0 ; y <= l + 2 ; y++) cout<<t1[y]<<" ";
			printf("\nti ");
			for (int y = 0 ; y <= l + 2 ; y++) cout<<t2[y]<<" ";
			printf("\n");
			*/
			
			
			
			
			swap(t1,t2);
		}

		unsigned long long m = 0;
		bool first = 1;


		for (int x = 0 ; x <= tel; x++) if (first || t1[x] < m ) 
		{
			m = t1[x];
			first = 0;
		}

		printf("Case #%d: ",test); cout<<m<<endl;
	}
	return 0;
}

