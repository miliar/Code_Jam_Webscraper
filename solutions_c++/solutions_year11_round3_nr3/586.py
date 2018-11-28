#include <stdlib.h>
#include <stdio.h>
#include <iostream.h>
#include <fstream.h>
#include <math.h>
#include <time.h>
#include <string.h>

const int T=41;
const int N=101;

int table1[T][3];
int table0[T][N];
int all;

const char name[]="C-small-attempt0.in";
const char name_out[]="series_out_large.txt";

void sw(int &k1,int &k2)	//change two numbers
{	int yy;	yy=k1;	k1=k2;	k2=yy;	}

void showdata()
{
	int i,j,k;
	cout<<all<<endl;

	for	(	i=1;	i<=all;	i++	)
	{ 	
		for( j=0; j<3 ; j++)
		{
			cout<<table1[i][j]<<' ';
		}
		cout<<endl;

		for( k=1; k<=table1[i][0]; k++)
		{
			cout<<table0[i][k]<<' ';
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
		for( j=0; j<3 ; j++)
		{
			read>>table1[i][j];
		}

		for( k=1; k<=table1[i][0]; k++)
		{
			read>>table0[i][k];
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
		
		bool sta=0;
		int res=0;


		for(int j=table1[i][1];	j<=table1[i][2]; j++	)
		{
			bool sta_in=1;
			
			for(int k=1; k<=table1[i][0]; k++)
				if(( (table0[i][k]%j ) !=0)&& (j% (table0[i][k] ) !=0) ){sta_in=0; break;}
			
			if(sta_in)
			{
				res=j; sta=1; break;
			}
		}
		
		write_signal<<"Case #"<<i<<": ";
		if(sta)		write_signal<<res<<endl;
		else write_signal<<"NO"<<endl;
	}
	
//		write_signal<<"Case #"<<i<<": "<<time_all<<endl;

	write_signal.close();

  /*
	ofstream write_signal2(name_out2);
	for (int d2=0;	d2<n_max; d2++)	
	{	write_signal2<<x_cul2[d2]<<' ';	}
	write_signal2.close();
*/

	finish=clock();
	totaltime=(double)(finish-start)/CLOCKS_PER_SEC;
	cout<<"\n"<<totaltime<<"s used in the process"<<endl;
}	//END FOR MAIN
