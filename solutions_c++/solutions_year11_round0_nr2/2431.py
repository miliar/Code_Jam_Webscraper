// code.cpp : Defines the entry point for the console application.
//
#define _CRT_SECURE_NO_WARNINGS 1
#include "stdafx.h"


int _tmain(int argc, _TCHAR* argv[])
{
	FILE *fi,*fo;
	int t,ti,c,d,n,i,j,no;
	bool ds[30][30],was[30];
	char cs[30][30];

	bool hascombined;

	char si[200],so[200];
	char tmp[10];


	fi=fopen("B.in","r");
	fo=fopen("B.out","w");

	fscanf(fi,"%d",&t);


	for (ti=0;ti<t;ti++)
	{
		for (i=0;i<30;i++)
		{
			was[i]=0;
			for (j=0;j<30;j++)
			{
				cs[i][j]=0;
				ds[i][j]=false;
			}
		}
		fscanf(fi,"%d",&c);
		for (i=0;i<c;i++) 
		{
			fscanf(fi,"%s",tmp);
			cs[tmp[0]-'A'][tmp[1]-'A']=tmp[2];
			cs[tmp[1]-'A'][tmp[0]-'A']=tmp[2];
		}
		fscanf(fi,"%d",&d);
		for (i=0;i<d;i++)
		{
			fscanf(fi,"%s",tmp);
			ds[tmp[0]-'A'][tmp[1]-'A']=true;
			ds[tmp[1]-'A'][tmp[0]-'A']=true;
		}
		fscanf(fi,"%d",&n);
		fscanf(fi,"%s",si);
		no=0;
		for (i=0;i<n;i++)
		{
			so[no]=si[i];
			no++;
			hascombined=false;
			while (no>=2 && cs[so[no-1]-'A'][so[no-2]-'A'])
			{
				so[no-2]=cs[so[no-1]-'A'][so[no-2]-'A'];
				no--;
				hascombined=true;
			}
			if (!hascombined)
			{
				for (j=0;j<no-1;j++) 
				{
					if (ds[so[j]-'A'][so[no-1]-'A'])
					{
						no=0;
						break;
					}
				}
			}
		}
		fprintf(fo,"Case #%d: [",ti+1);
		for (i=0;i<no;i++)
		{
			if (i==0) fprintf(fo,"%c",so[i]);
			else fprintf(fo,", %c",so[i]);
		}
		fprintf(fo,"]\n");
	}
	fclose(fi);
	fclose(fo);
	return 0;
}

