// saving.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "stdio.h"
#include "string.h"
#include "stdlib.h"

int tests;

struct trip{
	int starttime;
	int stoptime;
	int side; //0 a to b, 1 b to a
};

struct tren{
	int stoptime;
	int side;
	int startside;
};

int NA, NB;
int T;
struct trip viajes[400], tmp;
char line[1000];
struct tren trenes[1000]; // 0 libre, 1 hacia a, 2 hacia b;
int na, nb, n;


char * convert(_TCHAR *msg){
	char * resp = new char[wcslen(msg)+10];
	sprintf(resp,"%ls",msg);
	return resp;
}

int dehora(char * hora){
	int a, b;
	sscanf(hora,"%2d:%2d",&a,&b);
	return a*60+b;
}

int _tmain(int argc, _TCHAR* argv[])
{
	int i,j,c1,c2,k;  char hor1[30],hor2[30];
	if(argc <2)return 0;
	FILE *fp = fopen(convert(argv[1]),"r");
	FILE *fout = fopen("A-small.out","w");
	if(fp == NULL)return 0;
	fgets(line,99,fp);
	sscanf(line,"%d",&tests);
	for(k=0;k<tests;k++){
		fgets(line,99,fp);
		sscanf(line,"%d",&T);
		fgets(line,99,fp);
		sscanf(line,"%d %d",&NA, &NB);
		na = nb = 0;
		for(j=0;j<NA+NB;j++){
			fgets(line,100,fp);
			sscanf(line,"%s %s",hor1,hor2);
			viajes[j].starttime = dehora(hor1);
			viajes[j].stoptime = dehora(hor2) + T;
			viajes[j].side = j<NA?0:1;
		}
		for(i=0;i<NA+NB -1;i++){
			for(j=i;j<NA+NB;j++){
				if(viajes[i].starttime > viajes[j].starttime){
					memcpy(&tmp,&viajes[i],sizeof(tmp));
					memcpy(&viajes[i],&viajes[j],sizeof(tmp));
					memcpy(&viajes[j],&tmp,sizeof(tmp));
				}
			}
		}
		for(i=0;i<1000;i++){
			trenes[i].stoptime= 0;
			trenes[i].side = -1;
			trenes[i].startside = -1;
		}
		n = 0;
		for(i=0;i<NA+NB;i++){
			for(j=0;j<n;j++){
				if(trenes[j].stoptime<=viajes[i].starttime){ //ya termino su viaje
					if(trenes[j].side != viajes[i].side)
						trenes[j].stoptime = 0;
				}
			}
			for(j=0;j<=n;j++){
				if((trenes[j].stoptime==0)&&(trenes[j].side != viajes[i].side)){
					trenes[j].stoptime = viajes[i].stoptime;
					trenes[j].side = viajes[i].side;
					if(trenes[j].startside == -1)trenes[j].startside=viajes[i].side;
					if(n==j)n++;
					break; //ya se le asigno un viaje
				}
			}
		}		
		na = nb =0;
		for(j = 0;j<n;j++){
			if(trenes[j].startside == 0)na++;
			else nb++;
		}
		fprintf(fout,"Case #%d: %d %d\r\n",k+1,na,nb);
	}
	fflush(fout);
	fclose(fout);
	fclose(fp);
	return 0;
}

