#include <stdio.h>
#include <string.h>
#include <stdlib.h>


int main(int argc, char *argv[])
{
	int i,j,k,l,n,s,q,tmp;
	char strBuff[256],*engines[256],*words[1024];
	int switches[2][256],sel,min_switches;
	FILE *fp,*fp_out;

	if((fp=fopen("A-Large.in","r"))==NULL)return -1;
	if((fp_out=fopen("A-Large-out.txt","w"))==NULL)return -1;

	for(i=0;i<256;i++)
		engines[i] = new char [256];
	for(i=0;i<1024;i++)
		words[i] = new char [256];

	fgets(strBuff,256,fp);
	n=atoi(strBuff);
	for(i=0;i<n;i++){

		fgets(strBuff,256,fp);
		s=atoi(strBuff);
		for(j=0;j<s;j++){
			fgets(engines[j],256,fp);
			switches[0][j]=0;
			switches[1][j]=0;
		}
		fgets(strBuff,256,fp);
		q=atoi(strBuff);
		for(j=0;j<q;j++){
			fgets(words[j],256,fp);
		}

		sel=0;
		for(j=0;j<q;j++){
			for(k=0;k<s;k++){
				if(!strcmp(engines[k],words[j])){
					switches[!sel][k]=INT_MAX - 1;
					continue;
				}
				min_switches=INT_MAX;
				for(l=0;l<s;l++){
					tmp=switches[sel][l];
					if(k!=l)tmp++;
					if(tmp<min_switches)min_switches=tmp;
				}
				switches[!sel][k]=min_switches;
			}
			sel^=1;
		}

		min_switches=INT_MAX;
		for(j=0;j<s;j++){
			if(switches[sel][j]<min_switches)min_switches=switches[sel][j];
		}

		printf("Case #%d: %d\n",i+1,min_switches);
		fprintf(fp_out,"Case #%d: %d\n",i+1,min_switches);
	}
	//printf("Finished!\n");
	fclose(fp);
	fclose(fp_out);
	
	getchar();
}
