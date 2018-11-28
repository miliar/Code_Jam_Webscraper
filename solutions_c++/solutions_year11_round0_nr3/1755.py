#include <stdio.h>

int main()
{
	FILE *fin,*fout;
	fin=fopen("input.txt","r");
	fout=fopen("output.txt","w");	
	int min=-1,sum,xsum;
	int t,n,c;
	fscanf(fin,"%d",&t);
	for(int i=0;i<t;i++)
	{
		fprintf(fout,"Case #%d: ",i+1);
		fscanf(fin,"%d",&n);
		xsum=0;
		sum=0;
		min=-1;
		for(int j=0;j<n;j++)
		{
			fscanf(fin,"%d",&c);
			if(min == -1)
				min = c;
			else if(min > c)
				min = c;
			xsum^=c;
			sum+=c;
		}
		sum-=min;
		if(xsum!=0)
			fprintf(fout,"NO");
		else
			fprintf(fout,"%d",sum);
		if(i!=t-1)
			fprintf(fout,"\n");
	}
	return 0;
}