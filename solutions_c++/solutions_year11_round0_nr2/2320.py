#include <stdio.h>
#include <string.h>
#include <memory.h>

int N,T,C,D;
char com[36][5],opp[28][5];
char vok[110];

FILE *in = fopen("input.txt","r");
FILE *out = fopen("output.txt","w");

int main(void){
	int t,i,j,k;
	fscanf(in,"%d",&T);
	for(t=1;t<=T;t++){
		fscanf(in,"%d",&C);
		for(i=0;i<C;i++){
			fscanf(in,"%s",&com[i]);
		}
		fscanf(in,"%d",&D);
		for(i=0;i<D;i++){
			fscanf(in,"%s",&opp[i]);
		}
		fscanf(in,"%d%s",&N,vok);
		for(i=1;i<N;i++){
			for(j=0;j<C;j++){
				if(com[j][0]==vok[i]&&com[j][1]==vok[i-1]||com[j][0]==vok[i-1]&&com[j][1]==vok[i]){
					vok[i-1]=0;
					vok[i]=com[j][2];
					break;
				}
			}
			if(j!=C)continue;
			for(j=0;j<D;j++){
				for(k=0;k<i;k++){
					if(opp[j][0]==vok[i]&&opp[j][1]==vok[k]||opp[j][0]==vok[k]&&opp[j][1]==vok[i]){
						break;
					}
				}if(k!=i)break;
			}
			if(j!=D){
				for(j=0;j<=i;j++){
					vok[j]=0;
				}
			}
		}
		fprintf(out,"Case #%d: [",t);
		for(i=0,j=0;i<N;i++){
			if(vok[i]==0)continue;
			if(j==0)fprintf(out,"%c",vok[i]);
			else fprintf(out,", %c",vok[i]);
			j++;
		}fprintf(out,"]\n");
	}
	return 0;
}