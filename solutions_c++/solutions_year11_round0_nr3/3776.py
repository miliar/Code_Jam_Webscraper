#include<iostream>
using namespace std;
#include<cstdio>
#include<cstdlib>
#include<algorithm>
#define MAXN 1010
#include<fstream>


int main()
{
	FILE* fin = fopen("C-large.in","r");
	FILE* fout = fopen("R1_CL.out","w");
	int C[MAXN], T, N, i, sum, Case = 0;
	fscanf(fin,"%d",&T);
	while(T--)
	{
		fscanf(fin,"%d",&N);
		for( i=0, sum = 0  ; i< N ; i++ )
		{
			fscanf(fin,"%d",&C[i]);
			sum ^= C[i];
		}
		fprintf(fout,"Case #%d: ", ++Case );
		if( sum ) fprintf(fout,"NO\n");
		else
		{
			sort(C,C+N);
			for( i = 1  , sum = 0 ; i<N ; i++ )
				sum += C[i];
			fprintf(fout,"%d\n",sum);
		}
	}
	
}
