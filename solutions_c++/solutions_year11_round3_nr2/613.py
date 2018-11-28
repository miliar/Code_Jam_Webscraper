#include <stdlib.h>
#include <stdio.h>
#include <iostream.h>
#include <fstream.h>
#include <math.h>
#include <time.h>
#include <string.h>

const int T=101;
const int C=1001;

int table1[T][3];
double t[T];
int table0[T][C];
int all;

const char name[]="B-small-attempt0.in";
const char name_out[]="series_out_large.txt";

void sw(int &k1,int &k2)	//change two numbers
{	int yy;	yy=k1;	k1=k2;	k2=yy;	}

void showdata()
{
	int i,j;
	cout<<all<<endl;
	for (i=1;i<=all;i++)
	{
		cout<<table1[i][0]<<' '<<t[i]<<' '<<table1[i][1]<<' '<<table1[i][2];
		for( j=1; j<=table1[i][2]; j++)			cout<<' '<<table0[i][j];
		cout<<endl;
	}
}

void create()
{
	int i,j;	//,waiT=0,waiN=0;
	
	ifstream read(name);
	read>>all;
	for	(	i=1;	i<=all;	i++	)
	{ 	
		read>>table1[i][0];
		read>>t[i];
		read>>table1[i][1];
		read>>table1[i][2];

		for( j=1; j<=table1[i][2]; j++)	read>>table0[i][j];
	}
	return ;
}

void main()
{
	clock_t start,finish;
	double totaltime;
	start=clock();
	
	create();


	showdata();
	int i,j;
	ofstream write_signal(name_out);
	for(i=1;i<=all;i++)
	{
		double turn;
		int point;
		double ax;
		int period=0;
		for(j=1;j<=table1[i][2];j++) period+=table0[i][j];
	
		turn=0.5*(t[i]/(double)period);
		point=table1[i][2]*(int)floor(turn);
		turn=t[i]-(double)point*(double)period;
		for(j=1;j<=table1[i][2];j++)
		{
			if(table0[i][j]<turn*0.5 )
			{
				point++; turn=turn-table0[i][j]*2;
			}
			else
			{
				ax=table0[i][j]-0.5*turn;	point++; break;
			}
		}

		cout<<point<<' '<<turn<<' '<<ax<<endl;

		int  remain[1000];
	//	remain[0]=ax;
		int index=0;
		while(point<table1[i][1])
		{
			index++;
			remain[index]=table0[i][1+point%table1[i][2]];
			cout<<remain[index]<<' ';
			
			point++;
		}

		cout<<endl<<point<<' '<<index<<endl;

		int tim=0;	int ppp=0;

		while(ppp<table1[i][1])
		{
			tim=tim+table0[i][1+ppp%table1[i][2]];	ppp++;
		}
		
		tim=tim*2;

		cout<<tim<<endl;

		for(j=1;j<=table1[i][0];j++)
		{
			double sup=ax;	int rec=0;
			for(int k=1;	k<=index;	k++)
			{
				if(remain[k]>sup)	{sup=remain[k]; rec=k;}
			}
			tim=tim-sup;	if(rec==0)ax=0;else remain[rec]=0;
		}
		write_signal<<"Case #"<<i<<": "<<tim<<endl;
	}

	write_signal.close();

 	finish=clock();
	totaltime=(double)(finish-start)/CLOCKS_PER_SEC;
	cout<<"\n"<<totaltime<<"s used in the process"<<endl;
}	//END FOR MAIN
