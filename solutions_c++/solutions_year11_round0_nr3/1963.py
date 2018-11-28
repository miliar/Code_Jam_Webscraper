/*  Google Code Jam Qualification Round 2011
    Problem C. Candy Splitting
    Varot Premtoon 7 May 2554 */

#include <cstdio>
#include <cmath>

int sol(int cse)
{
    int n;
    int rt;
    int pck;
    int i,j;
    int can[100];
    int mx = -1;
    int v1,v2,v3;
    int sum = 0;
    scanf("%d",&n);
    for(i=0;i<n;i++) {
        scanf("%d",&can[i]);
        sum += can[i];
    }
    rt = (int)pow(2,n);
    //pck = 6;
    for(pck=0;pck<rt;pck++) {
        v1 = v2 = v3 = 0;
        for(j=pck,i=0;i<n;i++,j>>=1) {
            if(j%2==0) v1 = v1 ^ can[i];
            else {
                v2 = v2 ^ can[i];
                v3 += can[i];
            }
        }
        if(v1==v2&&v3>mx&&v3!=sum) mx = v3;
    }
    if(mx==-1) printf("Case #%d: NO\n",cse);
    else printf("Case #%d: %d\n",cse,mx);
    return 0;
}

int sol2(int cse)
{
    int n;
    int sumo,sum;
    int i,j;
    int mn = 10000000;
    sumo = sum = 0;
    scanf("%d",&n);
    for(i=0;i<n;i++) {
        scanf("%d",&j);
        sum += j;
        sumo = sumo ^ j;
        if(j<mn) mn = j;
    }
    if(sumo!=0) printf("Case #%d: NO\n",cse);
    else printf("Case #%d: %d\n",cse,sum-mn);
}

int main()
{
    int t,i;
    scanf("%d",&t);
    for(i=1;i<=t;i++) sol2(i);
    return 0;
}
