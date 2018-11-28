#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <cmath>
#include <vector>
using namespace std;
int c[10];
int sum[10];
int main()
{
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
    int t,a,b;
	int tca=1;
	scanf("%d",&t);
	while(t--)
	{
       scanf("%d %d",&a,&b);

	   int ans=0;
	   for(int i=a;i<=b;i++)
	   {
          int temp=i;
		  int num=0;
		  while(temp>0)
		  {
              c[num++]=temp%10;
			  temp/=10;
		  }
          for(int j=0;j<num;j++)
		  {
			  if(c[j]==0)
			  {
				  sum[j]=-1;
				  continue;
			  }
			  sum[j]=0;
			  int tnum=0;
		      for(int k=j;tnum<num;k--,tnum+=1)
			  {
                 if(k==-1)
					 k=num-1;
				 sum[j]=sum[j]*10+c[k];
			  }
			/*  if(sum!=i && sum>=a && sum<=b )
				  ans+=1;*/
		  }
		  sort(sum,sum+num);
          for(int j=0;j<num;j++)
		  {
		     if(sum[j]==-1)
				 continue;
			 if(j>=1 && sum[j]==sum[j-1])
				 continue;
			 if(sum[j]!=i && sum[j]>=a && sum[j]<=b)
                 ans+=1;
		  }
	   }
	   printf("Case #%d: %d\n",tca++,ans/2);
	}
	return 0;
}