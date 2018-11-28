//
//  main.cpp
//  GoJam
//
//  Created by Dina Shvayakova on 11-05-17.
//  Copyright 2011 PPX Services. All rights reserved.
//

#include <assert.h>
#include <memory.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>


static int total, best[100];


struct Card	{
	int c,s,t;
	bool used;
	void read(FILE*const f)	{
		fscanf(f,"%d%d%d",&c,&s,&t);
	}
	void open(Card &x)	{
		--t;
		c += x.c;
		s += x.s;
		t += x.t;
		x.used = true;
		if(c>total) c = total;
	}
}static C[100];


int cmp_int(const void *a, const void *b)	{
	return *(int*)b - *(int*)a;
}


void find(int old, Card x)	{
	int i, score = x.s;
	if(x.t)	{
		for(i=old; i<x.c; ++i)	{
			C[i].used = false;
			if(!C[i].t) continue;
			x.open(C[i]);
		}
		score = x.s;
		static int W[100];
		for(i=0; i<x.c; ++i)	{
			W[i] = (C[i].used ? 0 : C[i].s);
		}
		qsort(W, x.c, sizeof(int), cmp_int);
		for(i=0; i<x.t && i<x.c; ++i)	{
			score += W[i];
		}
	}
	if(best[x.c]>=score) return;
	best[x.c] = score;
	if(!x.t || x.c==total) return;
	for(i=0; i<x.c; ++i)	{
		if(C[i].used || !C[i].c) continue;
		Card y = x;
		x.open(C[i]);
		find(y.c,x);
		x = y;
		C[i].used = false;
	}
}


int main (int argc, const char * argv[])
{
    int i,T=0;
    FILE *const fi = fopen("input.txt","r");
    FILE *const fo = fopen("output.txt","w");
    fscanf(fi,"%d\n",&T);
    for(i=0; i<T; ++i)  {
		int N=0,M=0,j;
		fscanf(fi,"%d",&N);
		for(j=0; j<N; ++j)	{
			C[j+0].read(fi);
		}
		fscanf(fi,"%d",&M);
		for(j=0; j<M; ++j)	{
			C[j+N].read(fi);
		}
		total = N+M;
		memset(best,-1,sizeof(best));
		Card x = {N,0,1};
		find(0,x);
		int rez = 0;
		for(j=0; j<=total; ++j)	{
			int cur = best[j];
			if(cur>rez) rez = cur; 
		}
        fprintf(fo,"Case #%d: %d\n", i+1, rez);
	}
    fclose(fi);
    fclose(fo);
	return 0;
}

