// qual_2_small.cpp : Defines the entry point for the console application.
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
	int i, j, k, l, c, d, n, count;
	char stringc[10], stringd[10], stringn[20], combine[3], oppose[2], q[10];
	int oppose0, oppose1, comb0, comb1;

	fscanf(fp, "%d", &tc);

	//Q-0 W-1 E-2 R-3 A-4 S-5 D-6 F-7

	for(i=0; i<tc; i++){
		fscanf(fp, "%d", &c);
		for(j=0; j<c; j++){
			fscanf(fp, "%s", stringc);
			combine[0] = stringc[0];
			combine[1] = stringc[1];
			combine[2] = stringc[2];
		}
		fscanf(fp, "%d", &d);
		for(j=0; j<d; j++){
			fscanf(fp, "%s", stringd);
			oppose[0] = stringd[0];
			oppose[1] = stringd[1];
		}
		fscanf(fp, "%d", &n);
		fscanf(fp, "%s", stringn);
		count = 0;
		oppose0 = 0;
		oppose1 = 0;
		for(j=0; j<n; j++){
			q[count] = stringn[j];
			count++;			
			if(q[count-1] == oppose[0]) oppose0++;
			if(q[count-1] == oppose[1]) oppose1++;
			if(count>0){
				if(q[count-1] == combine[0]){
					if(q[count-2] == combine[1]){
						if(oppose[0] == q[count-1] || oppose[0] == q[count-2]) oppose0--;
						if(oppose[1] == q[count-1] || oppose[1] == q[count-2]) oppose1--;
						count--;
						q[count-1] = combine[2];
					}
				}
				else if(q[count-1] == combine[1]){
					if(q[count-2] == combine[0]){
						if(oppose[0] == q[count-1] || oppose[0] == q[count-2]) oppose0--;
						if(oppose[1] == q[count-1] || oppose[1] == q[count-2]) oppose1--;
						count--;
						q[count-1] = combine[2];
					}
				}
			}
			if(oppose0 > 0 && oppose1 > 0){
				count = 0;
				oppose0 = 0;
				oppose1 = 0;
			}
		}
		printf("Case #%d: [", i+1);
		fprintf(ofp, "Case #%d: [", i+1);
		for(j=0; j<count-1; j++){
			printf("%c, ", q[j]);
			fprintf(ofp, "%c, ", q[j]);
		}
		if(count != 0){
			printf("%c", q[count-1]);
			fprintf(ofp, "%c", q[count-1]);
		}
		printf("]\n");
		fprintf(ofp, "]\n");
		combine[0] = 3;
		combine[1] = 3;
		combine[2] = 4;
		oppose[0] = 4;
		oppose[1] = 4;
		q[0] = 5;
		q[1] = 5;
		q[2] = 5;
		q[3] = 5;
		q[4] = 5;
		q[5] = 5;
		q[6] = 5;
		q[7] = 5;
		q[8] = 5;
		q[9] = 5;
		stringn[0] = 6;
		stringn[1] = 6;
		stringn[2] = 6;
		stringn[3] = 6;
		stringn[4] = 6;
		stringn[5] = 6;
		stringn[6] = 6;
		stringn[7] = 6;
		stringn[8] = 6;
		stringn[9] = 6;
		stringn[10] = 6;
		stringn[11] = 6;
		stringn[12] = 6;
		stringn[13] = 6;
		stringn[14] = 6;
		stringn[15] = 6;
		stringn[16] = 6;
		stringn[17] = 6;
		stringn[18] = 6;
		stringn[19] = 6;
		stringd[0] = 7;
		stringd[1] = 7;
		stringd[2] = 7;
		stringd[3] = 7;
		stringd[4] = 7;
		stringd[5] = 7;
		stringd[6] = 7;
		stringd[7] = 7;
		stringd[8] = 7;
		stringd[9] = 7;
		stringc[0] = 7;
		stringc[1] = 7;
		stringc[2] = 7;
		stringc[3] = 7;
		stringc[4] = 7;
		stringc[5] = 7;
		stringc[6] = 7;
		stringc[7] = 7;
		stringc[8] = 7;
		stringc[9] = 7;
	}
	i = 0;
}

