#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <string>
#include <vector>

using namespace std;
#pragma warning(disable: 4996)

typedef struct {
	int pos;
	int case_num;
} ELEM;

vector< vector<ELEM> > place;

void main(int argc, char*argv[])
{
	if( argc < 3 ){
		printf("usage: solv.exe in out\n");
		return;
	}

	FILE* fin = fopen(argv[1],"r");
	FILE* fout = fopen(argv[2],"w");
	if( fin == NULL ){
		printf("cannot open in-file : %s\n", argv[1]);
		return;
	}
	if( fin == NULL ){
		printf("cannot open out-file : %s\n", argv[2]);
		return;
	}
	/////////////////////////////
	char line[1024];
	int CASE;
	fgets(line,1024,fin);
	CASE = atoi(line);

	int start[512];
	int end[512];
	const char phrase[20] = "welcome to code jam";
	vector<ELEM> letter_place;
	vector<ELEM>::iterator it,it2;
	ELEM elem;
	int sum;

	for( int cs = 0; cs < CASE; cs++ ){
		fgets(line,1024,fin);
		int pos = 0;
		int line_size = strlen(line);
		place.clear();
		// start
		for( int letter = 0; letter < 19; letter++ ){
			while( pos < line_size ){
				if( line[pos] == phrase[letter] ){
					start[letter] = pos;
					pos++;
					break;
				}
				pos++;
			}
			if( pos == line_size ){
				sum = 0;
				goto finish;
			}
		}
		// end
		pos = line_size-1;
		for( int letter = 18 ; letter >= 0; letter-- ){
			while( pos >= 0 ){
				if( line[pos] == phrase[letter] ){
					end[letter] = pos;
					pos--;
					break;
				}
				pos--;
			}
		}
		/// 
		for( int letter = 0; letter < 19; letter++ ){
			letter_place.clear();
			for( pos = start[letter]; pos <= end[letter]; pos++ ){
				if( line[pos] == phrase[letter] ){
					elem.pos = pos;
					elem.case_num = 1;
					letter_place.push_back(elem);
				}
			}
			place.push_back(letter_place);
		}
		/// 
		for( int letter = 17; letter >= 0; letter-- ){
			for( it = place[letter].begin();it != place[letter].end(); it++ ){
				sum = 0;
				for( it2 = place[letter+1].begin(); it2 != place[letter+1].end(); it2++ ){
					if( it->pos < it2->pos ){
						sum += it2->case_num;
					}
				}
				sum %= 10000;
				it->case_num = sum;
			}
		}
		///
		sum = 0;
		for( it = place[0].begin();it != place[0].end(); it++ ){
			sum += it->case_num;
		}
		sum %= 10000;
		///
finish:
		fprintf(fout,"Case #%d: %04d\n", cs+1, sum );
	}
}
