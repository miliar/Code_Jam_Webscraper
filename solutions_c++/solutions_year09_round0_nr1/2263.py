// Alien.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void main()
{
	int i,j,k,l,d,n,flag,count;
	char in[5000][15],test[15][26],ch;
	char *p;

	FILE *fp,*ofp;
	fopen_s(&fp,"A-large.in","r");
	fopen_s(&ofp,"Output.txt","w");
	fscanf(fp,"%d%d%d\n",&l,&d,&n);
	for(i=0;i<d;i++)
		fscanf(fp,"%s\n",in[i]);
	for(i=0;i<n;i++)
	{
		for(j=0;j<15;j++)
			for(k=0;k<26;k++)
				test[j][k] = 0;
		for(j=0;j<l;j++)
		{
			fscanf(fp,"%c",&ch);
			if(ch == '(')
			{
				k = 0;
				fscanf(fp,"%c",&ch);
				while(ch != ')')
				{
					test[j][k++] = ch;
					fscanf(fp,"%c",&ch);
				}
			}
			else
				test[j][0] = ch;
		}
		count = 0;
		for(k=0;k<d;k++)
		{
			flag = 0;
			for(j=0;j<l;j++)
			{
				p = find(test[j],test[j]+26,in[k][j]);
				if(test[j] + 26 == p)
				{
					flag = 1;
					break;
				}
			}
			if(flag == 0)
				count++;
		}
		fscanf(fp,"\n");
		fprintf(ofp,"Case #%d: %d\n",i+1,count);
	}
	fclose(fp);
	fclose(ofp);
}