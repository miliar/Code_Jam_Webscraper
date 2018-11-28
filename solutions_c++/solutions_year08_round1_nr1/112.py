#include <stdio.h>
#include <algorithm>
using namespace std;


__int64 a[1000];
__int64 b[1000];

int main()
{
	freopen("A-large.in.txt","r",stdin);
    freopen("A-large.out.txt","w",stdout);
 //  freopen("A-small-attempt0.in.txt","r",stdin);
 //   freopen("A-small-attempt0.out.txt","w",stdout);
    int n,t,p,i,j;
     __int64 result;
	scanf("%d",&t);
	for(p=0;p<t;p++)
	{
        scanf("%d",&n);
		for(i=0;i<n;i++)
	      scanf("%I64d",&a[i]);
		for(i=0;i<n;i++)
	      scanf("%I64d",&b[i]);
 
		sort(a,a+n);
		sort(b,b+n);
        result=0;
		for(i=0;i<n;i++)
			result+=a[i]*b[n-1-i];
        
		printf("Case #%d: %I64d\n",p+1,result);
	}

}