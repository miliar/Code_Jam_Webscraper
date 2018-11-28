#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#define NN 2000001
#define KK 8

int table[NN][KK];


void make(int k,int j)
{
	int t = k;
	int i = 0;
	while(1)
	{
		t = (t%10)*j + t/10;
		//printf("k = %d,t = %d,j = %d\n",k,t,j);
		//system("pause");
		if(k == t)
			break;
		if(t>k || t < j)
			continue;
		//printf("%d %d\n",k,t);
		//system("pause");
		table[k][i++] = t;
	}
}

int main()
{
	int i,j,t;
	int a,b;
	int cases = 1;
	int sum = 1;
	freopen("c.in2","r",stdin);
	freopen("c.out","w",stdout);
	memset(table,-1,sizeof(table));
	for(i=1;i<= NN;i++)
	{
		if(i >= sum*10)
		{
			sum*=10;
		}
		make(i,sum);
	}
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d%d",&a,&b);
		sum = 0;
		for(i=a;i<=b;i++)
		{
			for(j=0;table[i][j]!=-1;j++)
			{
				if(table[i][j]>=a)
					sum++;
			}
		}
		printf("Case #%d: %d\n",cases++,sum);
	}
	return 0;


	return 0;
}