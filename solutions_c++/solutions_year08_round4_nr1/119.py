#include<stdio.h>
#include<string.h>

const int maxn=128*128*2;
struct node{
    int g,c;
    int cot[2];
    int type;
    int v;
    void init(){
        cot[0]=cot[1]=-1;
        v=-1;
    };
}a[maxn];
int M,V;

void input()
{
    int i;
    scanf("%d%d",&M,&V);
    for(i=1;i<=M;i++) a[i].init();
    for(i=1;i<=(M-1)/2;i++){
        a[i].type=0;
        scanf("%d%d",&a[i].g,&a[i].c);
    }
    for(;i<=M;i++){
        a[i].type=1;
        scanf("%d",&a[i].v);
        a[i].cot[a[i].v]=0;
    }
}

int getmin(int a,int b)
{
    if(a<0) return b;
    if(b<0) return a;
    return a<b?a:b;
}

int solve()
{
    int i,d1,d2,t;
    for(i=(M-1)/2;i>=0;i--){
        //0
        if(a[i].g==1){
            for(d1=0;d1<2;d1++) for(d2=0;d2<2;d2++){
                if(d1==1 && d2==1) continue;
                if(a[i+i].cot[d1]>=0 && a[i+i+1].cot[d2]>=0){
                    t=a[i+i].cot[d1]+a[i+i+1].cot[d2];
                    a[i].cot[0]=getmin(a[i].cot[0],t);
                }
            }
            if(a[i].c==1){
                d1=d2=0;
                if(a[i+i].cot[d1]>=0 && a[i+i+1].cot[d2]>=0){
                    t=a[i+i].cot[d1]+a[i+i+1].cot[d2]+1;
                    a[i].cot[0]=getmin(a[i].cot[0],t);
                }
            }
        }else{
            d1=d2=0;
            if(a[i+i].cot[d1]>=0 && a[i+i+1].cot[d2]>=0){
                t=a[i+i].cot[d1]+a[i+i+1].cot[d2];
                a[i].cot[0]=getmin(a[i].cot[0],t);
            }
            if(a[i].c==1){
                for(d1=0;d1<2;d1++) for(d2=0;d2<2;d2++){
                    if(d1==1 && d2==1) continue;
                    if(a[i+i].cot[d1]>=0 && a[i+i+1].cot[d2]>=0){
                        t=a[i+i].cot[d1]+a[i+i+1].cot[d2]+1;
                        a[i].cot[0]=getmin(a[i].cot[0],t);
                    }
                }
            }
        }
        //1
        if(a[i].g==0){
            for(d1=0;d1<2;d1++) for(d2=0;d2<2;d2++){
                if(d1==0 && d2==0) continue;
                if(a[i+i].cot[d1]>=0 && a[i+i+1].cot[d2]>=0){
                    t=a[i+i].cot[d1]+a[i+i+1].cot[d2];
                    a[i].cot[1]=getmin(a[i].cot[1],t);
                }
            }
            if(a[i].c==1){
                d1=d2=1;
                if(a[i+i].cot[d1]>=0 && a[i+i+1].cot[d2]>=0){
                    t=a[i+i].cot[d1]+a[i+i+1].cot[d2]+1;
                    a[i].cot[1]=getmin(a[i].cot[1],t);
                }
            }
        }else{
            d1=d2=1;
            if(a[i+i].cot[d1]>=0 && a[i+i+1].cot[d2]>=0){
                t=a[i+i].cot[d1]+a[i+i+1].cot[d2];
                a[i].cot[1]=getmin(a[i].cot[1],t);
            }
            if(a[i].c==1){
                for(d1=0;d1<2;d1++) for(d2=0;d2<2;d2++){
                    if(d1==0 && d2==0) continue;
                    if(a[i+i].cot[d1]>=0 && a[i+i+1].cot[d2]>=0){
                        t=a[i+i].cot[d1]+a[i+i+1].cot[d2]+1;
                        a[i].cot[1]=getmin(a[i].cot[1],t);
                    }
                }
            }
        }
    }
    return a[1].cot[V];
}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int T,i,ans;
    scanf("%d",&T);
    for(i=1;i<=T;i++){
        input();
        printf("Case #%d: ",i);
        ans=solve();
        if(ans<0) printf("IMPOSSIBLE\n");
        else printf("%d\n",ans);
    }
    return 0;
}
