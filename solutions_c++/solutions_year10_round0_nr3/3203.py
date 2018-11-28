#include <stdio.h>
#include <iostream>
#define u 5000
using namespace std;

long t, R,K, k, n, l, fin[u], ans[u], m[u], sum, cur;


int main()
{
    freopen("c-small.in","r",stdin);
    freopen("c-small.out","w",stdout);
    
    scanf("%d",&t);
    for (long test = 1; test<=t; test++)
    {

        printf("Case #%d: ",test);
        scanf("%d%d%d",&R,&K,&n);
        for (sum=l=0; l<n; l++){ scanf("%d",&m[l]); sum += m[l]; }
        
        for (l=0; l<n; l++)
        {   
            ans[l] = 0;
            if (K>=sum) { ans[l] = sum; fin[l] = l; continue; }
            k = l;
            while (ans[l]+m[k]<=K)
            {
                  ans[l]+=m[k++];                  
                  if (k==n) k = 0;
            }
            fin[l] = k;
        }
        
        long long answer = 0;
        for (cur=l=0; l<R; l++)
        {
          answer+=1LL*ans[cur];
          cur = fin[cur];
        }
        cout<<answer<<endl;
    }


    return 0;
}
