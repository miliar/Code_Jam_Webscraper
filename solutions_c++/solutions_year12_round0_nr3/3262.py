#include <iostream.h>
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int n,a,b,cnt=0,wc=0;
    int m=1,mm=1,x=0,r;
    int i,j;
    scanf("%d",&n);
    for(i=0;i<n;i++) {
        cnt=0; wc=0; m=1; mm=1; x=0;
        scanf("%d %d",&a,&b);
        while(mm<=a) {
            mm*=10;
        }
        mm/=10;
        while(m<a) {
            m*=10;
            x++;
            for(j=a;j<=b;j++) {
                int tmp=j;
                r=tmp%m; tmp/=m; tmp+=r*mm;
                if(tmp>=a && tmp<=b && tmp!=j) {
                    cnt++;
                    if(mm==1000) {
                        int test=j%100;
                        if(test*100+test==j) {
                            wc+=2;
                        }
                    }
                    if(mm==100000) {
                        int test=j%100;
                        if(test*10000+test*100+test==j) {
                            wc+=3;
                        }
                        test=j%1000;
                        if(test*1000+test==j) {
                            wc+=4;
                        }
                    }
                }
            }
            mm/=10;
        }
        printf("Case #%d: %d\n",i+1,cnt/2-wc/4);
        cnt=0;
    }
    //system("PAUSE");
    return 0;
}
