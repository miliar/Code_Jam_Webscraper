#include<stdio.h>

void main()
{
	FILE *in,*out;
	in = fopen("Chicks.in","r");
	out = fopen("Chicks.out","w+");
	int C,N,K,B,T,c,X[50];
	int i,j,k,result;
	char able[50];
	fscanf(in,"%d",&C);
	for(c=0;c<C;c++)
	{
		fscanf(in,"\n%d %d %d %d\n",&N,&K,&B,&T);
		for(i=0;i<N;i++)
			fscanf(in,"%d ", &X[i]);
		for(i=0;i<N;i++)
		{
			fscanf(in,"%d ", &j);
			able[i]=((T*j)>=(B-X[i])?1:0);
		}
		k=0;
		result=0;
		for(i=N;i && K;i--)
			if(able[i-1])
			{
				K--;
				result+=k;
			}
			else
				k++;
		if(K)
			fprintf(out,"Case #%d: IMPOSSIBLE\n",c+1);
		else
			fprintf(out,"Case #%d: %d\n",c+1,result);
	}
	fclose(in);
	fclose(out);
}