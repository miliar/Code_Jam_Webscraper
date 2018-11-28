#include<stdio.h>
#include<string.h>
#include<algorithm>
using namespace std;
const int N = 1000+10;
int a[N];
int b[N];
int main()
{

	freopen("B-smal.in","r",stdin);
	freopen("B.out","w",stdout);
	int T;
	scanf("%d",&T);
	
	int cases;
	for(cases=1;cases<=T;cases++)
	{
		int ll,tt,nn,cc;
		scanf("%d%d%d%d",&ll,&tt,&nn,&cc);
		int i;
		for(i=0;i<cc;i++)
		{
          scanf("%d",&a[i]);
		 }
		int bid = 0;
		int temp = 0;
		int half = tt/2;
	    for(i=0;i<nn;i++)
	    { 
		   temp=temp+a[i%cc];
		   if(temp>half)
		   {
              b[bid++]=temp-half;
			  break;
		   }
	    }
                         
	     for(i++;i<nn;i++)
		 {
			 temp =temp+a[i%cc];
			 b[bid++]=a[i%cc];
		 }

		 sort(b,b+bid);
		 int ans;
		 if(bid==0)
			 ans = temp*2;
		 else
		 {
			 ans = temp*2;
			 int i = bid-1;
			 
			 while(i>=0&&ll>0)
			 {
				 ans-=b[i];
				 i--;
				 ll--;
			 }
		 }

		 printf("Case #%d: %d\n",cases,ans);
	}
	return 0;
}