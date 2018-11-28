#include<stdio.h>
#include<string.h>
#define inf 100000000
struct node{int z,lc,rc,it;bool can;}a[10010];
int re[10010][2];
void doit(int k)
{
     int tem=inf;
     if (a[k].lc==0)         {re[k][a[k].z]=0;return;}
     doit(k+k);doit(k+k+1);
     if (a[k].can==0) {
         if (a[k].it==1) {
             tem=inf;
             tem<?=re[a[k].lc][0]+re[a[k].rc][1];
             tem<?=re[a[k].lc][1]+re[a[k].rc][0];
             tem<?=re[a[k].lc][0]+re[a[k].rc][0];
             re[k][0]=tem;
             tem=inf;
             tem<?=re[a[k].lc][1]+re[a[k].rc][1];
             re[k][1]=tem;
         }
         else {
             tem=inf;
             tem<?=re[a[k].lc][0]+re[a[k].rc][1];
             tem<?=re[a[k].lc][1]+re[a[k].rc][0];
             tem<?=re[a[k].lc][1]+re[a[k].rc][1];
             re[k][1]=tem;
             tem=inf;
             tem<?=re[a[k].lc][0]+re[a[k].rc][0];
             re[k][0]=tem;             
         }
     }
     else {
         if (a[k].it==1) {
             tem=inf;
             tem<?=re[a[k].lc][1]+re[a[k].rc][1];
             tem<?=re[a[k].lc][1]+re[a[k].rc][0]+1;
             tem<?=re[a[k].lc][0]+re[a[k].rc][1]+1;
             re[k][1]=tem;
             
             tem=inf;
             tem<?=re[a[k].lc][0]+re[a[k].rc][0];
             tem<?=re[a[k].lc][0]+re[a[k].rc][1];
             tem<?=re[a[k].lc][1]+re[a[k].rc][0];
             re[k][0]=tem;
         }
         else {
             tem=inf;
             tem<?=re[a[k].lc][1]+re[a[k].rc][1];
             tem<?=re[a[k].lc][0]+re[a[k].rc][1];
             tem<?=re[a[k].lc][1]+re[a[k].rc][0];
             re[k][1]=tem;
             
             tem=inf;
             tem<?=re[a[k].lc][0]+re[a[k].rc][0];
             tem<?=re[a[k].lc][0]+re[a[k].rc][1]+1;
             tem<?=re[a[k].lc][1]+re[a[k].rc][0]+1;
             re[k][0]=tem;             
         }
     }
             
}
int main()
{
    int i,ii,n,j,nn,m,v,t1,t2;
    scanf("%d",&nn);
    for (ii=1;ii<=nn;ii++) {
        scanf("%d%d",&m,&v);
        memset(a,0,sizeof(a));
        for (i=0;i<10010;i++) re[i][0]=re[i][1]=inf;
        for (i=1;i<=(m-1)/2;i++) {
            scanf("%d%d",&t1,&t2);
            a[i].lc=i+i;
            a[i].rc=i+i+1;
            a[i].it=t1;
            a[i].can=t2;
        }
        for (i=(m-1)/2+1;i<=m;i++){
            scanf("%d",&t1);
            a[i].z=t1;
        }
        doit(1);
        if (re[1][v]>=inf) printf("Case #%d: IMPOSSIBLE\n",ii);
        else printf("Case #%d: %d\n",ii,re[1][v]);
    }
}
