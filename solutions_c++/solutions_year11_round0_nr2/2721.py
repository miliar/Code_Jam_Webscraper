#include<stdio.h>
#include "stdafx.h"
int t,T,i,j,k,z,N,C,D;
bool ok;
char a[37][3],b[29][2];
char S[101],s[101];


int main()
{
	freopen("outputB.txt","w",stdout);
	int T,t;
	scanf("%d",&T);
	for (t=1;t<=T;t++)
	{
		scanf("%d",&C);
		for (i=0;i<C;i++)
			scanf("%s",&a[i]);
		scanf("%d",&D);
		for (i=0;i<D;i++)
			scanf("%s",&b[i]);
		scanf("%d%s",&N,s);
		k=0;
		S[k++]=s[0];
		for (i=1;i<N;i++)
		{
			ok=true;
			for (z=0;z<C;z++)
				if (a[z][0]==s[i]&&a[z][1]==S[k-1]||
					a[z][1]==s[i]&&a[z][0]==S[k-1])
					{
						S[k-1]=a[z][2];
						ok=false;
					}
			if (ok)
			{
				for (z=0;z<D;z++)
					if (b[z][0]==s[i])
					{
						for (j=0;j<k;j++)
							if (b[z][1]==S[j])
							{
								k=0;
								S[k]=0;
								ok=false;
							}
					}
					else
					if (b[z][1]==s[i])
					{
						for (j=0;j<k;j++)
							if (b[z][0]==S[j])
							{
								k=0;
								S[k]=0;
								ok=false;
							}
					}										
			}
			if (ok)
				S[k++]=s[i];
			S[k]=0;
			//printf("%s\n",S);
		}
		printf("Case #%d: [",t);
		if (k>0)
		{
			for (i=0;i<k-1;i++)
				printf("%c, ",S[i]);
			printf("%c",S[k-1]);
		}
		printf("]\n");
	}
	
}
