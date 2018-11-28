#include<iostream>
using namespace std;
int main()
{
 	int tt;
 	int i,j;
 	int sum;
 	int minn;
 	int res;
 	int n,a;
 	freopen("C-large.in","r",stdin);
 	freopen("out.txt","w",stdout);
 	scanf("%d",&tt);
 	for(i=1;i<=tt;i++)
 	{
        res=0;
        scanf("%d",&n);
        minn=999999999;
        sum=0;
        for(j=0;j<n;j++)
        {
		    scanf("%d",&a);
		    res^=a;
		    sum+=a;
		    minn=minn<a?minn:a;
	    }
	    if(res==0)
	    {
 		  printf("Case #%d: %d\n",i,sum-minn);
 		  continue;
        }
        else
        {
		 	printf("Case #%d: NO\n",i);
 	    }
	    
        
    }
 	return 0;
}
