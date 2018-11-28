#include <stdlib.h>
#include <stdio.h>
#include <iostream.h>
#include <fstream.h>
#include <math.h>
#include <time.h>

const int T=2001;
const int N=15;

int table1[T][3];
double table0[T];
int all;

const char name[]="A-large (1).in";
const char name_out[]="series_out_large.txt";

void sw(int &k1,int &k2)	//change two numbers
{	int yy;	yy=k1;	k1=k2;	k2=yy;	}

void showdata()
{
	cout<<all;
	for (int i=0;i<=all;i++)
	{
		for (int j=0;j<3;j++)	
		{	
			cout<<table1[i][j]<<" - ";
		}
		cout<<endl;
	}
}

void create()
{
	int i,j,k;	//,waiT=0,waiN=0;
	int current;	
	for (i=0;i<T;i++)
		for (j=0;j<3;j++)	
		{	
			table1[i][j]=0;
			table0[i]=0;
		}

	ifstream read(name);
	read>>current;
	all= current;
	for	(	k=1;	k<=all;	k++	)
	{ 	
		for (j=0; j<=2; j++) 
		{
			if(j==0)read>>table0[k];
			else read>>table1[k][j];
		}
	}
	return ;
}

void main()
{
	clock_t start,finish;
	double totaltime;
	start=clock();
	
	create();

	bool ppp,bbb;
	showdata();

	ofstream write_signal(name_out);
	for(int i=1;i<=all;i++)
	{
		ppp=1;bbb=0;
		if(table0[i]<100)
		{
			table1[i][0]=(int)table0[i];
				for(int u=1;u<=table1[i][0];u++)	if((u*table1[i][1])%100==0) bbb=1;
			if(!bbb)	ppp=0;
		}
		if(table1[i][2]==100&&table1[i][1]!=100)ppp=0;
		if(table1[i][2]==0&&table1[i][1]!=0)ppp=0;
		
		if(ppp)
		write_signal<<"Case #"<<i<<": Possible"<<endl;
		else
		write_signal<<"Case #"<<i<<": Broken"<<endl;
	}
	
//		write_signal<<"Case #"<<i<<": "<<time_all<<endl;

	write_signal.close();
/*	ofstream write_signal2(name_out2);
	for (int d2=0;	d2<n_max; d2++)	
	{	write_signal2<<x_cul2[d2]<<' ';	}
	write_signal2.close();
*/

	finish=clock();
	totaltime=(double)(finish-start)/CLOCKS_PER_SEC;
	cout<<"\n"<<totaltime<<"s used in the process"<<endl;
}	//END FOR MAIN
