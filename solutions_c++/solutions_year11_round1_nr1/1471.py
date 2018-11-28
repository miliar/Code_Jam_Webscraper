/*
 * main.cpp
 *
 *  Created on: 2011-04-28
 *      Author: ronanrmo
 */
#include <cstdio>

int main(int argc, char **argv)
{

	FILE *file_in, *file_out;


	// OPENING FILES ////////////////////////////////////////////////////////////////////

	// checking if first argument is not provided than redirect to stdin
	if(argc == 1){
		file_in = stdin;
	}
	// otherwise open file to write
	else{
		file_in   = fopen(argv[1], "r");
	}

	// checking if second argument is not provided than redirect to stdout
	if(argc < 3){
		file_out = stdout;
	}
	// otherwise open file to write
	else{
		file_out = fopen(argv[2], "w");
	}
	// END OPENING FILES ////////////////////////////////////////////////////////////////

	int T;
	fscanf(file_in, "%d", &T);

	for(int t=0; t<T; t++){
		int N, Pd, Pg;
		fscanf(file_in, "%d %d %d", &N, &Pd, &Pg);

//		printf("%d %d %d\n", N, Pd, Pg);

		bool possible = false;

		for(int k=1; k<=N; k++){
			float val1;
			int val2;
			float a = 0;

			val1 = k*Pd/100.0;
			val2 = k*Pd/100;
			a = val1 - val2;

			if(a == 0 && !possible){
				if((Pg == 100 && Pd < 100) || (Pg == 0 && Pd > 0))
					possible = false;
				else
					possible = true;
			}
		}


		if(possible)
			fprintf(file_out, "Case #%d: %s\n", t+1, "Possible");
		else
			fprintf(file_out, "Case #%d: %s\n", t+1, "Broken");
	}


//	fprintf(file_out, "num %d\n", num);



	return 0;
}
