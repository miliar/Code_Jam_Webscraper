
#include <vector>
#include <stdlib.h>
#include <list>
#include <algorithm>
#include <stack>
#include <string>
#include <iostream>
#include <stdio.h>
#include <math.h>


using namespace std;

int compare (const void * a, const void * b)
{
  return ( -*(long long*)a + *(long long*)b );
}

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);




	int t;
	cin>>t;

	for (int tt = 1 ; tt <= t ; tt++)
	{
		int n;
		cin>>n;

		long long rez = 0;
		long long r = 0,in;
		long long xor_sum = 0;
		long long v[1001];
		int i = 0;

		for (int x = 0 ; x < n ; x++) 
		{
			cin>>in;
			v[i] = in;
			i++;
			xor_sum ^= in;
			if ( !xor_sum )
			{				
				qsort(v,i,sizeof(long long),compare);
				for (int x = 0 ; x < i - 1 ; x++) rez += v[x];
				i = 0;				
			}						
		}		
		printf("Case #%d: ",tt);
		if ( xor_sum ) printf("NO\n");
		else printf("%d\n",rez);
	}
}

