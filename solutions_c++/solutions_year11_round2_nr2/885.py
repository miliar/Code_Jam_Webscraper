#include <stdlib.h>
#include <stdio.h>
#include <iostream.h>
#include <fstream.h>
#include <math.h>
#include <time.h>

#define way 0.0001

const int T=51;
const int N=201;

int table1[T][2];
int table0[T][N][2];
int all;

const char name[]="B-small-attempt1.in";
const char name_out[]="series_out.txt";

void sw(int &k1,int &k2)	//change two numbers
{	int yy;	yy=k1;	k1=k2;	k2=yy;	}

void showdata()
{
	cout<<all;
	int i,j;
	for ( i=0;i<=all;i++)
	{
		for ( j=0;j<2;j++)	
		{	
			cout<<table1[i][j]<<' ';
		}
		cout<<endl;
		for (j=1;j<=table1[i][0];j++)
		{
			cout<<table0[i][j][0]<<' ';
			cout<<table0[i][j][1]<<' ';
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
		for (j=0; j<2; j++) 
		{
			read>>table1[i][j];
		}
		for (j=1;j<=table1[i][0];j++)
		{
			read>>table0[i][j][0];
			read>>table0[i][j][1];
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
		//initial
		double standard=(double)table1[i][1];
		double coordinate[100000];	int co_max=0,point=0;
		for(int j=1; j<=table1[i][0]; j++)
		{
			int cur=table0[i][j][1];
			while(cur>0)
			{coordinate[point]=(double)table0[i][j][0];	point++;	cur--;}
		}
		co_max=point;
		
		double t=0;
		bool status=1;
		while(status)
		{	
			status=0;
			for(point=1; point<co_max-1; point++)
			{
				if(((coordinate[point]-coordinate[point-1])<standard)&&((coordinate[point+1]-coordinate[point])>=standard)) {coordinate[point]=coordinate[point]+way;	status=1;}
				else if(( (coordinate[point]-coordinate[point-1]) >= standard) && ((coordinate[point+1]-coordinate[point])<standard)) {coordinate[point]=coordinate[point]-way; status=1;}
				else if(((coordinate[point]-coordinate[point-1])<standard)&&((coordinate[point+1]-coordinate[point])<standard)) {status=1;}
			}
			coordinate[0]=coordinate[0]-way;	coordinate[co_max-1]=coordinate[co_max-1]+way;
			if(status) t=t+way;
		}

		write_signal<<"Case #"<<i<<": "<<t<<endl;
		cout<<i<<"fin"<<endl;
	}
	
//		write_signal<<"Case #"<<i<<": "<<time_all<<endl;

	write_signal.close();

	finish=clock();
	totaltime=(double)(finish-start)/CLOCKS_PER_SEC;
	cout<<"\n"<<totaltime<<"s used in the process"<<endl;
}	//END FOR MAIN
