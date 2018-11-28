#include<stdio.h>
#include<vector>
#include<iostream>
#include<map>
#include<set>
#include<sstream>
#include<algorithm>
#include<math.h>
#include<stdlib.h>

using namespace std;

typedef pair<long long,long long> ii;

int main()
{
	int tc;
	scanf("%d",&tc);
	int peoples[2000];
	long long r;
	long long k;
	long long n;
	int i;
	int j;
	long long S=0;
	int index=0;
	int flag=0;
	long long Euros=0;
	int ct=1;
	int comp=0;
	while( tc -- )
	{
		scanf("%lld%lld%lld",&r,&k,&n);
		for( i = 0 ; i < n ; i++ )
			scanf("%d",&peoples[i]);
		vector< ii > V( n,ii( 0 , 0 ));
		Euros=0;
		for( i = 0 ; i < n ; i++ )
		{
			S=0;
			index=0;
			flag=0;
			comp=0;
			for( j = i ; ;j++ )
			{
				if( j == n && comp == n )
				{flag=1;index=0;break;}
				else if( j== n )
					break;
				else if( S + peoples[j] > k )
				{flag=1;index=j;break;}
				else
				{
					S+=peoples[j];
					comp++;
				}
			}
			if( flag == 0  )
			{
				for( j=0;;j++)
				{
					if( j == i )
					{ index = i ;break; }
					else if( S+ peoples[j] > k )
					{index=j;break;}
					else
					{
						S+=peoples[j];
						comp++;
					}
				}
			}
			V[i]= ii(S ,index);
		}
		S=0;
		for( i = 0 ; i < r ;i++ )
		{
			Euros+=V[S].first;
			S=V[S].second;
		}
		printf("Case #%d: %lld\n",ct,Euros);
		ct++;
	}	
	return 0;
}





