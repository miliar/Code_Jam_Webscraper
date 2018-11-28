#include<stdio.h>

int gcd2(int a, int b)
{
	if(a<0) a*=-1;
	if(b<0) b*=-1;
	if(b==0) return a;
	while(b>0)
	{
		int temp=a%b;
		a=b;
		b=temp;
	}
	return a;
}
int main()
{
	int C,N,t[100];

	FILE *fin=fopen("input.txt","r");
	FILE *fout=fopen("output.txt","w");
	fscanf(fin,"%d",&C);
	for(int i=1;i<=C;i++)
	{
		fscanf(fin,"%d",&N);
		for(int j=0;j<N;j++) fscanf(fin,"%d",t+j);
		int result=t[0]-t[1];
		if(result<0) result*=-1;
		if(N==3)
			result=gcd2(result,t[0]-t[2]);
		if(t[0]%result==0)
			fprintf(fout,"Case #%d: %d\n",i,0);
		else fprintf(fout,"Case #%d: %d\n",i,result-(t[0]%result));
	}
	return 0;
}