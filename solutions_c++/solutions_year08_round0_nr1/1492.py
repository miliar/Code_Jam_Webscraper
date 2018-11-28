// Jacek Migdal 2008 Google gode jam
#include <cstdio>
#include <cstring>
#include <climits>
#include <algorithm>

using namespace std;

const int MAX_LENGTH = 128;
const int MAX_ENGINE = 128;

int nEngines;
char engineNames[MAX_ENGINE][MAX_LENGTH];
int cache[MAX_ENGINE];
char query[MAX_LENGTH];

int doIt() {
	scanf( "%d", &nEngines );
	fgets( query, MAX_LENGTH, stdin ); // get rid of trash
	for( int i = 0 ; i<nEngines ; i++ ) {
		fgets( engineNames[i], MAX_LENGTH, stdin );
		cache[i] = 0;
	}
	int nQuery;
	scanf( "%d", &nQuery );
	fgets( query, MAX_LENGTH, stdin ); // get rid of trash
	for( int i = 0 ; i<nQuery ; i++ ) {
		fgets( query, MAX_LENGTH, stdin );
		for( int j = 0 ; j<nEngines ; j++ ) {
			//printf( "%s '%s'\n", query, engineNames[j] );
			if( strcmp(query, engineNames[j])==0 ) {
				cache[j] = INT_MAX-10;
				for( int k = 0 ; k<nEngines ; k++ ) {
					cache[j] = min(cache[j], cache[k]+1);
				}
				break;
			}
		}
	}

	int result = cache[0];
	for( int i = 0 ; i<nEngines ; i++ ) {
		result = min(result, cache[i]);
	}
	return result;
}

int main() {
	int nTests;
	scanf("%d", &nTests);
	for( int i = 1 ; i<=nTests ; i++ ) {
		printf( "Case #%d: %d\n", i, doIt() );
	}
	return 0;
}
