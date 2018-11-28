#include<stdio.h>

int snapp(int n);

int main(int argc, char *argv[]) 
{
	FILE *in=NULL,*out=NULL;
	int i=0, N, K, activate, T;

	in   = fopen(argv[1],"r");
	out = fopen(argv[2],"w");
	if(!in || !out){    /*file opening failed*/
		return -1;
	}
	


	fscanf(in,"%d \n",&T);

	//while (!feof(newFile)) 
	for (i=1; i<=T; ++i)
	{

		fscanf(in,"%d %d \n",&N,&K);
		activate = snapp(N);
		if ( (K % (activate+1) ) == activate)
		{
			fprintf(out,"Case #%d: ON\n",i);
		}
		else 
		{
			fprintf(out,"Case #%d: OFF\n",i);
		}

	}
    return 0;
}

int snapp(int n)
{
	if (n==1) return 1;
	return 2*snapp(n-1) + 1;
}
