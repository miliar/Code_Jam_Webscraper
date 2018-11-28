// cj2.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

int nextGroup(int a,int b)
{
	if(a+1<b)
		return a+1;
	else return 0;
}

void main()
{
	int i,j;
	int rides,cap,groups,group[15],no_inp;
	FILE *inp=fopen("inp","r");
	FILE *fout=fopen("out","w");
	fscanf(inp,"%d",&no_inp);
	int money=0,marker=0;
	for(i=0;i<no_inp;i++)
	{
		money=0;marker=0;
		fscanf(inp,"%d",&rides);
		fscanf(inp,"%d",&cap);
		fscanf(inp,"%d",&groups);
		for(j=0;j<groups;j++)
			fscanf(inp,"%d",&group[j]);
		for(j=0;j<rides;j++)
		{
			int start_group=marker;
			int cur_cap=0;
			while(cur_cap+group[marker]<=cap)
			{
				cur_cap=cur_cap+group[marker];
				marker=nextGroup(marker,groups);
				if(marker==start_group)
					break;
			}
			money=money+cur_cap;
		}
		fprintf(fout,"Case #%d: %d\n",i+1,money);
	}
}

