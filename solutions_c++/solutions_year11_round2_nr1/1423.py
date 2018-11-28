// r1b_1.cpp : Defines the entry point for the console application.
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

	float wp[110], owp[110], oowp[110], rpi[110], wpe[110][110];	
	char team[110][110];
	int i, j, k, n, t, tc;

	fscanf(fp, "%d", &tc);

	for(i=0; i<tc; i++){

		fscanf(fp, "%d", &n);
		fscanf(fp, "%c", &t);
		for(j=0; j<n; j++){
			for(k=0; k<n+1; k++){
				fscanf(fp, "%c", &team[j][k]);
			}
		}
		for(j=0; j<n; j++){
			float total = 0;
			float win = 0;
			for(k=0; k<n; k++){
				if(team[j][k]=='1' || team[j][k]=='0'){
					total++;
					if(team[j][k]=='1') win++;
				}
			}
			wp[j] = win/total;
			for(k=0; k<n; k++){
				if(team[j][k]=='1'){
					wpe[j][k] = (win-1)/(total-1);
				}
				if(team[j][k]=='0'){
					wpe[j][k] = win/(total-1);
				}
			}
		}
		for(j=0; j<n; j++){
			float total = 0;
			float towp = 0;
			for(k=0; k<n; k++){
				if(team[j][k]=='1' || team[j][k]=='0'){
					total++;
					towp += wpe[k][j];
				}
			}
			owp[j] = towp/total;
		}
		for(j=0; j<n; j++){
			float total = 0;
			float toowp = 0;
			for(k=0; k<n; k++){
				if(team[j][k]=='1' || team[j][k]=='0'){
					total++;
					toowp += owp[k];
				}
			}
			oowp[j] = toowp/total;
		}
		fprintf(ofp, "Case #%d:\n", i+1);
		for(j=0; j<n; j++){
			rpi[j] = 0.25*wp[j] + 0.50*owp[j] + 0.25*oowp[j];
			fprintf(ofp, "%f\n", rpi[j]);
		}
	}
}
