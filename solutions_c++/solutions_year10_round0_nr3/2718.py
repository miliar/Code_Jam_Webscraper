#include<stdio.h>
int main()
{
	long double R,k,g[1000],y,j,c;
	int x,T,N,i,d;

	FILE *ifp=fopen("C-small.in","r");
	FILE *ofp=fopen("C-small.out","w");

	fscanf(ifp,"%d\n",&T);
	for(x=1;x<=T;x++)
	{
		fscanf(ifp,"%Lf %Lf %d\n",&R,&k,&N);
		for(i=0;i<N;i++)
			fscanf(ifp,"%Lf",&g[i]);
		fscanf(ifp,"\n");
		i=0;y=0;
		for(j=0,c=0;j<R;j++,c=0)
		{
			for(c=0,d=0;c<k&d<N;d++)
			{
				c+=g[i++];
				if (i>=N)
					i=0;
			}

			if(c>k)
			{
				if(i==0)
					i=N-1;
				else
					i--;
				c-=g[i];
			}
			y+=c;
		}
		printf("Case #%d: %.0Lf\n",x,y);
		fprintf(ofp,"Case #%d: %.0Lf\n",x,y);
	}
	fclose(ifp);
	fclose(ofp);
	return 0;
}