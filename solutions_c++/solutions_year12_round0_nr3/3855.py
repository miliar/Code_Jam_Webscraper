#include<iostream>
#include<algorithm>
using namespace std;
#include<string.h>
#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#define max 2000000000
#define eps 1e-7
#define pi acos(-1.0)
int ten[9]={1,10,100,1000,10000,100000,1000000,10000000,100000000};
int a[2000000];
int getweishu(int n)
{
	int s=0;
	while(n)
	{
		s++;
		n/=10;
	}
	return s;
}
 
int main()
{
	int A,B;
	int n,i,ans,x;
	int t,c=0,k=0;
	freopen("C-large.in","r",stdin);
	freopen("out.out","w",stdout);
	scanf("%d",&t);
	while(t--)
	{
		k++;
		scanf("%d%d",&A,&B);
		memset(a,0,sizeof(a));
		ans=0;
		for(n=A;n<=B;n++)
		{
			c=0;
			if(!a[n])
			{	
				x = getweishu(n);
				for(i=0;;i++)
				{
					int q = n/ten[i];
					int h = n%ten[i];
					if(q==0) break;
					if(i>0 && h/ten[i-1]==0) continue;
					int d = h*ten[x-i]+q;
					if(d>=A && d<=B && a[d]==0){
						//cout<<d<<" ";
						a[d]=1;
						c++;
					}
				}
			}
			ans+=c*(c-1)/2;
			//puts("");
		}
		printf("Case #%d: %d\n",k,ans);
	}
	return 0;
}
