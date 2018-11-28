#include <windows.h>
#include <stdio.h>
#include <stdlib.h>

//#define FILENAME "sample"
#define FILENAME "A-large"
//#define FILENAME "A-small-attempt0"

#define FULLNAME(x) FILENAME##x

#define INFILE FULLNAME(".in")
#define OUTFILE FULLNAME(".out")

#define FIN(arg,...) fscanf_s(fin, arg, __VA_ARGS__)

#define FOUT(arg,...) fprintf(fout, arg##"\n", __VA_ARGS__)
#define CASE fprintf(fout, "Case #%d: ", i+1)

//#define FOUT(arg,...) printf(arg##"\n", __VA_ARGS__)
//#define CASE printf("Case #%d: ", i+1)

FILE *fin,*fout;

int primes[500];
int nPrimCnt;

bool testHappy(int n, int base)
{
	int nn=0;
	int cnt=0;
	while (n!=1 && cnt<10)
	{
		cnt++;
		nn=0;
		while (n>0)
		{
			int x = n%base;
			n /= base;
			nn+=x*x;
		}
		n=nn;
	}
	return n==1;
}

void main()
{
	int N=0;
	int i=0,j=1,k=0;
	char c;
	fopen_s(&fin,INFILE, "rt");
	fopen_s(&fout,OUTFILE, "wt");
	FIN("%d", &N);
	for (int i=0;i<N;++i)
	{
		printf("%d\n", i);
		nPrimCnt = 0;
		do
		{
			FIN("%d", &primes[nPrimCnt++]);
			c = fgetc(fin);
		}while (c!=0x0D && c!=0x0A && !feof(fin));
 		CASE;
		bool bItIs = false;
		for (j=2;!bItIs;++j)
		{
			bItIs = true;
			for (k=0;k<nPrimCnt && bItIs;++k)
			{
				bItIs &= testHappy(j, primes[k]);
			}
		}
		FOUT("%d", j-1);
		nPrimCnt = 0;
	}
	fclose(fout);
	fclose(fin);
}