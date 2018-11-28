#include <stdio.h>
#include <string>
#include <vector>
using namespace std;


int main() {
	int T;
	int N, C, D;
	string n;
	int c[26][26], d[26][26];
	char s[200];

	scanf("%d",&T);
	for( int t=1; t<=T; t++ ) {
		memset( c, 0, sizeof(c) );
		memset( d, 0, sizeof(d) );
		n = "";

		scanf("%d",&C);
		for( int cc=0; cc<C; cc++ ) {
			scanf("%s", s);
			c[ s[0]-'A' ][ s[1]-'A' ] = s[2];
			c[ s[1]-'A' ][ s[0]-'A' ] = s[2];
		}

		scanf("%d",&D);
		for( int dd=0; dd<D; dd++ ) {
			scanf("%s", s);
			d[ s[0]-'A' ][ s[1]-'A' ] = 1;
			d[ s[1]-'A' ][ s[0]-'A' ] = 1;
		}

		scanf("%d",&N);
		scanf("%s", s);
		for( int i=0; i<N; i++ ) {
			if( n.size() == 0 ) n += s[i];
			else {
				if( c[ n[n.size()-1]-'A' ][ s[i]-'A' ] ) {
					n[n.size()-1] = (char) c[ n[n.size()-1]-'A' ][ s[i]-'A' ] ;
					continue;
				}

				int j=0;
				for( ; j<n.size(); j++ ) {
					if( d[ n[j]-'A' ][ s[i]-'A' ] ) {
						break;
					}
				}
				if( j != n.size() ) {
					n="";
					continue;
				}

				n += s[i];
			}
		}

		printf("Case #%d: ", t);
		printf("[");
		for( int i=0; i<n.size(); i++ ) {
			printf("%c", n[i]);
			if( i != n.size()-1 )
				printf(", ");
		}
		printf("]\n");
	}

	return 0;
}