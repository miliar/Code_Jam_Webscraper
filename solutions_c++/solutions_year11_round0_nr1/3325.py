#include <stdlib.h>
#include <stdio.h>
#include <iostream.h>
#include <fstream.h>
#include <math.h>
#include <time.h>

const int T=101;
const int N=101;

int table1[T][N];
char table0[T][N];
int all;

const char name[]="A-large.in";
const char name_out[]="series_out_large.txt";

void sw(int &k1,int &k2)	//change two numbers
{	int yy;	yy=k1;	k1=k2;	k2=yy;	}

void showdata()
{
	for (int i=0;i<T;i++)
	{
		for (int j=0;j<N;j++)	
		{	
			cout<<table0[i][j]<<' '<<table1[i][j]<<" - ";
		}
		cout<<endl;
	}
}

void create()
{
	int i,j,k,waiT=0,waiN=0;
	int current;
	for (i=0;i<T;i++)
		for (j=0;j<N;j++)	
		{	
			table1[i][j]=0;
			table0[i][j]='0';
		}

	ifstream read(name);
	read>>current;
	all= current;
	for	(	k=1;	k<=all;	k++	)
	{ 	
		j=0;
		read>>current;	waiN=current; table1[k][j]=waiN;
		for (j=1; j<=waiN; j++) 
		{
			read>>table0[k][j];
			read>>table1[k][j];
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

//	showdata();

	int posi, timeslot ,time_all;
	int b_pre,o_pre;
	char cur,cur_pre;
	ofstream write_signal(name_out);
	for (int i=1 ; i<=all; i++)
	{
		posi=1; cur_pre='0';
		b_pre = o_pre = 1 ;
		time_all=0;
		timeslot=0;
		while(	posi<=table1[i][0]	)
		{
			cur=table0[i][posi];
			if (cur==cur_pre)
			{
				if (cur=='B') 
				{	timeslot+=abs(table1[i][posi]-b_pre)+1; b_pre=table1[i][posi];}
				if (cur=='O') 
				{	timeslot+=abs(table1[i][posi]-o_pre)+1; o_pre=table1[i][posi];}
			}
			else
			{
				cur_pre=cur;
				if (posi==1) 
				{	
					if (cur=='B') {timeslot+=abs(table1[i][posi]-b_pre)+1; b_pre=table1[i][posi];}
					if (cur=='O') {timeslot+=abs(table1[i][posi]-o_pre)+1; o_pre=table1[i][posi];}
				}
				else if (cur=='B') 
				{
					if(timeslot>=abs(table1[i][posi]-b_pre)) 
					{
						time_all+=timeslot; 
						timeslot=1;
					}
					else 
					{
						time_all+=timeslot; 
						timeslot=abs(table1[i][posi]-b_pre)+1-timeslot;
					}
					b_pre=table1[i][posi];
				}
				else if (cur=='O') 
				{
					if(timeslot>=abs(table1[i][posi]-o_pre)) 
					{
						time_all+=timeslot; 
						timeslot=1;
					}
					else 
					{
						time_all+=timeslot; 
						timeslot=abs(table1[i][posi]-o_pre)+1-timeslot;
					}
					o_pre=table1[i][posi];
				}
			}
			posi++;
		}
		time_all+=timeslot;
		cout<<"Case #"<<i<<": "<<time_all<<endl;
		write_signal<<"Case #"<<i<<": "<<time_all<<endl;
	}
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
