#include<stdio.h>
#include<string.h>
FILE* fin;
FILE* fout;

int min(int a, int b)
{
	return (a<b)?a:b;
}

int main(void)
{
	fin=fopen("swinging.in", "r");
	fout=fopen("swinging.out", "w");
	int T;
	fscanf(fin, "%d", &T);
	for(int tnum=1; tnum<=T; tnum++)
	{
		fprintf(fout, "Case #%d: ", tnum);
		int N;
		fscanf(fin, "%d", &N);
		int* d = new int[N];
		int* l = new int[N];
		int* b = new int[N];
		for(int i=0; i<N; i++)
		{
			fscanf(fin, "%d %d", &d[i], &l[i]);
			b[i]=0;
		}
		b[0]=l[0]=d[0];
		int D;
		fscanf(fin, "%d", &D);
		bool done=false;
		for(int i=0; i<N && !done; i++)
		{
			if(D<=d[i]+b[i])
				done=true;
			//printf("%d %d %d\n", D, d[i], b[i]);
			for(int j=i+1; j<N && d[j]<=d[i]+b[i]; j++)
			{
				if(b[j]<d[j]-d[i])
					b[j]=min(d[j]-d[i], l[j]);
			}
		}
		if(done)
			fprintf(fout, "YES");
		else
			fprintf(fout, "NO");
		fprintf(fout, "\n");
		//getchar();
	}
	return 0;
}
