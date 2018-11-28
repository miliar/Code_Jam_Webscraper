#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <math.h>

using namespace std;

double p[1000000],d;
int n,c;

int main()
{
    int i,j,k,t,T,q,flag;
    double w,need;
    long long int lo,mid,hi;

    freopen("bla.in","r",stdin);
    freopen("bout.txt","w",stdout);


    scanf("%d",&T);

    for(t=1;t<=T;t++)
    {
        scanf("%d %d",&c,&k);

        d=(double)k;

        n=0;

        for(i=0;i<c;i++)
        {
            scanf("%d %d",&j,&k);

            for(q=0;q<k;q++)
            {
                p[n++]=(double)j;
            }
        }

        lo=0;
        hi=1000000000000000000LL;

       while(lo!=hi)
       {
           mid=(lo+hi)/2;

           w=mid/2.0;

            need=p[0]-w+d;

            for(i=1;i<n;i++)
            {
                flag=1;

                if(p[i]>=need)
                {
                    if((p[i]-w)<=need)
                    {
                        need=need+d;
                    }

                    else need=p[i]-w+d;
                }

                else
                {
                    if(p[i]+w>=need)
                    {
                        need=need+d;
                    }

                    else
                    {
                        flag=0;
                        break;
                    }
                }
            }

            if(flag) hi=mid;

            else lo=mid+1;
        }

        printf("Case #%d: %.1lf\n",t,lo/2.0);
    }

    return 0;
}






