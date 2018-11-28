#include<stdio.h>
#include<algorithm>
using namespace std;
long long a,b,c,d,e,f,g,h,i,j,k;
long long tabel[1000005];
int main()
{
    freopen("space.in","r",stdin);
    freopen("space2.out","w",stdout);
    scanf("%lld",&a);
    for (b=1;b<=a;b++)
    {
        scanf("%lld%lld%lld%lld",&c,&d,&e,&f);
        for (g=1;g<=f;g++)
            scanf("%lld",&tabel[g]);
        tabel[0]=tabel[f];
        for (g=f+1;g<=e;g++)
        {
            tabel[g]=tabel[g%f];
            //printf("%lld %lld\n",tabel[g],g);
        }
        h=0; i=1;
        while(h<d && i<=e)
        {
            h+=tabel[i]*2;
            i++;   
        }
        if (h==d)
        {
            sort(tabel+i,tabel+e+1);
            for (j=e;j>=i;j--)
            {
                if (c>0)
                {
                   h+=tabel[j];
                   c--;
                }
                else
                    h+=tabel[j]*2;
            }
            printf("Case #%lld: %lld\n",b,h);
        }
        else
        {
            if (h>d)
            {
                tabel[e+1]=(h-d)/2;
                h=d; //printf("%lld %lld\n",h,tabel[e+1]);
                sort(tabel+i,tabel+e+2);
                for (j=e+1;j>=i;j--)
                {
                    if (c>0)
                    {
                       h+=tabel[j];
                       c--;        
                    }   
                    else
                        h+=tabel[j]*2;
                }
                printf("Case #%lld: %lld\n",b,h);
            }
            else
            {
                printf("Case #%lld: %lld\n",b,h);    
            }
        }
    }
}
