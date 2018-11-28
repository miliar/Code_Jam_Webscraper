#include <iostream>
#include <algorithm>
#include <stdio.h>
using namespace std;


int num[2][1000];

int main()
{
	int t;
	int i,j;

	FILE *fp = fopen("out.txt", "wt");
	freopen( "A-small-attempt0.in", "rt", stdin );

	cin>>t;
	for(  i=0; i<t; i++ ){
		int n;
		cin>>n;
		for( j=0 ;j<n; j++ ) {
			cin>>num[0][j];
		}
		for( j=0 ;j<n; j++ ) {
			cin>>num[1][j];
		}

		sort( &num[0][0], &num[0][n] );
		sort( &num[1][0], &num[1][n] );

		long long ans=0;
		for( j=0; j<n; j++ )
			ans+=(num[0][j]*num[1][n-j-1]);

		fprintf(fp, "Case #%d: %ld\n", i+1, ans );

	}

	fclose(fp);
	return 0;
}