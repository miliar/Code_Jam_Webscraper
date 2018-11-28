#include <iostream>
#include <string.h>
#include <algorithm>
#include <stdio.h>
#include <string>
using namespace std;

FILE* fp;
int k;
char s[1005];

int cnt;
bool used[5];
int perm[150][5];
int made[5];
void recur( int num )
{
	if( num==0 ) {
		for( int i=0; i<k; i++ ) {
			perm[cnt][i]= made[i];
		}
		cnt++;
	}
	else {
		for ( int i=0; i<k; i++ ) 
		{
			if( used[i]==false ) {
				used[i]=true;
				made[k-num]=i;

				recur( num-1 );

				made[k-num]=-1;
				used[i]=false;
			}
		}
	}
}

void solve( int tcase)
{
	int i,j,kk;
	
	for( i=0; i<k; i++ ) {
		used[i]=false;
		made[i]=-1;
	}

	cnt=0;
	recur( k );

	char comp[1005];
	int min_g=100000;

	for( i=0; i<cnt; i++ )
	{
		for( j=0; j<strlen(s)/k; j++ )
		{
			for( kk=0; kk<k; kk++ ) {
				comp[j*k + perm[i][kk] ] = s[j*k+kk];
			}
		}

		int group=1;
		for( j=1; j<strlen(s); j++ ) {
			if( comp[j]!=comp[j-1] ) {
				group++;
			}
		}

		min_g = min( min_g, group );
	}

	fprintf(fp, "Case #%d: %d\n", tcase, min_g );


	
}


int main()
{
	freopen("D-small-attempt0.in","rt",stdin);
	fp = fopen("out.txt", "wt" );
	int tc;
	cin>>tc;
	for( int i=0; i<tc; i++ ) 
	{
		cin>>k;
		cin>>s;
		
		solve(i+1);

		
	}

	fclose(fp);
	return 0;
}