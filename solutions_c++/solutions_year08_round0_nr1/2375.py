#include <stdio.h>
#include <string.h>

void main()
{
	int n,s,q,i,j,k,l,mm,min;
	char name[100][101];
	char tempname[101];
	int count[1000][100];
	FILE *fin,*fout;
	fin=fopen("A-large.in","r");
	fscanf(fin,"%d\n",&n);
	fout=fopen("A-large.out","w");
	for (i=0;i<n;i++)
	{
		fscanf(fin,"%d\n",&s);
		for (j=0;j<s;j++)
		{
			fgets(name[j],200,fin);
		}
		fscanf(fin,"%d\n",&q);
		for (j=0;j<q;j++)
			for (k=0;k<s;k++)
				count[j][k]=0;
		for (j=0;j<q;j++)
		{
			fgets(tempname,200,fin);
			if (j==0) for (k=0;k<s;k++) if (strcmp(name[k],tempname)==0) count[0][k]=-1;else;
			else for (k=0;k<s;k++)
			{
				if (strcmp(name[k],tempname)==0) count[j][k]=-1;
				else if (count[j-1][k]!=-1) count[j][k]=count[j-1][k];
				else{
					mm=20000;
					for (l=0;l<s;l++) if ((l!=k)&&(count[j-1][l]<mm)) mm=count[j-1][l];
					count[j][k]=mm+1;
				}
			}
		}
		min=20000;
		for (j=0;j<s;j++)
		{
			if ((min>count[q-1][j])&&(count[q-1][j]!=-1)) min=count[q-1][j];
		}
		fprintf(fout,"Case #%d: %d \n",i+1,min);
	}
	fclose(fin);
	fclose(fout);	
}