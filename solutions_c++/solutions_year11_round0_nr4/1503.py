#include <stdlib.h>
#include <stdio.h>
#include <iostream.h>
#include <fstream.h>
#include <math.h>
#include <time.h>

const int N=1001;
const int T=101;

int table1[T][N];

int all;

const char name[]="D-large.in";
const char name_out[]="series_out_large.txt";

void sw(int &k1,int &k2)	//change two numbers
{	int yy;	yy=k1;	k1=k2;	k2=yy;	}

int B[N];
double A[N];

int step_mult(int n)
{
	int r=1;
	for (int i=2; i<=n; i++)
		r*=i;
	return r;
}

int combin(int n, int k)
{
     if (k > n)
         return 0;
     int r = 1;
     for ( int d = 1; d <= k; ++d)
     {
         r *= n--;
         r /= d;
     }
     return r;
}

void build_B()
{
	B[0]=B[1]=0;
	for(int i=2; i<N; i++)
	{
		B[i]=step_mult(i)-1;
		for(int j=1; j<i; j++)
			B[i]-=combin(i,j)*B[i-j];
	}
}

void build_A()
{
	A[0]=A[1]=0;
	double coef;
	double sum;
	for(int i=2; i<N; i++)
	{
		coef=0;	sum=0;
		coef=step_mult(i)-B[i];
		for(int j=1; j<i; j++)
			sum=sum+double(combin(i,j))*double(B[j])*A[j];
		A[i]=sum/coef+step_mult(i)/coef;
	}
}

void showtable()
{
	for (int i=0;i<T;i++)
	{
		for (int j=0;j<N;j++)	
		{	
			cout<<table1[i][j]<<' ';
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

	cout<<combin(10,5)<<endl;

	int alll;
//	build_B();
//	build_A();

//	for(int i=1;i<N;i++)	cout<<B[i]<<' ';
//	cout<<endl;
//	for( i=1;i<N;i++)	cout<<A[i]<<' ';

	create();

	ofstream write_signal(name_out);
	
	for(int i=1;i<=all;i++)	
	{
		alll=table1[i][0];
		for(int j=1;j<=table1[i][0];j++)
		{if(j==table1[i][j]) alll--;}	
		write_signal<<"Case #"<<i<<": "<<alll<<".000000"<<endl;
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
