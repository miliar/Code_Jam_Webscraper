#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define INF 999999
#define forn(i,n) for(int i=0;i<n;i++)


int main()
{
	char filename[32]="A-large";
	char infile[32], outfile[32];
//	scanf("%s", filename);
	strcpy ( infile, filename );
	strcpy ( outfile, filename );
	strcat ( infile, ".in" );
	strcat ( outfile, ".out" );
	FILE *ifp=freopen ( infile, "r",stdin );
	FILE *ofp=freopen ( outfile, "w",stdout );
	if ( ifp==NULL ) return -1;


	int T;
	scanf ( "%d",&T );
	int N,K;
	int rt;
	int a[30];
	int s;
	int d;
	int cnt;
	int j;
	forn ( t,T ) {
		memset(a,0,sizeof(a));
		rt=0;
		scanf ( "%d%d",&N,&K );
		s=K;
		cnt=0;
		while ( s ) {
			d=s%2;
			s=s/2;
			a[cnt++]=d;
		}
		for ( j=0;j<N;j++ ) {
//			printf ( "%d",a[j] );
			if ( a[j]==0 ) break;
		}
//		printf ( "\n" );
		if ( j==N ) rt=1;

		printf ( "Case #%d: %s\n", t+1, rt==1?"ON":"OFF" );

	}
	fclose ( ifp );
	fclose(ofp);
	return 0;
}
