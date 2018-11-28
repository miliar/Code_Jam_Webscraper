#include <iostream>
#include <algorithm>
#include <cstdio>
using namespace std;

FILE* fp;
int m,v;

struct innernode
{
	int gate;
	int changable;
};

innernode inode[10005];
int nodev[10005];
int d[10005][2];

int minv( int a, int b, int c )
{
	return ( min( a, min(b,c) ) );
}

int recur( int node, int val )
{
	if( d[node][val] != -1 ) {
		return d[node][val];
	}


	//리프라면
	if( node > (m-1)/2 ) {
		d[node][val]=0;
		return d[node][val];
	}
	else {
		//이너노드

		int andv, orv;
		if( val == 1 ) {
			andv = recur( 2*node, 1 ) + recur( 2*node+1, 1 );
			orv = minv( recur( 2*node, 1 ) + recur( 2*node+1, 1 ),
				       recur( 2*node, 1 ) + recur( 2*node+1, 0 ),
					   recur( 2*node, 0 ) + recur( 2*node+1, 1 ) );
		}
		if( val == 0 ) {
			orv = recur( 2*node, 0 ) + recur( 2*node+1, 0 );
			andv = minv( recur( 2*node, 0 ) + recur( 2*node+1, 0 ),
				        recur( 2*node, 1 ) + recur( 2*node+1, 0 ),
				     	recur( 2*node, 0 ) + recur( 2*node+1, 1 ) );
		}

		int c_able = inode[node].changable;

		//and
		if( inode[node].gate == 1 ) {
			if( c_able==1 )
				d[node][val] = min( andv, orv+c_able );
			else
				d[node][val] = andv;
		}

		//or
		if( inode[node].gate == 0 ) {
			if( c_able==1 )
				d[node][val] = min( orv, andv+c_able );
			else
				d[node][val] = orv;
		}

		return d[node][val];
	}
	
}


void solve( int tcase )
{
	int i,j;
	for( i=0; i<=m; i++ )
	{
		d[i][0]=-1;
		d[i][1]=-1;
	}

	for( j=(m-1)/2+1; j<=m ; j++ ) {
		d[j][ 1-nodev[j] ] = 100000;
		d[j][ nodev[j] ] = 0;
	}


	int ans = recur( 1, v );

	if( ans<100000 )
		fprintf(fp, "Case #%d: %d\n", tcase, ans );
	else
		fprintf(fp, "Case #%d: IMPOSSIBLE\n", tcase );

}

int main()
{
	freopen("a-large.in","rt",stdin);
	fp = fopen("out.txt", "wt" );
	int tc;
	cin>>tc;

	for( int i=0; i<tc; i++ ) {
		cin>>m>>v;
		for( int j=1; j<=(m-1)/2; j++ ) {
			cin>>inode[j].gate>>inode[j].changable;
		}
		for( int j=(m-1)/2+1; j<=m ; j++ ) {
			cin>>nodev[ j ];
		}
		
		solve( i+1 );
		
	}
	fclose(fp);
	return 0;
}