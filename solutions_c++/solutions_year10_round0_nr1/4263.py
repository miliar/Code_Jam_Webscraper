#include<stdio.h>
#include<string.h>
#include<memory.h>
int main()
{
	int t,h=1,i,k,n,j,a[10];


char filename[32];
	char infile[32], outfile[32];
	scanf("%s", filename);
	strcpy(infile,filename); strcpy(outfile, filename);
	strcat(infile, ".in"); strcat(outfile, ".out");
	FILE *fp=fopen(infile, "r"), *ofp=fopen(outfile, "w");
	
	fscanf(fp,"%d",&t);
	while(h<=t)
	{
		fscanf(fp,"%d%d",&n,&k);
	
		for(i=0;i<n;i++)
		a[i]=0;
		for(i=1;i<=k;i++)
		{
			for(j=0;j<n;j++)
			{
				if(a[j]==0)
				{
					a[j]=1;
					break;
				}
				else
				{
					a[j]=0;
				}
			}
		}
		for(i=0;i<n;i++)
		{
		if(a[i]==0)
		break;
		}
		if(i==n)
	fprintf(ofp,"Case #%d: ON\n",h);
	else
	fprintf(ofp,"Case #%d: OFF\n",h);	
	h++;
		
	}
	
}
			
