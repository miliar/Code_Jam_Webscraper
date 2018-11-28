#include<stdio.h>
int main()
{
    freopen("c:\\A-small-attempt0.in","r",stdin);
    freopen("c:\\A-small-attempt0.out","w",stdout);
    int nn;
    scanf("%d",&nn);
    int n,k;
    for (int ii=1;ii<=nn;ii++) {
        scanf("%d%d",&n,&k);
        bool fal=0;
        printf("Case #%d: ",ii);
        for (int i=0;i<n;i++) if (!(k&(1<<i))) fal=1;
        if (fal) puts("OFF");
        else puts("ON");
    }
            
}
