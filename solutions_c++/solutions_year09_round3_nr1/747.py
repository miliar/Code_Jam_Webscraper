// Round 1C1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include<string.h>
using namespace std;

class chars
{
public:
	int val,inp;
};

int main()
{
	int i,j,k,t,count,flag,len,l;
	unsigned long long num;
	char inp[61];
	chars arr[61];
	FILE *fp,*ofp;
	fopen_s(&fp,"A-large.in","r");
	fopen_s(&ofp,"Output.txt","w");
	fscanf(fp,"%d\n",&t);
	for(i=0;i<t;i++)
	{
		fscanf(fp,"%s\n",inp);
		len = strlen(inp);
		arr[0].val = 1;
		arr[0].inp = inp[0];
		for(l=1;l<len;l++)
		{
			arr[l].inp = inp[l];
			if(inp[l-1]!=inp[l])
			{
				arr[l].val = 0;
				break;
			}
			else
				arr[l].val = 1;
		}
		count = 2;
		for(j=l+1;j<len;j++)
		{
			flag = 0;
			arr[j].inp = inp[j];
			for(k=0;k<j;k++)
			{
				if(arr[k].inp == arr[j].inp)
				{
					flag = 1;
					arr[j].val = arr[k].val;
					break;
				}
			}
			if(flag == 0)
			{
				arr[j].val = count;
				count++;
			}
		}
		num = 0;
		for(j=0;j<len;j++)
			num = num * count + arr[j].val;
		fprintf(ofp,"Case #%d: %llu\n",i+1,num);
	}
	fclose(fp);
	fclose(ofp);
}

