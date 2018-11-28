// GCJ2010R3A.cpp : コンソール アプリケーションのエントリ ポイントを定義します。
//
#include "stdafx.h"


int _tmain(int argc, _TCHAR* argv[])
{
	
	FILE *fp_in,*fp_out;
	fp_in=fopen("A-large (1).in","r");
	fp_out=fopen("A-large.out","w");
	int Case_Count=0,Case=0,ans=0;
	int AB[1005][2];
	int Atemp,Btemp;
	int i,j;
	fscanf(fp_in,"%d",&Case);
	int rope=0;
	while(Case!=Case_Count){
		Case_Count++;
		ans=0;
		fscanf(fp_in,"%d",&rope);
		for(i=0;i<rope;i++){
			fscanf(fp_in,"%d %d",&Atemp,&Btemp);
			AB[i][1]=Atemp;
			AB[i][2]=Btemp;
			for(j=0;j<i;j++){
				if(AB[i][1]<AB[j][1]&&AB[i][2]>AB[j][2]){ans++;}
				if(AB[i][1]>AB[j][1]&&AB[i][2]<AB[j][2]){ans++;}
			}
		}
		fprintf(fp_out,"Case #%d: %d\n",Case_Count,ans);
		printf("Case #%d: %d\n",Case_Count,ans);
	}
	
	getchar();
	return 0;
}

