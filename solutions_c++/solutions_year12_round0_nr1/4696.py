#include <cstdio>
#include <fstream>
#include <cstring>

using namespace std;

int main() {
	
	FILE *fin, *fout;
	
	int T;
	char reference[27] = "yhesocvxduiglbkrztnwjpfmaq";
 	
	fin = fopen ( "A-small-attempt3.in", "r" );
	fout = fopen ( "SpeakingInTonguesAnswer.txt", "w" );
	
	fscanf ( fin, "%d\n", &T );
	
	for ( int t = 0; t < T; t ++ ) {
		
		char input[120];
		
		fgets ( input, sizeof ( input ), fin );
		
		for ( int i = 0; i < strlen( input ); i ++ ) {
			
			if ( input [i] >= 'a' && input [i] <= 'z' ) {
				input[i] = reference[ input[i] - 'a']; 
			} 
			
		}
	   	fprintf(fout, "Case #%d: %s", t+1, input);
	}
	
	return 0;
}