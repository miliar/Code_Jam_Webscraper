#include<stdio.h>
#include<algorithm>
using namespace std;
int a,b,c,d,e,f,g,h,i;
int zz[200];
int main()
{
    //freopen("B-large.in","r",stdin);
    //freopen("bl.out","w",stdout);
    scanf("%d",&a);
    for (b=1;b<=a;b++)
    {
        i=0;
        scanf("%d %d %d",&c,&d,&e);
        for (f=1;f<=c;f++)
            scanf("%d",&zz[f]);
        sort(zz+1,zz+c+1);
        for (f=c;f>0;f--)
        {
            g=zz[f]%3;
            h=zz[f]/3;
            if (g!=0) h++;
            if (h<e && (g==2 || g==0) && d>0 && zz[f]>1 && zz[f]<29){ h++;d--;}
            if (h>=e) i++;
        }
        printf("Case #%d: %d\n",b,i);
    }
}
