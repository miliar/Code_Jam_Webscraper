#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

#define PI 3.14159265358979323846

int compare_int(const int *a, const int *b)
{
    return *a-*b;
}


int main(int argc, char *argv[])
{
	int i,j,k,l,m,n,na,nb,t,dHH,dMM,aHH,aMM;
	int tripAB[256][3],tripBA[256][3];
	int ansA,ansB,stateA,stateB;
	char strBuff[256];
	FILE *fp,*fp_out;

	if((fp=fopen("B-Large.in","r"))==NULL)return -1;
	if((fp_out=fopen("B-Large-out.txt","w"))==NULL)return -1;

	fgets(strBuff,256,fp);
	n=atoi(strBuff);
	for(i=0;i<n;i++){
		fscanf(fp,"%d",&t);
		fscanf(fp,"%d %d",&na,&nb);
		for(j=0;j<na;j++){
			fscanf(fp,"%d:%d %d:%d",&dHH,&dMM,&aHH,&aMM);
			tripAB[j][0]=dHH*60+dMM;
			tripAB[j][1]=aHH*60+aMM+t;
			tripAB[j][2]=0;
		}
		for(j=0;j<nb;j++){
			fscanf(fp,"%d:%d %d:%d",&dHH,&dMM,&aHH,&aMM);
			//printf("%d %d %d %d\n",dHH,dMM,aHH,aMM);
			tripBA[j][0]=dHH*60+dMM;
			tripBA[j][1]=aHH*60+aMM+t;
			tripBA[j][2]=0;
		}
		qsort(tripAB,na,sizeof(int)*3,(int (*)(const void*, const void*))compare_int);
		qsort(tripBA,nb,sizeof(int)*3,(int (*)(const void*, const void*))compare_int);

		ansA=0;	ansB=0;
		stateA=0; stateB=0;
		j=0;k=0;
		while(j<na || k<nb){
			if(k>=nb || (j<na && tripAB[j][0] < tripBA[k][0])){
				for(l=0;l<nb;l++){
					if(!tripBA[l][2] &&  tripBA[l][1] <= tripAB[j][0]){
						stateA++;
						tripBA[l][2]=1;
					}
				}
				if(stateA)stateA--;
				else ansA++;
				j++;
			}else{
				for(l=0;l<na;l++){
					if(!tripAB[l][2] &&  tripAB[l][1] <= tripBA[k][0]){
						stateB++;
						tripAB[l][2]=1;
					}
				}
				if(stateB)stateB--;
				else ansB++;
				k++;
			}
		}

		printf("Case #%d: %d %d\n",i+1,ansA,ansB);
		fprintf(fp_out,"Case #%d: %d %d\n",i+1,ansA,ansB);
	}
	//printf("Finished!\n");
	fclose(fp);
	fclose(fp_out);
	
	getchar();
}
