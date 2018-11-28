#include <stdio.h>
#include <stdlib.h>
#include <math.h>


int main(int argc, char* argv[])
{
	int T;
	long long N, L, H;
	long long* play;
	bool flag;
	int nota;
	char** ch;
	FILE *f_in;
	FILE *f_out;
	f_in=fopen("C-small-attempt0.in","rt");
	f_out=fopen("out.txt","wt");
	fscanf(f_in,"%d",&T);
	for(int r=0; r<T; r++)
	{
		fscanf(f_in,"%lld",&N);
		fscanf(f_in,"%lld",&L);
		fscanf(f_in,"%lld",&H);
		play=new long long[N];
		char tmp;
		fscanf(f_in,"%c",&tmp);
		for(int j=0; j<N; j++)
			fscanf(f_in,"%lld",&play[j]);
		bool flag;
		nota=L-1;
		for(int i=L; i<=H; i++)
		{
			flag=true;
			for(int j=0; j<N; j++)
				if((int)i%(int)play[j]!=0&&(int)play[j]%(int)i!=0)
				{
					flag=false;
					break;
				}
			if(flag)
			{
				nota=i;
				break;
			}
		}
		if(nota==L-1)
			fprintf(f_out,"Case #%d: NO\n", r+1);
		else
			fprintf(f_out,"Case #%d: %d\n", r+1, nota);
	}
	return 0;
}