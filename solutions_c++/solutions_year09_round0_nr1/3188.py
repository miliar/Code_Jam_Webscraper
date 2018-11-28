#include<stdio.h>
#include<string.h>
#include <ctype.h>
#include<stdlib.h>
#include <iostream>
#include <cmath>

int main(){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w+",stdout);

	int i,j,k,n,x=0,a=0,L,D,N,K[501],t,d;
	char str[5000][16],alien[501][1000];
	scanf("%d",&L);
	scanf("%d",&D);
	scanf("%d",&N);
	while(getchar()!='\n');

	for(i=0;i<D;i++)
		gets(str[i]);
	for(i=0;i<N;i++)
		gets(alien[i]);
	for(i=0;i<N;i++)
		K[i]=0;

	for(n=0;n<N;n++)
	{
		for(i=0;i<D;i++)
		{
			a=0;
			x=0;
			for(j=0;j<L;j++)
			{
				t=strlen(alien[n]);
				for(k=x;k<t;k++)
				{
					if(alien[n][k]=='(')
					{
						x=k;
						do
						{
							x++;
							if(alien[n][x]==str[i][j]) a++;
						}while(alien[n][x]!=')');
						x++;
						break;
					}
					else
					{
						if(str[i][j]==alien[n][k])
						{
							a++;
							x++;
							break;
						}
						else
						{
							x++;
							break;
						}
					}
				}
			}
			if(a==L) K[n]++;
		}
	}
	for(i=0;i<N;i++)
		printf("Case #%d: %d\n",i+1,K[i]);
}