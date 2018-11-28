#include <stdio.h>
#include <stdlib.h>

int main(int argc, char * argv[]){
	FILE *f  = fopen(argv[1],"r");
	FILE *fop  = fopen("d:\\testgoo\\op.txt","w");
	int T1;
	char T[6];
	fgets(T,6,f);
	T1 = atoi(T); 

	for (int i = 0; i < T1; i++){

		int sucDancers = 0;
		int numOfGoo = 0;
		fscanf(f,"%d",&numOfGoo);
		int numSup = 0;
		fscanf(f,"%d",&numSup);
		int bestScore= 0;
		fscanf(f,"%d",&bestScore);

		int dancer = 0;
		for (int j = 0; j < numOfGoo; j++){
			fscanf(f,"%d",&dancer);
			int avgScore = dancer / 3;
			if (dancer % 3 == 0){
				if ( avgScore >= bestScore)
					sucDancers++;
				else if (avgScore +1 >= bestScore && numSup > 0 && avgScore != 0){
					sucDancers++;
					numSup--;
				}
			}
			else if (dancer % 3 == 1 && avgScore != 0){
				if ( avgScore + 1 >= bestScore)
					sucDancers++;
			}
			else {
				if ( avgScore + 1 >= bestScore)
					sucDancers++;
				else if ( avgScore + 2 >= bestScore && numSup > 0){
					sucDancers++;
					numSup--;
				}
			}
		}
		fprintf(fop,"Case #%d: %d\n", i+1, sucDancers);


	}
	fclose(f);
	fclose(fop);
	return 0;
}