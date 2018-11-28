#include <stdio.h>
#include <stdlib.h>


int main(int argc, char *argv[]){
	FILE *fin = fopen(argv[1],"r");
	int casos ;
	fscanf(fin,"%d\n",&casos);
	for(int caso=1;caso<=casos;++caso){
		int seconds = 0;
		int numButtons ;
		fscanf(fin,"%d ",&numButtons);
		
		int positionO=1, positionB=1;
		int secondsO = 0, secondsB= 0, lastSeconds =0;
		for(int i=0;i<numButtons;++i){
			char robot; int position;
			fscanf(fin,"%c %d ",&robot,&position);
			lastSeconds = seconds;
			if(robot == 'O'){
				seconds = secondsO+abs(positionO-position)+1;
				positionO = position;
				secondsO = seconds;
				if(seconds <= lastSeconds){
					seconds = lastSeconds+1;
					secondsO = seconds;
				}
			}else if(robot == 'B'){
				seconds = secondsB+abs(positionB-position)+1;
				positionB = position;
				secondsB = seconds;
				if(seconds <= lastSeconds){
					seconds = lastSeconds+1;
					secondsB = seconds;
				}
			}
			if(seconds <= lastSeconds){
				seconds = lastSeconds+1;
			}

			//fprintf(stdout,"PositionO %d PositionB %d seconds %d\n",positionO, positionB, seconds);

		}
		fprintf(stdout,"Case #%d: %d\n",caso,seconds);
	}

	fclose(fin);
	return 0;
}
