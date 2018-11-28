// Alien Language.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"

#include "stdio.h"
#include "string.h"
#include "stdlib.h"
#define MAX 250
#define MORE 1000
char **ds,*t;
char ls[15][MAX];
bool *h;
int lsl[15];
int l,d,n;
int ss;
bool has(int i,int j)
{
	for(int k=0;k<lsl[j];k++)
	{
		if(ds[i][j]==ls[j][k])
			return true;
	}
	return false;
}

int main()
{
	FILE *in;
	in=fopen("d:\\A-large.in.txt","rb");
	FILE *out;
	out=fopen("d:\\A-large.out.txt","wb");
	int sl;
	int i,j,k,x;
	fscanf(in,"%d %d %d",&l,&d,&n);
	ds=new char*[d];
	h=new bool[d];
	memset(h,0,d);
	ss=0;
	bool hasit=false;
	int se[15];
	t=new char[MORE];
	memset(se,0,15);
	for(i=0;i<d;i++)
	{
		ds[i]=new char[MAX];
		fscanf(in,"%s",ds[i]);
	}
	for(i=1;i<=n;i++)
	{
		fscanf(in,"%s",t);
        sl=strlen(t);
		for(j=0,x=0,k=0;j<sl&&k<l;)
		{
            if(t[j]!='(')
			{
				ls[k][0]=t[j];
				lsl[k]=1;
				k++;
				j++;
				x=0;
				
				continue;
			}
			else
			{
                j++;
				x=0;
				while(j<sl&&t[j]!=')')
				{
					ls[k][x]=t[j];
					x++;
					j++;
				}
				ls[k][x]='\0';
				lsl[k]=x;
				k++;
				j++;
			}
		}
		ss=0;
		memset(h,0,d);
		for(k=0;k<d;k++)
		{
			hasit=true;
			for(j=0;j<l;j++)
			{
				if(has(k,j)==false)
				{
					hasit=false;
					break;
				}
			}
			if(hasit&&h[k]==0)
			{
				//printf("%s\n",ds[k]);
				h[k]=1;
				ss++;
			}
		}
		//printf("Case #%d: %d\n",i,ss);
		fprintf(out,"Case #%d: %d",i,ss);
		if(i!=n)
			fprintf(out,"\n");
	}
	return 0;
}


