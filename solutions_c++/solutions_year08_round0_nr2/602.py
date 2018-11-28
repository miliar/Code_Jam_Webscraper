#include<stdio.h>
#include<algorithm>
struct node{int beg,end;bool mark;}za[210],zb[210];
int op(struct node x,struct node y){return x.beg<y.beg||x.beg==y.beg&&x.end<y.end;}
int main()
{
    int i,j,k,nn,ii,na,nb,t,ho,mi,ans,n,p1,ans1,ans2;
//    freopen("c:\\B-large.in","r",stdin);
//    freopen("c:\\output.txt","w",stdout);
    scanf("%d",&nn);
    for (ii=1;ii<=nn;ii++) {
        scanf("%d%d%d",&t,&na,&nb);
        for (i=1;i<=na;i++) {
            scanf("%d:%d",&ho,&mi);
            za[i].beg=ho*60+mi;
            scanf("%d:%d",&ho,&mi);
            za[i].end=ho*60+mi+t;
            za[i].mark=1;
        }
        for (i=1;i<=nb;i++) {
            scanf("%d:%d",&ho,&mi);
            zb[i].beg=ho*60+mi;
            scanf("%d:%d",&ho,&mi);
            zb[i].end=ho*60+mi+t;
            zb[i].mark=1;
        }
        std::sort(za+1,za+na+1,op);
        std::sort(zb+1,zb+nb+1,op);
        n=na+nb;
        for (i=j=k=1;k<=n;k++) {
            if (i<=na&&op(za[i],zb[j])||j>nb) {
                for (p1=j;p1<=nb;p1++) if (zb[p1].mark&&za[i].end<=zb[p1].beg) {
                    zb[p1].mark=0;break;}
                i++;
            }
            else {
                for (p1=i;p1<=na;p1++) if (za[p1].mark&&zb[j].end<=za[p1].beg) {
                    za[p1].mark=0;break;}
                j++;
            }
        }
        for (ans1=0,i=1;i<=na;i++) ans1+=za[i].mark;
        for (ans2=0,i=1;i<=nb;i++) ans2+=zb[i].mark;
        printf("Case #%d: %d %d\n",ii,ans1,ans2);
    }
}
