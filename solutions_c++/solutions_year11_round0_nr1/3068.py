// qual_1.cpp : Defines the entry point for the console application.
//

#include<stdio.h>
#include<memory.h>
#include<string.h>

void main(){

	char filename[32];
	char infile[32], outfile[32];
	scanf("%s", filename);
	strcpy(infile, filename); strcpy(outfile, filename);
	strcat(infile, ".in"); strcat(outfile, ".out");
	FILE *fp=fopen(infile, "r"), *ofp=fopen(outfile, "w");

	int tc;
	int i, j, n, o[300], b[300], oCounter, bCounter, oPos, bPos, tot[300], totCounter, step, temppos, oStep, bStep, value, time;
	char c, totc[300], tempc;
	bool pushed = false;

	fscanf(fp, "%d", &tc);

	for(i=0; i<tc; i++){
		fscanf(fp, "%d", &n);
		oCounter = 0;
		bCounter = 0;
		totCounter = 0;
		for(j=0; j<n; j++){
			fscanf(fp, "%s %d", &c, &value);
			if(c == 'O'){
				//fscanf(fp, "%d", &o[oCounter]);
				o[oCounter] = value;
				totc[totCounter] = 'O';
				tot[totCounter] = o[oCounter];
				totCounter++;
				oCounter++;
			}
			else{
				//fscanf(fp, "%d", &b[bCounter]);
				b[bCounter] = value;
				totc[totCounter] = 'B';
				tot[totCounter] = b[bCounter];
				totCounter++;
				bCounter++;
			}
		}
		oPos = 1;
		bPos = 1;
		step = 0;
		oStep = 0;
		bStep = 0;
		time = 0;
		printf("for case %d\n", i+1);
		while(step < n){
			printf("at time : %d\n", time+1);
			if(totc[step] == 'O'){
				if(tot[step] > oPos){
					oPos++;
					printf("O moved to %d\n", oPos);
				}
				else if(tot[step] < oPos){
					oPos--;
					printf("O moved to %d\n", oPos);
				}
				else{
					step++; //O has pushed the button
					printf("O pushed button at %d\n", oPos);
					oStep++;
				}
				if(bStep < bCounter){
					if(b[bStep] > bPos){
						bPos++;
						printf("B moved to %d\n", bPos);
					}
					else if(b[bStep] < bPos){
						bPos--;
						printf("B moved to %d\n", bPos);
					}
				}
				time++;
			}
			else{
				if(tot[step] > bPos){
					bPos++;
					printf("B moved to %d\n", bPos);
				}
				else if(tot[step] < bPos){
					bPos--;
					printf("B moved to %d\n", bPos);
				}
				else{
					step++; //B has pushed the button
					printf("B pushed button at %d\n", bPos);
					bStep++;
				}
				if(oStep < oCounter){
					if(o[oStep] > oPos){
						oPos++;
						printf("O moved to %d\n", oPos);
					}
					else if(o[oStep] < oPos){
						oPos--;
						printf("O moved to %d\n", oPos);
					}
				}
				time++;
			}
		}
		printf("Case #%d: %d\n", i+1, time);
		fprintf(ofp, "Case #%d: %d\n", i+1, time);
	}

	totCounter = 0;
	fclose(ofp);
			

}

