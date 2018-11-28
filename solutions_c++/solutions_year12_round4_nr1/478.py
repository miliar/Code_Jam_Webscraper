#include <iostream>
#include <stdio.h>
#include <math.h>
#include <string.h>
#include <stdlib.h>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <utility>
#define pi (2*acos(0))
#define ll long long int
#define pii pair<int,int>
#define M 10005

using namespace std;

int d[M],l[M],n,mx[M];

int main()
{
    int i,j,k,t,T,r,D;

    freopen("A-large(1).in","r",stdin);
    freopen("aout.txt","w",stdout);

    scanf("%d",&T);

    for(t=1;t<=T;t++)
    {
        scanf("%d",&n);
        r=0;
        for(i=1;i<=n;i++)
        {
            mx[i]=0;
            scanf("%d %d",&d[i],&l[i]);
        }

        scanf("%d",&D);

        memset(mx,-1,sizeof(mx));

        mx[1]=d[1];

        for(i=1;i<=n;i++)
        {
            if(mx[i]==-1) continue;

            for(j=i+1; j<=n; j++)
            {
                if(d[i]+mx[i]<d[j]) break;

                if(d[j]-l[j]>d[i])
                {
                    mx[j]=l[j];
                }

                else    mx[j]=max(mx[j],d[j]-d[i]);

                if (d[j]+mx[j]>=D)
                {
                    r=1;
                    break;
                }
            }

            if(d[i]+mx[i]>=D)
            {
                r=1;
                break;
            }

            if(r) break;
        }


        printf("Case #%d: %s\n",t,(r) ? "YES" : "NO");
    }

    return 0;
}


