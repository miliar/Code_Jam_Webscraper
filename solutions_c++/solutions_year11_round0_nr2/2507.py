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


	for(int i=0; i<T; i++){
		int C;
		fscanf(file_in, "%d", &C);
		char combine[C][4];
		// populate combine
		for(int j=0; j<C; j++){
			fscanf(file_in, "%s", combine[j]);
//			fprintf(file_out, "%s ", combine[j]);
		}

		int D;
		fscanf(file_in, "%d", &D);
		char opposed[D][3];
		// populate opposed
		for(int j=0; j<D; j++){
			fscanf(file_in, "%s", opposed[j]);
//			fprintf(file_out, "%s ", opposed[j]);
		}

		int N;
		fscanf(file_in, "%d", &N);
		char list[N+1];
		char result[N+1];
		for(int j=0; j<N+1; j++)
			result[j] = 0;

		fscanf(file_in, "%s", list);
//		fprintf(file_out, "%s\n", list);

		// checking
		int resultcounter = 0;
		for(int j=0; j<N; j++){
			if(resultcounter>0){
				// test combines
				bool combined = false;
				for(int k=0; k<C; k++){
					if((list[j] == combine[k][0] && result[resultcounter-1] == combine[k][1]) ||  (list[j] == combine[k][1] && result[resultcounter-1] == combine[k][0])){
						result[resultcounter-1] = combine[k][2];
//						resultcounter++;
//						fprintf(file_out, "COMBINEDDDDDDDDDDDDDD %c\n", combine[k);
						combined = true;
						break;
					}
				}
				if(!combined){
					result[resultcounter] = list[j];
					resultcounter++;
				}

				// test opposed
//				if(!combined)
				for(int k=0; k<D; k++){
					for(int q=resultcounter-1; q>=0; q--){
						if((result[resultcounter-1] == opposed[k][0] && result[q] == opposed[k][1]) || (result[resultcounter-1] == opposed[k][1] && result[q] == opposed[k][0])	){
							for(int j=0; j<N+1; j++) result[j] = 0;
							resultcounter=0;
							break;
						}
					}

				}

			}else{
				result[0] = list[j];
				resultcounter++;
			}
		}
		fprintf(file_out, "Case #%d: [", i+1);
		for(int j=0; j<resultcounter-1; j++)
			fprintf(file_out, "%c, ", result[j]);
		if(resultcounter != 0)
			fprintf(file_out, "%c", result[resultcounter-1]);
		fprintf(file_out, "]\n");

	}


	return 0;
}
