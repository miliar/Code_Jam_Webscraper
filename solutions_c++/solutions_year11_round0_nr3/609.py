#include <iostream>
#include <fstream>
#include <stdio.h>
#include <string.h>
#include <algorithm>
#define MAXN 1000
#define MAX 10000000

using namespace std;

int T,N;
int c[MAXN+10];

int main()
{
//    freopen("in.txt","r",stdin);
//    freopen("out.txt","w",stdout);
    cin>>T;
    int ans;
    int S,m;
    for(int t=1;t<=T;t++)
    {
        m=MAX;
        S=0;
        ans=0;
        scanf("%d",&N);
        for(int i=0;i<N;i++)
        {
            scanf("%d",&c[i]);
            ans^=c[i];
            m=min(m,c[i]);
            S+=c[i];
        }
        if(ans) printf("Case #%d: NO\n",t);
        else
        {
            printf("Case #%d: %d\n",t,S-m);
        }

    }
    return 0;
}
