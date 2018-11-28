// GjamCpp.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <stdio.h>
#include <conio.h>
#include <string>
#include <iostream>

int main()
{
	int i,j,k;
	//printf("Hello world!\n");

	int Number_of_TestCases=0;
	int l=1;
	scanf("%d",&Number_of_TestCases);
	int N=0;
		double *WP;
		double *EWP;  
		double *OWP ; 
		double *OOWP ;
		char **Schedule;
	while(l<=Number_of_TestCases)
	{
		scanf("%d", &N);
		Schedule = new char*[N+1];
		for(int i=0; i<N;i++)
			Schedule[i] = new char[N+1];

		for(int k=0; k<N; k++)
		{
			scanf("%s", Schedule[k]);
		}

		WP = new double[N+1];
		EWP = new double[N+1];
		OWP = new double[N+1];
		OOWP = new double[N+1];

		for(int m=0;m<N;m++)
		{
			int Wins=0;int Los=0;
			for(int n=0;n<N;n++)
			{
				if(Schedule[m][n] == '1')	Wins++;
				else if(Schedule[m][n] == '0') Los++; 
			}
			if((Wins+Los) ==0) {WP[m] = 0; continue;}

			WP[m] = (Wins)* 1.0000000/(Wins + Los);
		}

		for(int m=0;m<N;m++)
		{
			int OpNum = 0;
			for(int c=0;c<N;c++)
			{
				if(c==m  || Schedule[c][m] == '.') continue;
				
				int Wins=0;int Los=0;
				for(int n=0;n<N;n++)
				{
					if(n==m) continue;
					if(Schedule[c][n] == '1')	Wins++;
					else if(Schedule[c][n] == '0') Los++; 
				}
				if((Wins+Los) ==0) {EWP[OpNum] = 0; OpNum++; continue;}
				
				EWP[OpNum] = (Wins)* 1.0000000/(Wins + Los);
				OpNum++;
			}
			double tforAvgCal =0;
			for(int b=0;b<OpNum;b++)
			{
				tforAvgCal +=  EWP[b];
			}
			if(OpNum ==0) {OWP[m]= 0; continue;}
				OWP[m]=tforAvgCal * 1.0000000/OpNum;

		}

		for(int m=0;m<N;m++)
		{
			int Wins=0;int Los=0;
			double TforAvgCal = 0;
			int nOp= 0;
			for(int n=0;n<N;n++)
			{
				if(Schedule[m][n] != '.') {TforAvgCal += OWP[n]; nOp++;}
			}
			if(nOp == 0) {OOWP[m] = 0; continue;}

			OOWP[m] = (TforAvgCal) * 1.0000000/nOp;

		}

		

		printf("Case #%d:\n",l); 

		//RPI = 0.25 * WP[k] + 0.50 * OWP[k] + 0.25 * OOWP[k]

		for(int k=0; k<N; k++)
		{
			printf("%lf\n", 0.25 * WP[k] + 0.50 * OWP[k] + 0.25 * OOWP[k] );
		}

		delete WP;
		delete OWP;
		delete EWP;
		delete OOWP;

		for(int j=0; j<N; j++)
			delete Schedule[j];
		delete Schedule;

		l++;
	}
	return 0;
}
