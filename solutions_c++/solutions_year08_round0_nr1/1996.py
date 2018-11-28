#include <stdlib.h>
#include <stdio.h>
#include <string.h>

typedef char str[100];
int count[100];

int pr(int n,int k)
{
	int p=1;
	for(int i=0;i<n;i++) if(i!=k)p*=count[i];
	return p;
}

int eq(str s1, str s2)
{
	int i;
	for(i=0;s1[i]!=10,s2[i]!=10;i++)
		if(s1[i]!=s2[i]) break;
	return (s1[i]==s2[i]);
}

int main(int argc, char* argv)
{
	FILE *fin, *fout;
	int n=0,s=0,q=0,i,j,k,I,j0,min_count,res,sr1,sr2;
	char c;
	str srch[101];
	str qrty[1000];

	fin=fopen("A-small-attempt4.in", "r");
	fout=fopen("A.txt", "w");
	fscanf(fin, "%d", &n);
	for(I=0;I<n;I++)
	{
		fscanf(fin, "%d", &s);
		fscanf(fin,"%c",&c);
		for(j=0;j<s;j++)
			for(k=0,c=1;c!=10;k++)
			{
				fscanf(fin, "%c", &c);
				srch[j][k]=c;
			}
		fscanf(fin, "%d", &q);
		fscanf(fin,"%c",&c);
		for(j=0;j<q;j++)
			for(k=0,c=1;c!=10;k++)
			{
				fscanf(fin, "%c", &c);
				qrty[j][k]=c;
			}

	res=0;
	sr1=100;
	for(j0=0;j0<q;)
	{
		for(j=0;j<s;j++) count[j]=0;
		for(j=j0;j<q && pr(s,sr1)==0;j++) 
			for(k=0;k<s;k++) if(k!=sr1 && eq(qrty[j],srch[k]))
				count[k]++;
		
		if(pr(s,sr1)==0)
			break;
		else
		{
			sr1=k;
			j0=j-1;
			printf("%d [pos %d] -> ", sr1,j0);
			res++;
		}

	}
	printf("end case %d\n",I+1);
	fprintf(fout, "Case #%d: %d\n", I+1, res);		

	}
	fclose(fin);
	fclose(fout);
	return 0;
}