#include <stdlib.h>
#include <stdio.h>
#include <iostream.h>
#include <fstream.h>
#include <math.h>
#include <time.h>

const int T=21;
const int N=101;

int table1[T];
char table0[T][N][N];
int all;

const char name[]="A-large.in";
const char name_out[]="series_out.txt";

void sw(int &k1,int &k2)	//change two numbers
{	int yy;	yy=k1;	k1=k2;	k2=yy;	}

void showdata()
{
	cout<<all;
	int i,j,k;
	for ( i=0;i<=all;i++)
	{
			
			cout<<table1[i]<<' ';
		
		cout<<endl;
		for (j=1;j<=table1[i];j++)
		{
			for (k=1;k<=table1[i];k++)
			{
				cout<<table0[i][j][k];
			}
			cout<<endl;
		}
		cout<<endl;
	}
}

void create()
{
	int i,j,k;	//,waiT=0,waiN=0;
	
	ifstream read(name);
	read>>all;
	
	for	(	i=1;	i<=all;	i++	)
	{ 	
		read>>table1[i];
		
		for (j=1;j<=table1[i];j++)
		{
			for (k=1;k<=table1[i];k++)
			{
				read>>table0[i][j][k];
			}
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
	showdata();

	ofstream write_signal(name_out);
	for(int i=1;i<=all;i++)
	{
		double wp[N];
		int total[N];
		double owp[N];
		double oowp[N];

		int j,k;

		for( j=1;j<=table1[i];j++)
		{
			 total[j]=0;
			wp[j]=0;
			for( k=1;k<=table1[i];k++)
			{
				if(table0[i][j][k]=='1') {total[j]=total[j]+1;	wp[j]=wp[j]+1;}
				else if(table0[i][j][k]=='0') {total[j]=total[j]+1;	}
			}
			wp[j]=wp[j]/total[j];
			cout<<wp[j]<<' ';
		}
		cout<<endl;
		for( j=1;j<=table1[i];j++)
		{
			double totall=0;
			owp[j]=0;
			for( k=1;k<=table1[i];k++)
			{
				if(table0[i][j][k]!='.') 
				{
					totall=totall+1;	
					if(table0[i][k][j]=='.')owp[j]=owp[j]+wp[k];
					else if(table0[i][k][j]=='0')owp[j]=owp[j]+wp[k]*total[k]/(total[k]-1);
					else if(table0[i][k][j]=='1')owp[j]=owp[j]+(wp[k]*total[k]-1)/(total[k]-1);
				}
			}
			owp[j]=owp[j]/totall;
			cout<<owp[j]<<' '<<totall<<' ';
		}
cout<<endl;
		
		for( j=1;j<=table1[i];j++)
		{
			double totalll=0;
			oowp[j]=0;
			for( k=1;k<=table1[i];k++)
			{
				if(table0[i][j][k]!='.') {totalll=totalll+1;	oowp[j]=oowp[j]+owp[k];}
			}
			oowp[j]=oowp[j]/totalll;
		}

		write_signal<<"Case #"<<i<<':'<<endl;
		for( j=1;j<=table1[i];j++)
		{
		oowp[j]= 0.25 * wp[j] + 0.50 * owp[j] + 0.25 * oowp[j];
		write_signal<<oowp[j]<<endl;
		}
		cout<<i<<"fin"<<endl;
	}
	
//		write_signal<<"Case #"<<i<<": "<<time_all<<endl;

	write_signal.close();

	finish=clock();
	totaltime=(double)(finish-start)/CLOCKS_PER_SEC;
	cout<<"\n"<<totaltime<<"s used in the process"<<endl;
}	//END FOR MAIN
