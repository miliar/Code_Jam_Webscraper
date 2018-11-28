#include <cstdio>
#include <iostream>
#include <cstring>
#include <cmath>
#include <string>
#include <cstdlib>
#include <map>
#include <queue>
#include <algorithm>
#include <sstream>
#include <vector>

using namespace std;

int n, K;
char M[100][100],MM[100][100];

int calc( int x, int y, int dx, int dy ){
	int ret=0;
	char c=M[x][y];
	while ( x>=0 && x<n && y>=0 && y<n && M[x][y]==c ){
		++ret; x+=dx; y+=dy;
	}
	return ret-1;
}

int main(){
	int test=0;
	scanf("%d", &test);
	for ( int T=1; T<=test; ++T ){
		scanf("%d %d", &n, &K); --K;
		for ( int i=0; i<n; ++i ){
			char junk; scanf("%c", &junk);
			for ( int j=0; j<n; ++j ){
				char c;
				scanf("%c", &MM[i][j]);
			}
		}
		for ( int i=0; i<n; ++i )
			for ( int j=n-1; j>=0; --j )
				M[i][n-j-1]=MM[j][i];
		for ( int i=n-2; i>=0; --i )
			for ( int j=0; j<n; ++j )
				if ( M[i][j]!='.' ){
					int x=i+1;
					while ( x<n && M[x][j]=='.' ){
						M[x][j]=M[x-1][j]; M[x-1][j]='.'; ++x;
					}
				}
		/*for ( int i=0; i<n; ++i ){
			for ( int j=0; j<n; ++j )
				printf("%c",M[i][j]);
			printf("\n");
		}*/
		bool ok1=false, ok2=false;
		for ( int i=0; i<n; ++i )
			for ( int j=0; j<n; ++j )
				if ( M[i][j]!='.' ){
					int a=calc(i,j,0,-1)+calc(i,j,0,1);
					if ( a>=K )
						if ( M[i][j]=='R' ) ok1=true; else ok2=true;
					a=calc(i,j,-1,-1)+calc(i,j,1,1);
					if ( a>=K )
						if ( M[i][j]=='R' ) ok1=true; else ok2=true;
					a=calc(i,j,1,-1)+calc(i,j,-1,1);
					if ( a>=K )
						if ( M[i][j]=='R' ) ok1=true; else ok2=true;
					a=calc(i,j,-1,0)+calc(i,j,1,0);
					if ( a>=K )
						if ( M[i][j]=='R' ) ok1=true; else ok2=true;
				}
		if ( ok1 && ok2 )
			printf("Case #%d: Both\n", T);
		else
			if ( ok1 )
				printf("Case #%d: Red\n", T);
			else
				if ( ok2 )
					printf("Case #%d: Blue\n", T);
				else
					printf("Case #%d: Neither\n", T);
	}
}
