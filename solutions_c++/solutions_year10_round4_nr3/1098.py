#include<stdio.h>
#include<memory.h>
#include<string.h>

int inMat[110][110];
int finMat[110][110];

int main()
{
	char filename[32];
	char infile[32], outfile[32];
	scanf("%s", filename);
	strcpy(infile, filename); strcpy(outfile, filename);
	strcat(infile, ".in"); strcat(outfile, ".out");
	FILE *fp=fopen(infile, "r"), *ofp=fopen(outfile, "w");

	int i, j, tc, r, a, b, c, x1, y1, x2, y2, flag = 1, count;
	int cnt;
	fscanf(fp, "%d", &tc);
	for(i=1; i<=tc; i++){
		for(a=0; a<=100; a++){
			for(b=0; b<=100; b++){
				inMat[a][b]=0;
				finMat[a][b]=0;
			}
		}
		fscanf(fp, "%d", &r);
		for(a=1; a<=r; a++){
			fscanf(fp, "%d %d %d %d", &x1, &y1, &x2, &y2);
			for(b=x1; b<=x2; b++){
				for(c=y1; c<=y2; c++){
					inMat[b][c]=1;
				}
			}
		}
		flag = 1;
		count = 0;
		while(flag){
			for(a=1; a<=100; a++){
				for(b=1; b<=100; b++){
					if(inMat[a][b]==0){
						if(inMat[a-1][b] == 1 && inMat[a][b-1] == 1){
							finMat[a][b] = 1;
						}
						else finMat[a][b] = 0;
					}
					if(inMat[a][b]==1){
						if(inMat[a-1][b] == 1 || inMat[a][b-1] == 1){
							finMat[a][b] = 1;
						}
						else finMat[a][b] = 0;
					}
				}
			}
			count++;
			flag=0;
			for(a=1; a<=100; a++){
				for(b=1; b<=100; b++){
					inMat[a][b] = finMat[a][b];
					if(inMat[a][b] == 1) flag = 1;
				}
			}
		}
		fprintf(ofp, "Case #%d: %d\n", i, count);
	}
				

}