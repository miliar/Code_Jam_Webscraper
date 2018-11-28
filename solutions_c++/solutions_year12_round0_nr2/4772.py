#include<iostream>
#include<cstdio>
using namespace std;
int a[]={0,1,4,7,10,13,16,19,22,25,28};
int b[]={0,1,2,5,8,11,14,17,20,23,26};
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("oular.txt","w",stdout);
	int test,i,j,count,n,s,p,t;
	i=1;
	scanf("%d",&test);
	while(i<=test)
	{
		count=0;
		scanf("%d %d %d",&n,&s,&p);
		for(j=0;j<n;j++)
		{
			scanf("%d",&t);
			if(t>=a[p])
			{
				count++;

			}
			else if(p>1)
			{
				if(s>0 && t>=b[p])
				{
				 count++;
				 s--;
				}
			}
		}
		 
		printf("Case #%d: %d\n",i,count);
		i++;
	}
	return 0;
}
