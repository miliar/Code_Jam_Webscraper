#include <stdio.h>
#include <stdlib.h>
#include <math.h>


int main(int argc, char* argv[])
{
	int Pd, Pg, T, N;
	char A;
	int** comand;
	double* WP;
	double* OWP;
	double* OOWP;
	double* RPI;
	double* count;
	FILE *f_in;
	FILE *f_out;
	f_in=fopen("A-large.in","rt");
	f_out=fopen("out.txt","wt");
	fscanf(f_in,"%d",&T);
	for(int r=0; r<T; r++)
	{
		fscanf(f_in,"%d",&N);
		comand=new int*[N];
		for(int i=0; i<N; i++)
			comand[i]=new int[N];
		WP=new double[N];
		OWP=new double[N];
		OOWP=new double[N];
		RPI=new double[N];
		count=new double[N];
		for(int i=0; i<N; i++)
		{
			WP[i]=0;
			OWP[i]=0;
			OOWP[i]=0;
			count[i]=0;
		}
		char tmp;
		
		for(int i=0; i<N; i++)
		{
			fscanf(f_in,"%c",&tmp);
		for(int j=0; j<N; j++)
		{
			fscanf(f_in,"%c",&A);
			if(A=='1')
			{
				comand[i][j]=1;
				count[i]++;
			}	
			else if(A=='0')
			{
				comand[i][j]=0;
				count[i]++;
			}
			else if(A=='.')
				comand[i][j]=-1;
		}
		}
		for(int i=0; i<N; i++)
			for(int j=0; j<N; j++)
				if(comand[i][j]!=-1)
					WP[i]+=comand[i][j]/count[i];
		for(int i=0; i<N; i++)
			for(int j=0; j<N; j++)
				if(comand[j][i]!=-1)
				OWP[i]+=(WP[j]*count[j]-comand[j][i])/(count[j]-1)/count[i];
		for(int i=0; i<N; i++)
			for(int j=0; j<N; j++)
				if(comand[i][j]!=-1)
					OOWP[i]+=OWP[j]/count[i];
		for(int i=0; i<N; i++)
			RPI[i]=0.25*WP[i]+0.5*OWP[i]+0.25*OOWP[i];
		fprintf(f_out,"Case #%d:\n", r+1);
		for(int i=0; i<N; i++)
			fprintf(f_out,"%f\n", RPI[i]);
	}
	return 0;
}