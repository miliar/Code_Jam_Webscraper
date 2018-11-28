#include<stdio.h>
#include<math.h>
#include<iostream.h>
int main()
{
    unsigned int n,k,i,j,tst,y;
    freopen("A-large.in","rt",stdin);
    freopen("A.txt","w",stdout);
    scanf("%d",&tst);
    for(unsigned int x=1;x<=tst;x++)
    {
        scanf("%u%u",&n,&k);

        y=1;
        for(i=1;i<=n;i++)
        {
            //cout<<(k&1)<<endl;
            if((k&1)==0) y=0;
            k=k>>1;
        }
        if(y) printf("Case #%u: ON\n",x);
        else printf("Case #%u: OFF\n",x);



        /*if(j>k)
        {
            printf("Case #%d: OFF\n",x);
        }
        else
        {
            i=k-j;

            if(i==0) printf("Case #%d: ON\n",x);

            else {

                y=ceil(log10(i)/log10(2));
                if((int)pow(2,y)==i) printf("Case #%d: ON\n",x);
                else printf("Case #%d: OFF\n",x);

            }
        }*/


    }
    return 0;
}
