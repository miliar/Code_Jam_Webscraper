#include<stdio.h>

void main()
{
	FILE *in,*out;
	in = fopen("ThemePark.in","r");
	out = fopen("ThemePark.out","w+");
	int T,R,N,k,g[1000],r,t,round,i;
	__int64 sum;
	fscanf(in,"%d",&T);
	for(t=0;t<T;t++)
	{
		printf("%d\n",t);
		fscanf(in,"\n%d %d %d\n",&R, &k ,&N);
//		printf("\n%d %d %d\n",R,k,N);
		sum=0;
		for(i=0;i<N;i++)
		{
			fscanf(in, "%d ", &g[i]);
			sum+=g[i];
		}
		if(((__int64)k)>=sum)
			sum*=R;
		else
		{
			sum=0;
			i=0;
			round=0;
			for(r=0;r<R;r++)
			{
				while((round+g[i])<=k)
				{
					round+=g[i];
					if(++i==N)
						i=0;
				}
//				printf("%d ",round);
				sum+=round;
				round=0;
			}
		}
		fprintf(out,"Case #%d: %I64u\n",t+1,sum);
	}
	fclose(in);
	fclose(out);
//	printf("\nDone.\n");
//	getchar();
}