#include<stdio.h>

int winner(int a,int b)
{
	if(a>b)
	{
		int temp=a;
		a=b;
		b=temp;
	}
	if(a==0) return 0;
	else if(2*a<=b) return 1;
	else if(a==b) return 0;
	return 1-winner(a,b-a);
}

int main()
{
	FILE *fin=fopen("input.txt","r");
	FILE *fout=fopen("output.txt","w");

	int T,A1,A2,B1,B2;

	fscanf(fin,"%d",&T);

	for(int i=1;i<=T;i++)
	{
		fscanf(fin,"%d%d%d%d",&A1,&A2,&B1,&B2);

		int kmin=(A1+1)/2, kmax=A1*2;

		if(kmin<B1) kmin=B1;
		if(kmax>B2) kmax=B2;
		
		kmin=B1;
		kmax=B2;

		int result=(A2-A1+1)*(B2-B1+1);
		for(int j=A1;j<=A2;j++)
			for(int k=kmin;k<=kmax;k++)
			{
				if(winner(j,k)==0) result--;
			}

		fprintf(fout,"Case #%d: %d\n",i,result);
	}
	return 0;
}