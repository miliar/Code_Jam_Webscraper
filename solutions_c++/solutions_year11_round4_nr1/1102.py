#include<iostream>
#include<stdio.h>
#include<map>
#include<stdlib.h>
#include<algorithm>
#include<vector>
#include<string>
#include<math.h>
using namespace std;
struct f
{
    int len,w;
}node[1010];
int cmp(const void *a,const void *b)
{
    return (*(struct f*)a).w-(*(struct f*)b).w;
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("outA1.txt","w",stdout);
    int case1,k,i,j,X,S,R,m,n,b,e,a;
    double ans,tmp,t;
    
    scanf("%d",&case1);
    for(a=1;a<=case1;a++) {
        scanf("%d%d%d%d%d",&X,&S,&R,&m,&n);
        t=m;
        node[0].len=X;
        node[0].w=S;
        for(i=1;i<=n;i++) {
            scanf("%d%d%d",&b,&e,&node[i].w);
            node[i].w+=S;
            node[i].len=e-b;
            node[0].len-=node[i].len;
        }
        printf("Case #%d: ",a);
        qsort(node,n+1,sizeof(node[0]),cmp);
        ans=0; 
        if((double)node[0].len/R>=t) {
            ans=t+((double)node[0].len-t*R)/(double)S;
            for(i=1;i<=n;i++) ans+=(double)node[i].len/(double)node[i].w;
            printf("%.12lf\n",ans);
            continue;
        }
        ans=(double)node[0].len/R;
        t-=ans;
        for(i=1;i<=n;i++) {
            if((double)node[i].len/(node[i].w+R-S)>=t) {
                ans=ans+t+((double)node[i].len-t*(node[i].w+R-S))/(double)node[i].w;
                for(j=i+1;j<=n;j++) ans+=(double)node[j].len/(double)node[j].w;
                break;
            }
            else {
                tmp=(double)node[i].len/(double)(node[i].w+R-S);
                t-=tmp;
                ans+=tmp;
            }
        }
        printf("%.12lf\n",ans);
        
    }
    //system("pause");
    return 0;
}
