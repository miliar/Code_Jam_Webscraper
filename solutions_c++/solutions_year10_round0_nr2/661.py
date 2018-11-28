#include<stdio.h>

int mcm(int a,int b)
{
	int tmp;
	while(tmp=(b%a))
	{
		b=a;
		a=tmp;
	}
	return a;
}

void main()
{
	FILE *in,*out;
	in = fopen("FairWarning.in","r");
	out = fopen("FairWarning.out","w+");
	int C,N,c,i,first,a,b,result,t[3],j,tmp;
	fscanf(in,"%d",&C);
	for(c=0;c<C;c++)
	{
		fscanf(in,"\n%d",&N);
		for(i=0;i<N;i++)
			fscanf(in," %d",&t[i]);
		for(i=0;i<N;i++)
			for(j=i+1;j<N;j++)
				if(t[i]>t[j])
				{
					tmp=t[i];
					t[i]=t[j];
					t[j]=tmp;
				}
		first=t[0];
		a=t[1]-first;
		for(i=2;i<N;i++)
		{
			b=t[i]-first;
			if(a)
				a=mcm(a,b);
			else
				a=b;
		}
		result=first%a;
		if(result)
			result=a-result;
		fprintf(out,"Case #%d: %d\n",c+1,result);
	}
	fclose(in);
	fclose(out);
}