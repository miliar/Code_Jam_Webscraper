#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <vector>
using namespace std;

int main() {
	FILE *in = fopen("B.in","r");
	FILE *out = fopen("B.out","w");
	int T,H,W,i,j,k,m,n,o,p,q;
	int ar[100][100];
	int fl[100][100];
	int div[100][100];
	int xr[4] = {-1,0,1,0};
	int yr[4] = {0,1,0,-1};
	int map[10000];
	int mapc;
	fscanf(in,"%d",&T);
	for(i=0;i<T;i++) {
		fscanf(in,"%d%d",&H,&W);
		for(j=0;j<H;j++) {
			for(k=0;k<W;k++) {
				fscanf(in,"%d",&ar[j][k]);
				div[j][k]=j*W+k;
			}
		}
		for(j=0;j<H;j++) {
			for(k=0;k<W;k++) {
				m=ar[j][k];
				n=j*W+k;
				if(j!=0&&ar[j-1][k]<m) {
					m=ar[j-1][k];
					n=(j-1)*W+k;
				}
				if(k!=0&&ar[j][k-1]<m) {
					m=ar[j][k-1];
					n=j*W+k-1;
				}
				if(k!=W-1&&ar[j][k+1]<m) {
					m=ar[j][k+1];
					n=j*W+k+1;
				}
				if(j!=H-1&&ar[j+1][k]<m) {
					m=ar[j+1][k];
					n=(j+1)*W+k;
				}
				fl[j][k]=n;
			}
		}
		n=1;
		while(n) {
			n=0;
			for(j=0;j<H;j++) {
				for(k=0;k<W;k++) {
					if(div[j][k]<div[fl[j][k]/W][fl[j][k]%W]){
						div[fl[j][k]/W][fl[j][k]%W]=div[j][k];
						n=1;
					}
					else if(div[j][k]>div[fl[j][k]/W][fl[j][k]%W]) {
						div[j][k]=div[fl[j][k]/W][fl[j][k]%W];
						n=1;
					}
				}
			}
		}
		fprintf(out,"Case #%d:\n",i+1);
		for(j=0;j<10000;j++)
			map[j]=0;
		mapc='a';
		for(j=0;j<H;j++) {
			for(k=0;k<W;k++) {
				if(map[div[j][k]]==0) {
					map[div[j][k]]=mapc++;
				}
				if(k!=0) fprintf(out," ");
				fprintf(out,"%c",map[div[j][k]]);
			}
			fprintf(out,"\n");
		}
	}
	fclose(in);
	fclose(out);
}