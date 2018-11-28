#include<stdio.h>
#include<math.h>
#define show(A) fprintf(ofp2,"%s : %ld\n",#A,A)
int main()
{
	int T,N,x,i;
	long int K,l,r;
	
	
	FILE *ifp = fopen("A-large.in","r");
	FILE *ofp = fopen("A-large.out","w");
	FILE *ofp2 = fopen("A-large.txt","w");

	fscanf(ifp,"%d\n",&T);
	
	for(x=1;x<=T;x++)
	{
		fprintf(ofp2,"\n*******************");
		show(x);
		fscanf(ifp,"%d %ld\n",&N,&K);
		show(N);show(K);
		l=pow(2.0,N);
		show(l);
		r=K%l;
		show(r);
		if(r==(l-1))
			fprintf(ofp,"Case #%d: ON\n",x);
		else
			fprintf(ofp,"Case #%d: OFF\n",x);
	}

	fclose(ifp);
	fclose(ofp);
	
	return 0;
}