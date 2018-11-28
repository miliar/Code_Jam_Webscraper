#include<stdio.h>
#include<iostream>
using namespace std;

int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int i,n,k,cases,j,flag,p,ab;
	int in[31];
	scanf("%d",&cases);
	for(ab=0;ab<cases;ab++)
	{
		scanf("%d %d",&n,&k);
		for(i=0;i<n;i++)
		{
			in[i] = 0;
		}
		if(k>0)
			in[0]=1;
		
		for(i=1;i<k;i++)
		{
			
			for(j=0;j<n;j++)
			{
				if(in[j] == 0)
				{
					break;
				}
			}
			for(p=0;p<=j;p++)
			{
				//toggle(a[p]);
				if(in[p] == 0)
					in[p] = 1;
				else
					in[p] = 0;
			}
		}
		for(i=0;i<n;i++)
		{
			flag = 1;
			if(in[i] == 0)
			{
				flag = 0;
				break;
			}
		}
		printf("Case #%d: ",ab+1);
		if(flag)
			printf("ON\n");
		else
			printf("OFF\n");
	}
	return 0;
}

			
