#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <string>
#include <vector>

using namespace std;

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
	int L,D,N;
	fgets(line,1024,fin);
	sscanf(line, "%d %d %d", &L, &D, &N);

	vector<string> words;
	vector< vector<string> > patterns;

	for( int i = 0; i < D; i++ ){
		fgets(line,1024,fin);
		words.push_back(line);
	}
	for( int i= 0; i < N; i++ ){
		fgets(line,1024,fin);
		char* p = line;
		vector<string> pattern;
		int line_length = strlen(line);
		for( int j = 0; j < line_length; j++ ){
			string elem;
			if( *p == '(' ){
				p++;
				j++;
				char* start = p;
				while( *p != ')' ){
					p++;
					j++;
				}
				*p = '\0';
				elem = start;
			}else{
				elem = *p;
			}
			pattern.push_back(elem);
			p++;
		}
		patterns.push_back(pattern);
	}

	////
	for( int cs = 0; cs < N; cs++ ){
		int unmatch = 0;
		for( int wd = 0; wd < D; wd++ ){
			for( int f = 0; f < L; f++ ){
				if( patterns[cs][f].find(words[wd][f]) == string::npos ){
					unmatch++;
					break;
				}
			}
		}
		fprintf(fout, "Case #%d: %d\n", cs+1, D-unmatch);
	}
}