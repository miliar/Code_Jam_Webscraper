#include<iostream>
int no[10],size;
using namespace std;
void split(int x)
{
	int i=0,temp=1;
    size=0;
	while(x/temp!=0)
	{
		temp*=10;
		size++;
	}
	while(temp>1)
	{
		temp/=10;
        no[i++]=x/temp;
		x-=no[i-1]*temp;
	}
}
int main()
{
	int i,t,a,b,m,k,l,n,ans,cnt;
	scanf("%d",&t);
	for(i=1;i<=t;i++)
	{
		ans=0;
		scanf("%d%d",&a,&b);
		for(m=a;m<b;m++)
		{
			split(m);
			for(k=1;k<size;k++)
			{
				n=0;
				l=k;
				for(cnt=0;cnt<size;cnt++)
				{
					if(l<size-1)
					{
						n=n*10+no[l++];
					}
					else
					if(l==size-1)
					{
						n=n*10+no[l];
						l=0;	
					}
				}
				if(n>m&&n<=b)
					{
                       ans++;
                       }
			}
		}
		printf("Case #%d: %d\n",i,ans);
	}
}
