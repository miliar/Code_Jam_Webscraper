#include "stdio.h"
#include "stdlib.h"
#include "memory.h"
#include "string.h"

FILE *fin, *fout;

#define INPUT_FILE_NAME "A-large"
#define INPUT_FILE INPUT_FILE_NAME##".in"
#define OUTPUT_FILE INPUT_FILE_NAME##".out"

#define print(format,...) {fprintf(fout, format, __VA_ARGS__); printf(format, __VA_ARGS__);}

#define min(a,b) ((a)<(b)?(a):(b))
#define max(a,b) ((a)>(b)?(a):(b))

void problem();

void main(int argc, char **argv)
{
	int N,k;
	printf("%s\n", INPUT_FILE);
	fopen_s(&fin, INPUT_FILE, "rt");
	fopen_s(&fout, OUTPUT_FILE, "wt");
	fscanf_s(fin, "%d", &N);
	k=0;
	while(N--)
	{
		++k;
		print("Case #%d: ", k);
		problem();
		print("\n");
	}
	fclose(fin);
	fclose(fout);
}

typedef struct  
{
	int B,E,w;
	int len;
	bool bRun;
}SWalkway;

void problem()
{
	int x, s, r, t, n;
	long double tt;
	int i;
	int noWalkways = 0;
	long double time;
	SWalkway walks[1000];
	fscanf_s(fin, "%d %d %d %d %d", &x, &s, &r, &t, &n);
	tt = t;
	for (i=0;i<n;++i)
	{
		fscanf_s(fin, "%d %d %d", &walks[i].B, &walks[i].E, &walks[i].w);
		walks[i].bRun = false;
		walks[i].len = walks[i].E-walks[i].B;
		if (i==0)
		{
			noWalkways = walks[i].B;
		}
		else
		{
			noWalkways += walks[i].B-walks[i-1].E;
		}
	}
	noWalkways += x-walks[n-1].E;
	if ((noWalkways/(long double)r)>=tt)
	{
		time = t+(noWalkways-tt*r)/(long double)s;
		tt = 0;
	}
	else
	{
		time = noWalkways/(long double)r;
		tt -= time;
	}
	while(tt>0)
	{
		int mini = -1;
		for (i=0;i<n;++i)
		{
			if (walks[i].bRun == false)
			{
				if (mini==-1 || walks[mini].w>walks[i].w)
				{
					mini = i;
				}
			}
		}
		if (mini==-1)
			break;
		walks[mini].bRun = true;
		if ((walks[mini].len/(long double)(walks[mini].w+r))>tt)
		{
			time += tt+(walks[mini].len-tt*(walks[mini].w+r))/(long double)(walks[mini].w+s);
			tt = 0;
		}
		else
		{
			time += walks[mini].len/(long double)(walks[mini].w+r);
			tt -= walks[mini].len/(long double)(walks[mini].w+r);
		}
	}
	for (i=0;i<n;++i)
	{
		if (walks[i].bRun==false)
		{
			time += walks[i].len/(long double)(walks[i].w+s);
		}
	}
	print("%.7llf", time);
}