#include<stdio.h>
using namespace std;
int a,b,c,d,e,f,g,h,i,j,k;
int zz[10],zz2[10];
bool bole;
int main()
{
    //freopen("C-large.in","r",stdin);
    //freopen("cl.out","w",stdout);
    scanf("%d",&a);
    for (b=1;b<=a;b++)
    {
        j=0;
        scanf("%d %d",&c,&d);
        for (e=c;e<=d;e++)
        {
            f=e;
            g=0;
            while(f>0)
            {
                zz[g]=f%10;
                f/=10;
                g++;
            }
            f=e;
            i=1;
            k=0;
            for (h=1;h<g;h++) i*=10;
            for (h=0;h<g;h++)
            {
                f/=10;
                f+=zz[h]*i;
                bole=1;
                if (e<f && f<=d && zz[h]!=0)
                {
                   for (int l=0;l<k;l++)
                       if (f==zz2[l]) 
                          bole=0;
                   if (bole)
                      j++;
                   zz2[k]=f;
                   k++;   
                }
            }
        }
        printf("Case #%d: %d\n",b,j);
    }
}
