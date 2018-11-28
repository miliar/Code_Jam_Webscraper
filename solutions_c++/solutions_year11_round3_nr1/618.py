#include <stdlib.h>
#include <stdio.h>
#include <iostream.h>
#include <fstream.h>
#include <math.h>
#include <time.h>
#include <string.h>

const int T=51;
const int R=51;
const int C=51;


int table1[T][2];
char table0[T][R][C];
int all;

const char name[]="A-large (2).in";
const char name_out[]="series_out_large.txt";

void sw(int &k1,int &k2)	//change two numbers
{	int yy;	yy=k1;	k1=k2;	k2=yy;	}

void showdata()
{
	int i,j,k;
	cout<<all<<endl;
	for (i=1;i<=all;i++)
	{
	cout<<table1[i][0]<<' '<<table1[i][1]<<endl;
		for( j=1; j<=table1[i][0]; j++)
		{for( k=1; k<=table1[i][1]; k++)
			cout<<table0[i][j][k];
			cout<<endl;	
		}
	
	}
}

void create()
{
	int i,j,k;	//,waiT=0,waiN=0;
	
	ifstream read(name);
	read>>all;
	for	(	i=1;	i<=all;	i++	)
	{ 	
		read>>table1[i][0];read>>table1[i][1];
		for( j=1; j<=table1[i][0]; j++)
		for( k=1; k<=table1[i][1]; k++)
			read>>table0[i][j][k];
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
	int i,j,k;
	ofstream write_signal(name_out);
	for(i=1;i<=all;i++)
	{
		bool st=1;
		for( j=1; j<=table1[i][0]; j++)
		{
			
			for( k=1; k<=table1[i][1]; k++)
			{
				if( table0[i][j][k]=='#')
				{
					if(( table0[i][j+1][k]=='#')&&( table0[i][j][k+1]=='#')&&( table0[i][j+1][k+1]=='#'))
					{
						table0[i][j][k]='/';
						table0[i][j][k+1]='\\';
						table0[i][j+1][k]='\\';
						table0[i][j+1][k+1]='/';
					}
					else st=0;
				}
			}
		}

		write_signal<<"Case #"<<i<<":"<<endl;
		if(st)
		{
			for( j=1; j<=table1[i][0]; j++)
				{for( k=1; k<=table1[i][1]; k++)
					write_signal<<table0[i][j][k];
					write_signal<<endl;	
				}
		}
		else	write_signal<<"Impossible"<<endl;
	}

	write_signal.close();

 	finish=clock();
	totaltime=(double)(finish-start)/CLOCKS_PER_SEC;
	cout<<"\n"<<totaltime<<"s used in the process"<<endl;
}	//END FOR MAIN
