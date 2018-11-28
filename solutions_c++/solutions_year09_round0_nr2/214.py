#include "stdio.h"
int al[105][105],x[105][105],y[105][105],xx[30],yy[30];
char dd[105][105];
void search(int a,int b)
{
	int o,di;
	if(x[a][b]!=-1)
		return;
	o=0;
	di=al[a][b];
	if(al[a-1][b]<di)
	{
		o=1;
		di=al[a-1][b];
	}
	if(al[a][b-1]<di)
	{
		o=2;
		di=al[a][b-1];
	}
	if(al[a][b+1]<di)
	{
		o=3;
		di=al[a][b+1];
	}
	if(al[a+1][b]<di)
	{
		o=4;
		di=al[a+1][b];
	}
	if(o==0)
	{
		x[a][b]=a;
		y[a][b]=b;
	}
	else if(o==1)
	{
		search(a-1,b);
		x[a][b]=x[a-1][b];
		y[a][b]=y[a-1][b];
	}
	else if(o==2)
	{
		search(a,b-1);
		x[a][b]=x[a][b-1];
		y[a][b]=y[a][b-1];
	}
	else if(o==3)
	{
		search(a,b+1);
		x[a][b]=x[a][b+1];
		y[a][b]=y[a][b+1];
	}
	else if(o==4)
	{
		search(a+1,b);
		x[a][b]=x[a+1][b];
		y[a][b]=y[a+1][b];
	}
}
int main()
{
	int kase,kk,i,k,j,n,m,l;
	scanf("%d",&kase);
	for(kk=1;kk<=kase;kk++)
	{
		scanf("%d%d",&m,&n);
		for(i=0;i<=n+1;i++)
		{
			al[0][i]=10005;
			al[m+1][i]=10005;
		}
		for(i=0;i<=m+1;i++)
		{
			al[i][0]=10005;
			al[i][n+1]=10005;
		}
		for(i=1;i<=m;i++)
			for(k=1;k<=n;k++)
				scanf("%d",&al[i][k]);
		for(i=1;i<=m;i++)
			for(k=1;k<=n;k++)
			{
				x[i][k]=-1;
				y[i][k]=-1;
			}
		for(i=1;i<=m;i++)
			for(k=1;k<=n;k++)
				search(i,k);
/*		for(i=1;i<=m;i++)
		{
			for(k=1;k<=n;k++)
				printf("%d %d-",x[i][k],y[i][k]);
			printf("\n");
		}*/
		j=0;
		for(i=1;i<=m;i++)
			for(k=1;k<=n;k++)
			{
				for(l=0;l<j;l++)
					if(x[i][k]==xx[l]&&y[i][k]==yy[l])
					{
						dd[i][k]=l+97;
						break;
					}
				if(l==j)
				{
					xx[j]=x[i][k];
					yy[j]=y[i][k];
					dd[i][k]=j+97;
					j++;
				}
			}
		printf("Case #%d:\n",kk);
		for(i=1;i<=m;i++)
			for(k=1;k<=n;k++)
			{
				printf("%c",dd[i][k]);
				if(k!=n)
					printf(" ");
				else
					printf("\n");
			}
	}
	return 0;
}