#include <iostream>
#include <stdio.h>
#include <conio.h>
#include <string>
using namespace std;
int N[100], S[100], p[100], t[100][100], y[100];
void main()
{
	int T;
	int i,j;
	scanf("%d",&T);
	int q;
	for (i=0;i<T;i++)
	{
		scanf("%d",&N[i]);
		scanf("%d",&S[i]);
		scanf("%d",&p[i]);
		for (j=0;j<N[i];j++)
		{
			scanf("%d",&q);
			t[i][j]=q;
		}
		y[i]=1;
	}
	for (i=0;i<T;i++)
	{
		y[i]=0;
		q=S[i];
		for (j=0;j<N[i];j++)
		{
			if ((t[i][j]+2)/3>=p[i]) y[i]++;
			else
			{
				if (q>0 && (t[i][j]+2)/3+1>=p[i] && t[i][j]>1 && t[i][j]%3!=1)
				{
					q--;
					y[i]++;
				}
			}
		}
	}
	for (i=0;i<T;i++) printf("Case #%d: %d\n",i+1,y[i]);
	getch();
}