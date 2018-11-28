// U  guys are gonna get sick seeing all the arrays That Im gonna use now =) 
//Dynamic allocations would have been better, 
//but then agiain I need to get the output in 8 mins right? 
//So I will favour speed to efficiency ;) 

//Command to generate the output --> ./progA.1  <A-small-attempt0.in 2>/dev/null | tee OPA1.1

#include <iostream.h>
#include <string.h>
#include <stdio.h>

char EngineNames[100][100];
char queries[1000][100];


int arr1[100];
int arr2[100];
int switchResults[20];
int cases[101];
int switchCount;

int *curr,*nxt;

void swap(int **first,int **second);
void cleanup(int *lst,int *val);
void populateEngine(int *engineCntr);
void populateQuery(int *queryCntr);
void renderResults(int *totCount);
void incrementAll(int *ptr,int *exception);
void optiSwitch(int *engineCntr,int *queryCntr,int pos);
int seMileage(int *pos,int *qLength,char *SE);
int getMax(int *engineCntr);

int main()
{
	//Since we can perform redirection with clever Cygwin ( thank you Unix) I convinently avoid the mess associated with the file handling :) 
	int tstCases,tstCntr,engineCntr,queryCntr;
	curr=arr1;
	nxt=arr2;
	cin>>tstCases;
	for(tstCntr=1;tstCntr<=tstCases;tstCntr++)
	{
		cin>>engineCntr;
		cin.ignore();
		populateEngine(&engineCntr);
		cin>>queryCntr;
		cin.ignore();
		if(queryCntr==0)
		{
			cases[tstCntr]=0;
			continue;
		}
		populateQuery(&queryCntr);
		optiSwitch(&engineCntr,&queryCntr,0);
		cases[tstCntr]=switchCount;
		switchCount=0;
		
	}
	renderResults(&tstCntr);
	
}
void swap(int **first,int **second)
{
	int *tmp;
	tmp=*first;
	*first=*second;
	*second=tmp;
}

void cleanup(int *lst,int val)
{
	//List size is always 100
	int cntr;
	for(cntr=0;cntr<100;cntr++)
	{
		*(lst+cntr)=val;
	}
}

void populateEngine(int *engineCntr)
{
	int cntr;
	for(cntr=0;cntr<*engineCntr;cntr++)
	{
		cin.getline(EngineNames[cntr], 100, '\n');
	}
}

void populateQuery(int *queryCntr)
{
	int cntr;
	for(cntr=0;cntr<*queryCntr;cntr++)
	{
		cin.getline(queries[cntr], 100, '\n');
	}
}

void optiSwitch(int *engineCntr,int *queryCntr,int pos)
{
	int cntrE,cntrQ,mileage;
	bool jackpot;
	int switches;
	static int totMileage;
	switchCount++;
	cerr<<"Switch Count :"<<switchCount<<endl; //This Statement makes my prog Tick. I have no idea how.. :) 
	cleanup(arr1,0);
	for(int cntrE=0;cntrE<*engineCntr;cntrE++)
	{
		mileage=seMileage(&pos,queryCntr,EngineNames[cntrE]);
		//cout<<"Mileage is "<<mileage<<endl;

		if(mileage==-1)
		{

			jackpot=true;
			arr1[cntrE]=*queryCntr;
			break;
			
		}
		else
		{
			arr1[cntrE]=mileage;
		}
		
	}
	totMileage+=getMax(engineCntr);
	//cout<<"totMileage "<<totMileage<<endl;
	if(!jackpot)
	{
		if((totMileage <= *queryCntr))
		{
			optiSwitch(engineCntr,queryCntr,totMileage);
		}
		else
			totMileage=0;
		return;
	}
	else
	{
		switchCount--;
		totMileage=0;
		return;
	}
	
}
	

int getMax(int *engineCntr)
{
	int cntr,MaxVal=0;
	for(cntr=0;cntr<*engineCntr;cntr++)
	{
		if(arr1[cntr]>=MaxVal)
		{
			MaxVal=arr1[cntr];
		}
	}
	//cout<<"MaxVal "<<MaxVal<<endl;
	return MaxVal;
}


int seMileage(int *pos,int *qLength,char *SE)
{
	int cntr=*pos;
	do
	{
		if(strcmp(queries[cntr],SE)==0)
			break;
		cntr++;
	}while(cntr<=*qLength);
	cntr=(cntr>=*qLength)?-1:(cntr-*pos);
	return cntr;
}

void renderResults(int *tot)
{
	int cntr;
	for(cntr=1;cntr<*tot;cntr++)
	{
		cout<<"Case #"<<cntr<<": "<<cases[cntr];
		if((cntr<*tot-1))
		cout<<endl;
	}
}
