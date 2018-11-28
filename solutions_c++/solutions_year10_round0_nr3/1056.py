#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <math.h>
using namespace std;

int peo[1005];
int r,k,n;

int main ()
{
	int i,j;

	freopen("C-small.in","r",stdin);
	freopen("C-small.out","w",stdout);

	int test,sum,t,p,temp,Cnt;

	scanf("%d",&test);
	for(t=1;t<=test;t++)
	{
		sum=0;p=0;
		scanf("%d %d %d",&r,&k,&n);
		for(i=0;i<n;i++)
		{
			scanf("%d",&peo[i]);
		}

		for(i=0;i<r;i++)
		{
			Cnt=0,temp=0;

			while(peo[p]+temp<=k)
			{
				Cnt++;
				temp += peo[p++];
				if(p==n)
				{
					p=0;
				}
				if(Cnt==n)
				{
					break;
				}
			}
			sum += temp;
		}
		printf("Case #%d: %d\n",t,sum);
	}
	return 0;
}