#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <string>
#include <map>

using namespace std;



// Queries - Search Engines
int tab[1005][105];

map <string, int> engines;
int engine_cnt;
int engine_max;

char line[1024];

int queries_cnt;
int queries_max;

int main ( int argc, char ** argv ) {
	int cases;
	int case_cnt;

	scanf("%d", &cases);

	for (case_cnt = 0; case_cnt < cases; case_cnt++) {

		memset( tab, 0, sizeof(tab) );

		scanf("%d", &engine_max);
		fgets( line, 1024, stdin );

		engines.clear();
		engine_cnt = 0;
		for (engine_cnt = 0; engine_cnt < engine_max; engine_cnt ++) {

			fgets( line, 1024, stdin );
			if ( line[strlen(line)-1] == '\n') {
				line[strlen(line)-1] = '\0';
			}

			string name( line );

			engines[line] = engine_cnt;
		}

		scanf("%d", &queries_max);
		fgets( line, 1024, stdin );
		for ( queries_cnt = 0; queries_cnt < queries_max; queries_cnt++ ) {

			fgets( line, 1024, stdin );	
			if ( line[strlen(line)-1] == '\n') {
				line[strlen(line)-1] = '\0';
			}

			string name ( line );
			
			int engine_now = engines[line];
			tab[queries_cnt][engine_now] = -1;
	
			if ( queries_cnt == 0 ) continue;

			for ( int check = 0; check < engine_max; check++ ) {

				if ( check == engine_now ) continue;

				/* Am besten einfach so lassen.. */
				if ( tab[queries_cnt-1][check] != -1)  {
					tab[queries_cnt][check] = tab[queries_cnt-1][check];
					continue;
				}

				/* Okay, nun müssen wir uns was raussuchen */
				int min = 2000;
				for ( int better = 0; better < engine_max; better++) {
					if ( tab[queries_cnt-1][better] == -1 ) continue;
					if ( tab[queries_cnt-1][better] + 1 < min ) {
						min = tab[queries_cnt-1][better] + 1;
					}
				}

				tab[queries_cnt][check] = min;
			}

			/*
			printf("Query #%d, Engine is %d:\n", queries_cnt, engine_now );
			for (int y=0; y<engine_max; y++) {
				printf("Engine %d: ",y);
				for (int x=0; x<queries_max; x++) {
					printf("%2d", tab[x][y]);
				}
				printf("\n");
			}
			*/
				
		}

		int min = 2000;
		for (int x=0; x<engine_max; x++) {
			if ( tab[queries_max-1][x] == -1 ) continue;
			if ( tab[queries_max-1][x] < min ) {
				min = tab[queries_max-1][x];
			}
		}
		printf("Case #%d: %d\n", case_cnt+1, min);
		
	}
	return 0;
}
