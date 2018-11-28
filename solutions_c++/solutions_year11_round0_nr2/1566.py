// poj.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <stdio.h>

int main()
{
	int t,c,d,n;
	int i,j,k,l;
	char com[36][4];
	char opp[28][3];
	char a[101];
	int cur,len;
	bool flag;

//	freopen("B-small-attempt1.in.txt","r",stdin);
//	freopen("B-small.out1.txt","w",stdout);
	scanf("%d",&t);
	for(i=0;i<t;i++)
	{
		scanf("%d",&c);
		for(j=0;j<c;j++)
			scanf("%s",com[j]);
		scanf("%d",&d);
		for(j=0;j<d;j++)
			scanf("%s",opp[j]);
		scanf("%d%s",&n,a);
		len=n;
		cur=1;
		while(cur<len)
		{
			flag=false;
			
			for(j=0;j<c;j++)
			{
				if((a[cur-1]==com[j][0]&&a[cur]==com[j][1])||(a[cur]==com[j][0]&&a[cur-1]==com[j][1]))
				{
					a[cur-1]=com[j][2];
					for(k=cur+1;k<=len;k++)
					{
						a[k-1]=a[k];
					}
					len--;
					flag=true;
					break;
				}
			}
			for(k=cur-1;k>=0;k--)
			{
				for(j=0;j<d;j++)
				{
					if((a[k]==opp[j][0]&&a[cur]==opp[j][1])||(a[k]==opp[j][1]&&a[cur]==opp[j][0]))
					{
						for(l=cur+1;l<=len;l++)
						{
							a[l-cur-1]=a[l];
						}
						len=len-cur-1;
						cur=1;
						flag=true;
						break;
					}
				}
				if(flag)
					break;
			}
			if(flag)
				continue;
			else
				cur++;
		}
		printf("Case #%d: [",i+1);
		for(j=0;j<len;j++)
		{
			printf("%c",a[j]);
			if(j<len-1)
				printf(", ");
		}
		printf("]\n");
	}
	
	return 0;
}

