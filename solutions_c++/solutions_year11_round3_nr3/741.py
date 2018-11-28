#include<iostream>
using namespace std;
int num[105];
int gcd(int a,int b)
{
 	return (b==0)?a:gcd(b,a%b);
}
int main()
{
 	int t;
 	freopen("C-small-attempt0.in","r",stdin);
    freopen("out1.txt","w",stdout);
 	scanf("%d",&t);
 	int cas;
 	int ll,rr;
 	int n;
 	int i,j;
 	for(cas=1;cas<=t;cas++)
 	{
        scanf("%d%d%d",&n,&ll,&rr);
        for(i=0;i<n;i++)
        {
		    scanf("%d",&num[i]);
		}
		bool flag=0;
		for(i=ll;i<=rr;i++)
		{
            for(j=0;j<n;j++)
            {
		         if((i%num[j]==0)||(num[j]%i==0)) continue;
		         else
		             break;
		    }
		    if(j==n)
		        break;
        }
        if(i==rr+1)
            printf("Case #%d: NO\n",cas);
        else
            printf("Case #%d: %d\n",cas,i);
    }
 	return 0;
}
