#include "stdio.h"
#include <iostream>
#include <fstream>
using namespace std;
#define MaxNum 200
#define  MaxMinutes 1440
void main()
{
	FILE   *infile;   
	int Turnaround[MaxNum];
	int CaseNum;
	int temp[4];
	int SwapTemp;
	int NaDeparture[MaxNum];
	int NbDeparture[MaxNum];
	int NaStart[MaxNum];
	int NbStart[MaxNum];
	int NA[MaxNum];
	int NB[MaxNum];
	int NaHave[MaxNum];
	int NbHave[MaxNum];
	int NaMin[MaxNum];
	int NbMin[MaxNum];
	int TrainNa[MaxNum];
	int TrainNb[MaxNum];
	int NaCount;
	int NbCount;
	int NowTime;
	infile=fopen("d:\\B-large.in","r");   
	 fscanf(infile,"%d",&CaseNum);   
     //cout<<CaseNum<<endl;
	 for (int j=0;j<CaseNum;j++)
	 {
		 NaHave[j]=60;
		 NbHave[j]=60;
		 NaMin[j]=60;
		 NbMin[j]=60;
	 }
	for (int i=0;i<CaseNum;i++)
	{
		 fscanf(infile,"%d  %d  %d",&Turnaround[i], &NA[i], &NB[i]);
       //cout<<NA[i]<<endl;
		 for (int j=0;j<NA[i];j++)
		 {
			 fscanf(infile,"%d:%d %d:%d",  &temp[0],&temp[1],&temp[2],&temp[3]);
			 NaDeparture[j] = temp[0]*60+temp[1];
			 NbStart[j] = temp[2]*60+temp[3]+Turnaround[i];
       //cout<<NaDeparture[j]<<"-"<<NbStart[j]<<endl;
		 }
		 for (int n=0;n<NA[i];n++)
		 {
			 for (int m=0;m<NA[i]-1;m++)
			 {
				 if (NaDeparture[m]>NaDeparture[m+1])
				 {
					 SwapTemp = NaDeparture[m];
					 NaDeparture[m] = NaDeparture[m+1];
					 NaDeparture[m+1] = SwapTemp;
				 }
			 }
		 }
		 for (int n=0;n<NA[i];n++)
		 {
			 for (int m=0;m<NA[i]-1;m++)
			 {
				 if (NbStart[m]>NbStart[m+1])
				 {
					 SwapTemp = NbStart[m];
					 NbStart[m] = NbStart[m+1];
					 NbStart[m+1] = SwapTemp;
				 }
			 }
		 }
      //cout<<NB[i]<<endl;
		 for (int j=0;j<NB[i];j++)
		 {
			 fscanf(infile,"%d:%d %d:%d",  &temp[0],&temp[1],&temp[2],&temp[3]);
			 NbDeparture[j] = temp[0]*60+temp[1];
			 NaStart[j] = temp[2]*60+temp[3]+Turnaround[i];
       //cout<<NbDeparture[j]<<"-"<<NaStart[j]<<endl;
		 }
		 for (int n=0;n<NB[i];n++)
		 {
			 for (int m=0;m<NB[i]-1;m++)
			 {
				 if (NbDeparture[m]>NbDeparture[m+1])
				 {
					 SwapTemp = NbDeparture[m];
					 NbDeparture[m] = NbDeparture[m+1];
					 NbDeparture[m+1] = SwapTemp;
				 }
			 }
		 }
		 for (int n=0;n<NB[i];n++)
		 {
			 for (int m=0;m<NB[i]-1;m++)
			 {
				 if (NaStart[m]>NaStart[m+1])
				 {
					 SwapTemp = NaStart[m];
					 NaStart[m] = NaStart[m+1];
					 NaStart[m+1] = SwapTemp;
				 }
			 }
		 }
		 NaCount = 0;
		 NbCount = 0;
		 while (NaCount<NA[i])
		 {
			 if(NbCount<NB[i])
			 {
			 if ((NaDeparture[NaCount]<NaStart[NbCount]))
			 {
				 NowTime = NaDeparture[NaCount];
				 NaCount++;
				 NaHave[i]--;
			 }
			 else if (NaDeparture[NaCount]>=NaStart[NbCount])
			 {
				 NowTime = NaStart[NbCount];
				 NbCount++;
				 NaHave[i]++;
			 }
			 }
			 else
			 {
				 NowTime = NaDeparture[NaCount];
				 NaCount++;
				 NaHave[i]--;
			 }
			 if(NaMin[i]>NaHave[i])
			 {
				 NaMin[i]=NaHave[i];
			 }
		 }
		 NaCount = 0;
		 NbCount = 0;
		 while (NbCount<NB[i])
		 {
			 if(NaCount<NA[i])
			 {
				 if ((NbDeparture[NbCount]<NbStart[NaCount]))
				 {
					 NowTime = NbDeparture[NbCount];
					 NbCount++;
					 NbHave[i]--;
				 }
				 else if (NbDeparture[NbCount]>=NbStart[NaCount])
				 {
					 NowTime = NbStart[NaCount];
					 NaCount++;
					 NbHave[i]++;
				 }
			 }
			 else
			 {
				 NowTime = NbDeparture[NbCount];
				 NbCount++;
				 NbHave[i]--;
			 }
			 if(NbMin[i]>NbHave[i])
			 {
				 NbMin[i]=NbHave[i];
			 }
		 }
	TrainNa[i] = 60 - NaMin[i];
	TrainNb[i] = 60 - NbMin[i];
}
   fclose(infile);
   ofstream outfile("Output.out");
   if (!outfile)
   {
	   cerr<<"cannot open the output file\n";
	   exit(-1);
   }
   for (int i =0;i<CaseNum;i++)
   {
	   outfile<<"Case #"<<i+1<<": "<<TrainNa[i]<<" "<<TrainNb[i]<<endl;
   }
}