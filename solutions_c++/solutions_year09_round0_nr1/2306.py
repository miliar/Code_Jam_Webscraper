#include <stdio.h>
#include <stdlib.h>
#include <conio.h>
#include <string.h>

#define D_DATA_MAX 16   //big
#define N_DATA_MAX 421 //big
#define D_MAX 5000 //big
#define N_MAX 500 //big
#define L_MAX 15 //big

void main()
{
	int i,j,k,p,m,f;
	char word[L_MAX];
	char stack[L_MAX][29]={0};
	int l,d,n;
	int count;
	char ddata[D_MAX][D_DATA_MAX],ndata[N_MAX][N_DATA_MAX];
	FILE *fp=fopen("A-large.in","r"),*ft=fopen("A-large.out","w");;
	if(!fp) exit(0);
	if(!ft) exit(0);
	fscanf(fp,"%d %d %d\n",&l,&d,&n);
	for(i=0;i<d;i++)
	{
		fscanf(fp,"%s\n",ddata[i]);
	}
	for(i=0;i<n;i++)
	{
		fscanf(fp,"%s\n",ndata[i]);
	}
	for(i=0;i<n;i++)
	{
		k=0;
		p=0;
		f=0;
		for(j=0;ndata[i][j]!=NULL;j++)
		{
			if(ndata[i][j]=='(')
			{
				f=1;
				continue;
			}
			else if(ndata[i][j]==')')
			{
				f=0;
				k++;
				p=0;
				continue;
			}
			stack[k][p]=ndata[i][j];
			if(f==0)
			{
				k++;
				p=0;
			}
			else
			{
				p++;
			}
		}
		count=0;
		for(j=0;j<d;j++)
		{
			f=0;
			for(k=0;k<l;k++)
			{
				for(p=0;stack[k][p]!=0;p++)
				{
					if(stack[k][p]==ddata[j][k])
					{
						f=1;
						break;
					}
					else
					{
						f=0;
					}
				}
				if(f==0)
				{
					break;
				}
			}
			if(f==1)
			{
				count++;
			}
		}
		fprintf(ft,"Case #%d: %d\n",i+1,count);
		for(j=0;j<L_MAX;j++)
		{
			for(k=0;k<29;k++)
			{
				stack[j][k]=0;
			}
		}
	}
	fclose(fp);
	fclose(ft);
	getch();
}
