#include<stdio.h>
#define abs(x) (x>0?x:-(x))
int main()
{
    int ii,nn,x1,x2,y1,y2,n,m,a;
    scanf("%d",&nn);
    for (ii=1;ii<=nn;ii++) {
        scanf("%d%d%d",&n,&m,&a);
        for (x1=0;x1<=n;x1++) 
            for (x2=0;x2<=n;x2++)
                for (y1=0;y1<=m;y1++) 
                    for (y2=0;y2<=m;y2++) {
                        if (abs(x1*y2-x2*y1)==a) goto found;
                    }
        printf("Case #%d: IMPOSSIBLE\n",ii); continue;
        found:printf("Case #%d: 0 0 %d %d %d %d\n",ii,x1,y1,x2,y2);
    }
}
