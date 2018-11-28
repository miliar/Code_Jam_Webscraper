#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<math.h>
using namespace std ;

int xs[5],ys[5],rs[5];

int main()
{
    FILE *in=fopen("wat.in","r");
    freopen("wat.out","w",stdout);
    int tests;
    fscanf(in,"%d",&tests);
    int c,c2;
    int n;
    int testn=1;
    while(tests)
    {
        printf("Case #%d: ",testn);
        testn++;
        tests--;
        fscanf(in,"%d",&n);
        for (c=0;c<n;c++)
        fscanf(in,"%d %d %d",&xs[c],&ys[c],&rs[c]);
        double ret=1<<30;
        
        if (n==1)printf("%.6lf\n",1.0*rs[0]);
        else if (n==2)printf("%.6lf\n",max(1.0*rs[0],1.0*rs[1]));
        else
        {
            for (c=0;c<n;c++)
            {
                int i,i2,i3;
                i=c;
                i2=(c+1)%3;
                i3=(c+2)%3;
                double len=sqrt((((double)xs[i2]-xs[i])*((double)xs[i2]-xs[i]))+((1.0*ys[i2]-ys[i])*(1.0*ys[i2]-ys[i])));
                len+=rs[i];
                len+=rs[i2];
                len/=2.0;
                ret=min(ret,max(len,1.0*rs[i3]));
            }
            printf("%.6lf\n",ret);
        }
    }
//    system("pause");
    return 0;
}
