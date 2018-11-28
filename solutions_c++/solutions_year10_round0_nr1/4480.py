#include <stdio.h>

void main()
{
	int p[30], s[30];
	int N,i,j,k,n,ok;
	long K;
	FILE *ip,*op;
	ip=fopen("input.txt","r");
	op=fopen("output.txt","w");
	fscanf(ip,"%d",&n);
	for (i=0;i<n;i++)
	{
		ok=0;\
		fscanf(ip,"%d %d",&N, &K);
		for (j=0;j<30;j++)
		{
			p[j]=0;
			s[j]=0;
		}
		p[0]=1;
		for (j=0;j<K;j++)
		{
			for (k=0;k<N;k++)
				if (p[k]==1)
					s[k]=(s[k]+1)%2;
			for (k=0;k<N-1;k++)
			{
				if (p[k]==1 && s[k]==1)
					p[k+1]=1;
				else
					p[k+1]=0;
			}
		}
		for (k=0;k<N;k++)
			{
				if (p[k]==0 || s[k]==0)
					break;
				if (k==N-1)
					ok=1;
			}
		if (ok==1)
			fprintf(op,"Case #%d: ON\n",i+1);
		else
			fprintf(op,"Case #%d: OFF\n",i+1);
	}
	fcloseall();
}