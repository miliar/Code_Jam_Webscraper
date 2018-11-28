//
//  main.cpp
//  GoJam
//
//  Created by Dina Shvayakova on 11-05-17.
//  Copyright 2011 PPX Services. All rights reserved.
//

#include <assert.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>



int main (int argc, const char * argv[])
{
    int i,T=0;
	char X[100][100];
	int won[100],total[100];
	double OW[100];
    FILE *const fi = fopen("input.txt","r");
    FILE *const fo = fopen("output.txt","w");
    fscanf(fi,"%d\n",&T);
    for(i=0; i<T; ++i)  {
		int j,N=0;
		fscanf(fi,"%d",&N);
		for(j=0; j<N; ++j)	{
			fscanf(fi,"%s",X[j]);
		}
		for(j=0; j<N; ++j)	{
			int nw=0,nt=0;
			for(int k=0; k<N; ++k)	{
				char c = X[j][k];
				if(c!='.') ++nt;
				if(c=='1') ++nw;
			}
			won[j] = nw;
			total[j] = nt;
		}
		for(j=0; j<N; ++j)	{
			int nt = 0;
			double score = 0.0;
			for(int k=0; k<N; ++k)	{
				char c = X[j][k];
				if(c=='.' || total[k]<=1) continue;
				int mw = won[k]-(c=='0');
				score += mw * 1.0 / (total[k]-1);
				++nt;
			}
			if(nt)	OW[j] = score / nt;
			else	OW[j] = 0.0;
		}
		fprintf(fo,"Case #%d:\n", i+1);
		for(j=0; j<N; ++j)	{
			double OOWP = 0.0;
			int nt = 0;
			for(int k=0; k<N; ++k)	{
				char c = X[j][k];
				if(c=='.') continue;
				OOWP += OW[k];
				++nt;
			}
			if(nt) OOWP /= nt;
			//final
			double RPI = 0.0;
			if(total[j]) RPI += won[j] * 0.25 / total[j];
			RPI += 0.5 * OW[j];
			RPI += 0.25 * OOWP;
			fprintf(fo,"%lf\n",RPI);
		}
	}
    fclose(fi);
    fclose(fo);
	return 0;
}

