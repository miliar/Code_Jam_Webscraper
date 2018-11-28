// CodeJam.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"


int _tmain(int argc, _TCHAR* argv[])
{
	int L,D,N,i,j,k,l,m,n,o;
	char s[1000];
	FILE* f=fopen("..\\input.txt","r");
	FILE* fo=fopen("output.txt","w");
	fscanf(f,"%d %d %d",&L,&D,&N);
	char a[5000][15];
	for (i=0;i<D;i++)
		fscanf(f,"%s",&a[i]);
	for (i=0;i<N;i++)
	{
		fscanf(f,"%s",&s);
		j=0;
		for (m=0;m<D;m++)
		{
		  k=1;
		  l=0;
		  n=0;
		  while (s[l]&&k)
		  {
			if (s[l]=='(')
			{
				l++;
				o=0;
				while (s[l]!=')')
				{
					if (s[l]==a[m][n]) o=1;
					l++;
				}
				k=o;
			}
			else
				if (s[l]!=a[m][n]) k=0;
			l++;
			n++;
	      }
		  j+=k;
		}
		fprintf(fo,"Case #%d: %d\n",i+1,j);
	}
	fclose(f);
	fclose(fo);
	return 0;
}

