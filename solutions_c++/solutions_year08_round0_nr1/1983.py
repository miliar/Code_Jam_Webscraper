#include <stdio.h>
#include <iostream>
#include <string>
using namespace std;

int main() {
	int i,j,inst,n,s,q,max,sw,pivoteFila, pivoteCol;
	int cest[102][12];
	string query,engine[12];
	char tmp[128];

	for( i=0; i<102; i++ ) cest[0][i] = 0;

	cin>>n;
	for( inst=1; inst<=n; inst++ ) {
		cin>>s; cin.ignore();
		for( i=0; i<s; i++ ) {
			getline( cin, engine[i] );
			if( engine[i].length() < 1 ) i--;
		}
		cin>>q; cin.ignore();
		for( i=1; i<=q; i++ ) {
				getline( cin, query );
				if( query.length() < 1 ) i--;
				else {
					for( j=0; j<s; j++ ) {
						if ( query == engine[j] )
							cest[i][j] = 0;
						else cest[i][j] = 1+cest[i-1][j];
					}
				}
		}
		pivoteFila = q;
		pivoteCol = -1;
		sw=-1;
		while( pivoteFila ) {
			sw++;
			max = -1;
			for( j=0; j<s; j++ ) {
				if( j!=pivoteCol && cest[pivoteFila][j] > max ) {
					max = cest[pivoteFila][j];
					pivoteCol = j;
				}
			}
			if( max>0 ) pivoteFila-=max;
			else pivoteFila--;
		}
		if( sw>-1 ) printf("Case #%d: %d\n",inst,sw);
		else printf("Case #%d: 0\n",inst);
	}
	return 0;
}
