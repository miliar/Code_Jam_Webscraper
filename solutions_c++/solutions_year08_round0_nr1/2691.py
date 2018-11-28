#include<stdio.h>
#include<conio.h>
#include<string.h>
#include<stdlib.h>

#define MAX_TEST_CASES 20	
#define MAX_SE	100
#define MAX_SE_LEN	100
#define MAX_Q	100


struct testcase
{
	short NoOfSE;
	char SEName[MAX_SE][MAX_SE_LEN];
	short NoOfQ;
	char Queries[MAX_Q][MAX_SE_LEN];
	short QueryFreq[MAX_SE];
	short NoOfSwitch;
	short FirstOccurance[MAX_SE];
	short FarSE;
};

void CalculateFar(testcase &t,int s,int c)
{
	int Distance[MAX_SE]={0};
	for(int i=0;i<t.NoOfSE;i++)
	{
		Distance[i]=100;
		for(int j=s;j<t.NoOfQ;j++)
		{
			if(strcmp(t.SEName[i],t.Queries[j])==0)
			{
			  Distance[i]=j;
			  break;
		    }
		}
	}
	int Max=0;
	for(int k=0;k<t.NoOfSE;k++)
	{
	   if(Distance[k] > Max)	
	   {
			Max=Distance[k];
			t.FarSE=k;
		}
	}
}


void CalculateSwitches(testcase &t)
{
	int MaxDistance=0;
  	for(int j=0;j<t.NoOfQ;j++)
	{
		if(strcmp(t.SEName[t.FarSE],t.Queries[j])==0)
		{
			t.NoOfSwitch++;
			CalculateFar(t,j,t.FarSE);
		}
	}
}


int main()
{
 testcase t[MAX_TEST_CASES]={0};
 short NoOfTestCases=0;
 
 char tempString[100]={0};
 
 char FileName[128]={"C:\\CodeJam\\A-small-attempt4.in"};
 char OFileName[128]={"C:\\CodeJam\\A-small-attempt4.out"};
 FILE *fp=NULL;
 FILE *fpO=NULL;
 fp=fopen(FileName,"r");
 fpO=fopen(OFileName,"w");
 
 if(fp!= NULL)
 {
 fgets(tempString,100,fp);
 NoOfTestCases  = atoi(tempString);
 for(int i=0;i<NoOfTestCases;i++)
 {
	fgets(tempString,100,fp);
 	t[i].NoOfSE = atoi(tempString);	
	for(int j=0;j<t[i].NoOfSE;j++)
	{
		fgets(tempString,100,fp);
		strcpy(t[i].SEName[j],tempString);
	}
	
	fgets(tempString,100,fp);
 	t[i].NoOfQ = atoi(tempString);	
	for(int j=0;j<t[i].NoOfQ; j++)
	{
		fgets(tempString,100,fp);
		strcpy(t[i].Queries[j],tempString);
	}	
	
	CalculateFar(t[i],0,0);
 	CalculateSwitches(t[i]);
   	printf("Case #%d: %d \n",i+1,t[i].NoOfSwitch);
	if(fpO != NULL)
	{
		fprintf(fpO,"Case #%d: %d \n",i+1,t[i].NoOfSwitch);
	} 
 }
}

fclose(fp);
fclose(fpO);

getch();
return 0;	
}
