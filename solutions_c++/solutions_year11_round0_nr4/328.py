#include <iostream>
#include <cmath>
#include <map>
using namespace std;
int dp[2][1024000];
int main()
{
   // printf("%d\n",1<<1);
 freopen("d2.txt","r",stdin);
   freopen("d2out.txt","w",stdout);
    int T;
    scanf("%d",&T);
    for(int t=1;t<=T;t++)
    {
        int n;
        int num[1024];
        scanf("%d",&n);
        int res=0;
        for(int i=1;i<=n;i++)
        {
            scanf("%d",&num[i]);
            if(num[i]!=i)
            {
                res++;
            }
        }
        printf("Case #%d: %d.000000\n",t,res);
    }
	return 0;
}
