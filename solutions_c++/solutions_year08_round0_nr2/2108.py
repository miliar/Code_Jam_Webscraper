#include <stdio.h>
#include <stdlib.h>
#include <string.h>


void main(){
	FILE *ifp, *ofp;
	int loop,loopCount;
	int tDelay, na, nb, cntA, cntB;
	int i,j;
	int Time[100][2];
	int map[100];
	char buf[128],tmp[5];
	int minT,min;
	
	ifp=fopen("B-small-attempt0.in","r");
	ofp=fopen("B-small-attempt0.out","w");
	fscanf(ifp,"%d",&loopCount);
	for(loop=0;loop<loopCount;loop++){
		fscanf(ifp,"%d",&tDelay);
		fscanf(ifp,"%d %d",&na,&nb);
		cntA=na;
		cntB=nb;
		for(i=0;i<100;i++){
			map[i]=0;
		}
		for(i=0;i<na+nb;i++){
			fgets(buf,128,ifp);
			if (buf[0] == '\n') { i --; continue; }
			else{
				strncpy(tmp,buf,2);
				Time[i][0]=60*atoi(tmp);
				strncpy(tmp,&buf[3],2);
				Time[i][0]+=atoi(tmp);
				strncpy(tmp,&buf[6],2);
				Time[i][1]=60*atoi(tmp);
				strncpy(tmp,&buf[9],2);
				Time[i][1]+=atoi(tmp);
			}
		}

		for(i=0;i<na;i++)
		{
			minT=100000;
			for(j=na;j<na+nb;j++)
			{
				if((Time[i][1]+tDelay)<=Time[j][0] && map[j]==0){
					if(Time[j][0]<minT){
						minT=Time[j][0];
						min=j;
					}
				}
			}
			if(minT!=100000){
				map[min]++;
				cntB--;
			}

		}
		for(i=na;i<na+nb;i++)
		{
			minT=100000;
			for(j=0;j<na;j++)
			{
				if((Time[i][1]+tDelay)<=Time[j][0] && map[j]==0){
					if(Time[j][0]<minT){
						minT=Time[j][0];
						min=j;
					}
				}
			}
			if(minT!=100000){
				map[min]++;
				cntA--;
			}
		}

		fprintf(ofp,"Case #%d: %d %d\n",loop+1,cntA,cntB);
	}
	fclose(ifp);
	fclose(ofp);
}