#include<stdio.h>
int main(void)
{
	int T,i,N,S,P,j,t[100],count,count2;
	FILE * rf, * wf;
	rf = fopen ("b.txt","r");
	wf = fopen ("b2.txt","w");
	while(fscanf(rf,"%d",&T)==1)
	{
		for(i=0;i<T;i++)
		{
			count=0;
			count2=0;
			fscanf(rf,"%d %d %d",&N,&S,&P);
			for(j=0;j<N;j++)
			{
				fscanf(rf,"%d",&t[j]);
			}
			if(P==0)
				fprintf(wf,"Case #%d: %d\n",i+1,N);
			else if(P==1)
			{
				for(j=0;j<N;j++)
					if(t[j]>=1)
						count++;
				fprintf(wf,"Case #%d: %d\n",i+1,count);
			}
			else
			{
				for(j=0;j<N;j++)
				{
					printf("%d %d\n",t[j],3*P-2);
					if(t[j]>=(3*P-2))
						count++;
					if(t[j]>=(3*P-4))
						count2++;
				}
				printf("%d %d\n",count,count2);
				if(S>=(count2-count))
					fprintf(wf,"Case #%d: %d\n",i+1,count2);
				else
					fprintf(wf,"Case #%d: %d\n",i+1,count+S);
			}
		}
	}
	return 0;
}
