#include <stdio.h>
#include <stdlib.h>
FILE *inFile;
FILE *outFile;
char inputFile[] = "input.txt";
char outputFile[] = "output.txt";
int test = 0;
int main(void) {
	inFile = fopen(inputFile,"r");
	outFile = fopen(outputFile,"w");
	fscanf(inFile,"%d",&test);
	for(int i=1;i<=test;i++) {
		int N=0,S=0,p=0;
		fscanf(inFile,"%d",&N);
		fscanf(inFile,"%d",&S);
		fscanf(inFile,"%d",&p);
		int count = 0;
		for(int j=0;j<N;j++) {
			int a=0,x=0,diff=0;
			fscanf(inFile,"%d",&a);
			if(a==0 && p!=0) continue;
			x = a/3;
			diff = (x*3) - a;
			if(x>=p) {
				count++;
				continue;
			}
			x = (a-1)/3;
			diff = (x*3)-(a-1);
			if(diff==0) {
				if(x+1>=p) {
					count++;
					continue;
				}
			}
			x = (a-2)/3;
			diff = (x*3)-(a-2);
			if(diff==0) {
				if(x+1>=p) {
					count++;
					continue;
				}
				else if (S>0 && x+2>=p) {
					count++;
					S--;
					continue;
				}
			}
			x = (a-3)/3;
			diff = (x*3)-(a-3);
			if(diff==0) {
				if(x+2>=p && S>0) {
					count++;
					S--;
					continue;
				}
			}
			x = (a-4)/3;
			diff = (x*3)-(a-4);
			if(diff==0) {
				if(x+2>=p && S>0) {
					count++;
					S--;
					continue;
				}
			}
		}
		fprintf(outFile,"Case #%d: %d\n",i,count);
	}
	fclose(inFile);
	fclose(outFile);
	return 0;
}