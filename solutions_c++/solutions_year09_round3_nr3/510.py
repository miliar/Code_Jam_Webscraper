#include<stdio.h>
#include<iostream>
#include<algorithm>
#include<string>
#include<math.h>
#include<string.h>

using namespace std;

int T,P,Q,q,i,j,k,a[9],d[999],p;

main()
{
    freopen("c.in","r",stdin);
    freopen("c.out","w",stdout);
    scanf("%d",&T);
    for(q=1;q<=T;q++)
    {
        scanf("%d%d",&P,&Q);
        d[0]=-1; d[P+1]=-1;
        for(i=0;i<Q;i++)
            scanf("%d",&a[i]);
        sort(a,a+Q);
        p=2000000000;
        do
        {
            for(i=1;i<=P;i++)
                d[i]=i;
            k=0;
            for(i=0;i<Q;i++)
            {
                d[a[i]]=-1;
                j=a[i]-1;
                while(d[j]!=-1)
                {
                    j--;
                    k++;
                }
                j=a[i]+1;
                while(d[j]!=-1)
                {
                    j++;
                    k++;
                }
            }
            if(k<p)p=k;
        } while (next_permutation(a,a+Q));
        printf("Case #%d: %d\n",q,p);
    }
}
