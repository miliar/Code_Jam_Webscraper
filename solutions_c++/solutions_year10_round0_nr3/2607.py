#include <iostream>

using namespace std;

int main()
{
    FILE *in,*out;
    in=fopen("input.txt","r");
    out=fopen("output.txt","w");
    int i,j=1,r,k,n,a[100000],cost=0,sum,flag,x,t;
    fscanf(in,"%d",&i);
    printf("%d\n",i);
    while(j<=i)
    {
        fscanf(in,"%d%d%d",&r,&k,&n);
        printf("%d\t%d\t%d\n",r,k,n);
        for(t=0;t<n;t++)
            fscanf(in,"%d",&a[t]);
        t=0;
        cost=0;
        for(x=0;x<r;x++)
        {
            sum=a[t];
            t=(t+1)%n;
            for(flag=1;flag<n;flag++)
            {
                if((sum<k)&&(sum+a[t]<=k))
                {
                    sum+=a[t];
                    t=(t+1)%n;
                }
                else
                    break;
            }
            cost+=sum;

        }
        fprintf(out,"Case #%d: %d\n",j,cost);
        j++;
    }
    return 0;
}
