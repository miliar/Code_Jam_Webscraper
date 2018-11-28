#include<iostream>
#include<cmath>
#include<map>
#include<set>
#include<algorithm>
#include<cstdio>
#define MAX 100
using namespace std;
typedef pair< int, pair< int, int > >pp;
map< int, set< pp > >mx;
int mxv;
void preprocess()
{
	for( int i = 0; i <= 10; i++ )
	{
		for( int j = 0; j <= 10; j++ )
		{
			//if( abs( i - j ) > 2 )break;
			for( int k = 0; k <= 10; k++ )
			{
				//if( abs( j - k ) > 2 )break;
				if( abs( i - k ) <= 2 && abs( i - j ) <= 2 && abs( j - k ) <= 2)
				{
					int arr[] = {i, j, k };
					sort( arr, arr + 3 );
					mx[ i + j + k ].insert( pp( arr[0], make_pair( arr[1], arr[2] ) ) );
				}
			}
		}
	}
	return ;
}
void solve( int tsc[], int n, int s, int p, pp triplets[], int idx )
{
	if( idx > n  && s > 0 )return ;
	else if( s < 0 )return ;
	else if( idx > n && s == 0 )
	{
		int cnt = 0;
		for( int i = 1; i <= n; i++ )
		{
			if( triplets[i].second.second >= p )
			cnt += 1;
		}
		if( cnt > mxv )mxv = cnt;
		return ;
	}
	else
	{
		set< pp >sx = mx[ tsc[idx ] ];
		for( set< pp >::iterator iter = sx.begin(); iter != sx.end(); iter++ )
		{
			int surp = 0;
			pp curr = *iter;
			triplets[idx] = curr;
			
			if( (curr.second.first - curr.first) == 2 || ( curr.second.second - curr.second.first ) == 2 || ( curr.second.second - curr.first ) == 2 )
			surp = 1;		
				
			solve( tsc, n, s - surp, p, triplets, idx + 1 );
		}
		return ;
	}
	return ;
}
int main()
{
	
	preprocess();
	/*for( map< int, set< pp > >::iterator it = mx.begin(); it != mx.end(); it++ )
	{
		printf("%d-->", it->first );
		for( set< pp >::iterator iter = (it->second).begin(); iter != (it->second).end(); iter++ )
		printf("(%d, %d, %d)  ", iter->first, (iter->second).first, (iter->second).second );
		printf("\n");
	}*/
	int t;
	scanf("%d", &t );
	for( int tcase = 1; tcase <= t; tcase++ )
	{
		int n, s, p;
		int tsc[MAX];
		scanf("%d%d%d", &n, &s, &p );
		for( int i = 1; i <= n; i++ )
		scanf("%d", &tsc[i] );
		
		mxv = -1;
		pp triplets[MAX];
		
		solve( tsc, n, s, p, triplets, 1 );
		printf("Case #%d: %d\n",tcase, mxv );
	}
	return 0;
}
