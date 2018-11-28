#include<iostream>
using namespace std;
int main()
{
 	int tt;
 	int i,j;
 	int a,n;
 	int ans;
 	
 	freopen("D-large.in","r",stdin);
 	freopen("out.txt","w",stdout);scanf("%d",&tt);
 	for(i=1;i<=tt;i++)
 	{
        ans=0;
	    scanf("%d",&n);
		for(j=1;j<=n;j++)
		{
	        scanf("%d",&a);
	        if(a!=j)
	            ans++;
	    }
		printf("Case #%d: %d.000000\n",i,ans);				  
    }
    return 0;
}
