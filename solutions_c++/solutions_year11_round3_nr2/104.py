#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <math.h>
#include <string>
#include <cstring>
#include <queue>
#include <map>
#include <set>
#define u 10000000
using namespace std;

int t,i,L,N,C,l,k,a,ind;
long long To[u],T;

int main()
{
    freopen("b.in","r",stdin);
    freopen("b.out","w",stdout);
    
    scanf("%d",&t);
    for (i = 1; i <= t; i++)
    {
        cin>>L>>T>>N>>C;
        for (l=0; l<C; l++)
        {
            cin>>a;
            k = l;
            while (k<N) { To[k] = a; k+=C; }
        }
        
        long long cur = 0;
        for (l=0; l<N; l++)
        {
            cur+=1LL*2*To[l];
            if (cur>T) { ind = l; break; }
        }       
        
        sort(To+ind+1,To+N);
        reverse(To+ind+1,To+N);
        long long ans1 = 0, ans2 = 0, cur1;
        
        for (l=0; l<=ind; l++)
            ans1 += 1LL*To[l] * 2;
        for (l=ind+1; l<=ind+L; l++) ans1 += 1LL * To[l];
        for (l=ind+L+1; l<N; l++) 
         ans1 += 1LL * To[l] * 2;
         
        cur1 = cur - 2*To[ind];
        for (l=0; l<ind; l++) ans2 += 1LL*To[l] * 2;
        ans2 += 1LL*(T-cur1);
        ans2 += 1LL*(To[ind]-(T-cur1)/2);
        for (l=ind+1; l<ind+L; l++) ans2 += 1LL * To[l];
        for (l=ind+L; l<N; l++) ans2 += 1LL * To[l] * 2;
        
        if (ans2<ans1) ans1 = ans2;
        
        printf("Case #%d: ",i);
        cout<<ans1<<endl;
    }

    return 0;
}
