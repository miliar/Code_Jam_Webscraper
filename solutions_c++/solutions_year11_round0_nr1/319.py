#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#define MAXN 100
using namespace std;

char lr[MAXN+1];
int po[MAXN+1],pb[MAXN+1];
int n;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int i,p,c,t,no,nb,io,ib,co,cb,st;
    scanf("%d",&t);
    for(c=0;c<t;c++)
    {
        scanf("%d",&n);
        no=nb=0;
        for(i=0;i<n;i++)
        {
            scanf(" %c %d",&lr[i],&p);
            if(lr[i]=='O')
            {
                po[no++]=p;
            }
            else
            {
                pb[nb++]=p;
            }
        }
        io=ib=0;
        co=cb=1;
        st=0;
        for(i=0;i<n;i++)
        {
            if(lr[i]=='O')
            {
                if(ib<nb)
                {
                    if(labs(cb-pb[ib])<=labs(co-po[io]))
                    {
                        cb=pb[ib];
                    }
                    else
                    {
                        cb=cb-(labs(co-po[io])+1)*((cb-pb[ib])/labs(cb-pb[ib]));
                    }
                }
                st=st+labs(co-po[io])+1;
                co=po[io++];
            }
            else
            {
                if(io<no)
                {
                    if(labs(co-po[io])<=labs(cb-pb[ib]))
                    {
                        co=po[io];
                    }
                    else
                    {
                        co=co-(labs(cb-pb[ib])+1)*((co-po[io])/labs(co-po[io]));
                    }
                }
                st=st+labs(cb-pb[ib])+1;
                cb=pb[ib++];
            }
        }
        printf("Case #%d: %d\n",c+1,st);
    }
    return 0;
}
