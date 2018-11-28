/*
 * main.cpp
 *
 *  Created on: 2011-04-28
 *      Author: ronanrmo
 */
#include <cstdio>
#include <cmath>
#include <cstdlib>

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
//	fprintf(file_out, "num %d\n", T);

	for(int i=0; i<T; i++){
		int N;
		fscanf(file_in, "%d", &N);
//		fprintf(file_out,"%d ", N);

		int lastO = 1, lastB = 1;
		char previousRobot = ' ';
		int  previousTime = 0;
		int totalTime = 0;

		for(int j=0; j<N; j++){
			char R = ' ';
			int P;

			while(R == ' ')R = fgetc(file_in);

			fscanf(file_in, "%d", &P);
//			fprintf(file_out, "%c %d ", R, P);

			if(R == 'O'){
				int time = abs(P - lastO);
				lastO = P;

				if(previousRobot == 'O'){
					previousTime += time+1;
					totalTime += time+1;
				}else{
					if(time > previousTime){
						totalTime += time-previousTime+1;
						previousTime = time-previousTime+1;
					} else {
						totalTime += 1;
						previousTime = 1;

					}

				}
				previousRobot = 'O';
			}

			if(R == 'B'){
				int time = abs(P - lastB);
				lastB = P;

				if(previousRobot == 'B'){
					previousTime += time+1;
					totalTime += time+1;
				}else{
					if(time > previousTime){
						totalTime += time-previousTime+1;
						previousTime = time-previousTime+1;
					} else {
						totalTime += 1;
						previousTime = 1;

					}

				}
				previousRobot = 'B';
			}


		}
		fprintf(file_out, "Case #%d: %d\n",i+1, totalTime);
	}




	return 0;
}
