#include<stdio.h>
#include<string.h>
struct node{int cho,type;}a[110][11];
int c[110],top;
bool t[11];
unsigned short int re[1200];
int main()
{
    int ii,i,j,n,m,nn,tem,ty,min,sit;
    bool found;
    unsigned short int ui,beg,end;
    scanf("%d",&nn);
    for (ii=1;ii<=nn;ii++) {
        memset(a,0,sizeof(a));
        scanf("%d%d",&n,&m);top=0;
        for (i=1;i<=m;i++) {
            scanf("%d",c+i);
            for (j=1;j<=c[i];j++) {scanf("%d%d",&tem,&ty);a[i][j].cho=tem;a[i][j].type=ty;}
        }
        end=1;
        for (i=1;i<=n;i++) end*=2;
        end--;
        for (ui=0;ui<=end;ui++) {
            for (i=1;i<=m;i++) {
                found=0;
                for (j=1;j<=c[i];j++)
                    if (((ui>>(n-a[i][j].cho))&1)==a[i][j].type) {found=1;break;}
                if (!found) goto next;
            }
            re[++top]=ui;
            next:;
        }
        if (top==0) {printf("Case #%d: IMPOSSIBLE\n",ii);continue;}
        min=n;sit=1;
        for (i=1;i<=top;i++) {
            tem=0;
            for (j=1;j<=n;j++) tem+=((re[i]>>(n-j))&1);
            if (tem<min) {min=tem;sit=i;}
        }
        printf("Case #%d:",ii);
        for (i=1;i<=n;i++) printf(" %d",(re[sit]>>(n-i))&1);
        puts("");
    }

}
