// r1c_1.cpp : Defines the entry point for the console application.
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

	int tc, r, c, i, j, k;
	char t[60][60];

	fscanf(fp, "%d", &tc);

	for(i=0; i<tc; i++){
		fscanf(fp, "%d %d", &r, &c);
		fscanf(fp, "%c", &k);
		bool poss = true;
		for(j=0; j<r; j++){
			for(k=0; k<c+1; k++){
				fscanf(fp, "%c", &t[j][k]);
			}
		}
		for(j=0; j<r; j++){
			for(k=0; k<c; k++){
				if(t[j][k]=='#'){
					if(j<r-1 && k<c-1){
						if(t[j][k+1] == '#' && t[j+1][k] == '#' && t[j+1][k+1] == '#'){
							t[j][k] = '/';
							t[j][k+1] = '\\';
							t[j+1][k] = '\\';
							t[j+1][k+1] = '/';
						}
						else poss = false;
					}
					if(j==r-1 || k==c-1) poss = false;
				}
			}
		}
		fprintf(ofp, "Case #%d:\n", i+1);
		if(poss){
			for(j=0; j<r; j++){
				for(k=0; k<c; k++){
					fprintf(ofp, "%c", t[j][k]);
				}
				fprintf(ofp, "\n");
			}
		}
		else fprintf(ofp, "Impossible\n");
	}
}