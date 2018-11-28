#include<iostream>
using namespace std;
#include<cstdio>
#include<cstdlib>
#include<algorithm>
#define MAXN 110
#include<fstream>

int ABS( int a )
{
	if( a < 0 ) return -a;
	return a;
}

int main()
{
	FILE* fin = fopen("A-large.in","r");
	FILE* fout = fopen("R1_AL.out","w");
	int  button[MAXN]={0}, T, N, i, sum, Case = 0, op, bp, Ot, Bt, Bnow, Onow, OB[MAXN]={0}, BB[MAXN]={0};
	char robot[MAXN];
	fscanf(fin,"%d",&T);
	while(T--)
	{
		fscanf(fin,"%d ",&N);
		for( i=0, Ot=0, Bt=0 ; i< N ; i++ )
		{
			fscanf(fin,"%c %d ",&robot[i], &button[i]);
			if( robot[i] == 'O' )
				OB[Ot++] = button[i];
			else
				BB[Bt++] = button[i];
		}
		fprintf(fout,"Case #%d: ", ++Case );
		for( i=0, sum=0, op=1, bp=1, Onow=0, Bnow=0 ; i<N ; i++ )
		{
			if( robot[i] == 'O' )
			{
				Onow++;
				sum += (ABS(button[i]-op) +1);
				
				if( Bnow<Bt )
				{
					if( ABS(BB[Bnow]-bp) <= (ABS(button[i]-op)+1) )
						bp = BB[Bnow];
					else
					{
						if( BB[Bnow]>bp ) bp += (ABS(button[i]-op)+1);
						else bp -= (ABS(button[i]-op)+1);
					}
				}
				op = button[i];
			}
			else
			{
				Bnow++;
				sum +=  (ABS(button[i]-bp) +1);
				if( Onow < Ot )
				{
					if( ABS(OB[Onow]-op) <= (ABS(button[i]-bp)+1) )
						op = OB[Onow];
					else
					{
						if( OB[Onow] > op ) op += (ABS(button[i]-bp)+1);
						else op -= (ABS(button[i]-bp)+1);
					}
				}
				bp = button[i];
			}
		}
		fprintf(fout,"%d\n",sum);
		
	}
	return 0;
	
}
