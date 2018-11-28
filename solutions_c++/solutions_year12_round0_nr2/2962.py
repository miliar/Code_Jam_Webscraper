#define _CRT_SECURE_NO_DEPRECATE

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

int i,j,k;
int T;
int ans;
int N, S,p;
int t[1000];

int main( )
{
	freopen( "B-large.in", "r", stdin );
	freopen( "B-large.out", "w", stdout );


	scanf("%d",&T);

	for(i=1;i<=T;i++)
	{
		ans = 0;

		scanf("%d%d%d",&N,&S,&p);
		for(j=0;j<N;j++)
		{
			scanf("%d",&t[j]);
			
			if(t[j] % 3 == 0)
			{
				if(t[j] / 3 >= p)  ans ++;

				else if(t[j] / 3 + 1 >= p && S > 0 && t[j] /3 -1 >=0) { ans ++; S --; }
			}
			else if((t[j] +1) % 3 == 0)
			{
				if((t[j] + 1) / 3 >= p && (t[j] + 1) / 3  - 1 >= 0) ans ++;
				else if( ( (t[j] + 4) / 3 ) >= p && S > 0 && (t[j]+4)/3 - 2 >= 0 ) { ans ++; S --; }
			}
			else
			{
				if((t[j] + 2) / 3 >= p && (t[j] + 2 ) / 3 - 1 >= 0) ans ++;
			}
		}

		printf("Case #%d: %d\n",i,ans);
		
		
	}

	return 0;
}
