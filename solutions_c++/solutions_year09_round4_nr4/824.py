#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<time.h>
#include<ctype.h>
#include<iostream>
#include<vector>
#include<string>
#include<set>
#include<map>
#include<stack>
#include<queue>
#include<algorithm>

using namespace std;

int x[42], y[42], r[42];

double dist(int i, int j)
{
    return ((sqrt((x[i]-x[j])*(x[i]-x[j])+(y[i]-y[j])*(y[i]-y[j])))+(double)r[i]+(double)r[j])/2.0;
}

int main()
{
    freopen("D_small.in","r",stdin);
    freopen("D_small.out","w",stdout);
    
    int T;
    scanf("%d",&T);
    
    for(int t = 1; t <= T; ++t)
    {
        int n;
        scanf("%d",&n);
        for(int i = 0; i < n; ++i)
        {
            scanf("%d%d%d",x+i,y+i,r+i);   
        }   
        
        printf("Case #%d: ",t);
        
        if(n==1)
        {
            printf("%lf\n",(double)r[0]);   
        }
        else if(n==2)
        {
            printf("%lf\n",(double)max(r[0],r[1]));   
        }
        else
        {
            double ans = max( dist(0,1), (double)r[2] );
            
            ans = min(ans, max( dist(1,2), (double)r[0] ));
            
            ans = min(ans, max( dist(0,2), (double)r[1] ));
            
            printf("%lf\n",ans);
        }
    }
    return 0;
}
