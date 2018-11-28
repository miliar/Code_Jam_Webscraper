// saving.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "stdio.h"
#include "string.h"
#include "stdlib.h"

int tests;
int S;
int Q;
int C;

char engines[100][101];
char queries[1000][200];
char line[100];

char * convert(_TCHAR *msg){
	char * resp = new char[wcslen(msg)+10];
	sprintf(resp,"%ls",msg);
	return resp;
}

int menossaltos(){
	int i, j, k,kk, saltos, menor= -1, ms = -1, cur= -1;
	kk = 0;
	saltos =0;
	while(kk < Q){
		//busco al mas lejano
		for(j=0;j<S;j++){
			if(j==cur)continue; // el actual no cuenta
			for(k=kk;k<Q;k++){
				if(stricmp(engines[j],queries[k])==0)break;
			}
			if(k>ms){
				ms = k; menor = j;
			}
			if(k==Q)break;
		}
		if(k<=Q){ kk = ms; cur = menor; if(k<Q) saltos ++; }
	}	
	return saltos;
}

int _tmain(int argc, _TCHAR* argv[])
{
	int i,j,k;
	if(argc <2)return 0;
	FILE *fp = fopen(convert(argv[1]),"r");
	FILE *fout = fopen("A-small.out","w");
	if(fp == NULL)return 0;
	fgets(line,99,fp);
	sscanf(line,"%d",&tests);
	for(i=0;i<tests;i++){
		fgets(line,99,fp);
		sscanf(line,"%d",&S);
		for(j=0;j<S;j++)
			fgets(engines[j],100,fp);
		fgets(line,99,fp);
		sscanf(line,"%d",&Q);
		for(j=0;j<Q;j++)
			fgets(queries[j],100,fp);
		C = menossaltos();
		fprintf(fout,"Case #%d: %d\r\n",i+1,C);
	}
	fflush(fout);
	fclose(fout);
	fclose(fp);
	return 0;
}

