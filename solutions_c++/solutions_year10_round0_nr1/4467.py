#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <string>
#include <vector>
#include <iostream>
#include <sstream>

using  namespace std;
#pragma warning(disable: 4996)

vector<bool>	states;

void Snap(int index, int max ){
	if( index < max ){
		if( states[index] ){
			Snap( index+1, max );
			states[index]	= false;
		}else{
			states[index]	= true;
		}
	}
}

void main(int argc, char* argv[]){
	int i;
	FILE* fin = fopen( argv[1],"r" );
	FILE* fout = fopen( argv[2],"w" );
	if( fin == NULL ){
		return;
	}
	if( fout == NULL ){
		return;
	}

	char line[1024];
	int CASE, N, K;
	fgets( line, 1024, fin );
	CASE = atoi(line);

	stringstream	ss;
	int				no;
	cout << "case " << CASE << "\n";
	for( int i = 0; i < CASE; i++ ){
		fgets( line, 1024, fin );
		sscanf( line, "%d %d", &N, &K );
		
		states.clear();
		for( no = 0; no < N; no++ ){
			states.push_back( false );
		}

		for( int snapNum = 0; snapNum < K; snapNum++ ){
			Snap( 0, N );
		}

		// ‘‚«ž‚Ý
		bool on = true;
		ss.str("");
		ss << "Case #" << (i+1) << ": ";
		for( no = 0; no < N; no++ ){
			if( states[no] == false ){
				on	= false;
				break;
			}
		}
		ss << ( on ? "ON\n" : "OFF\n" );
		fputs( ss.str().c_str(), fout );
	}
	
	fclose( fin );
	fclose( fout );

}