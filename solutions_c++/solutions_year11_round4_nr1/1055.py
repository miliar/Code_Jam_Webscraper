#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<algorithm>
using namespace std;
double x,s,r,t;
int N;
struct In{
    double b,e,w,c;
}p[1500];
bool cmp1(In A,In B){
    return A.b<B.b;
}
bool cmp(In A,In B){
    return A.c>B.c;
}
int main(){
    int T;
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    scanf("%d",&T);
    for(int ca=1;ca<=T;ca++){
        double ans=0;
        scanf("%lf%lf%lf%lf%d",&x,&s,&r,&t,&N);
        for(int i=0;i<N;i++){
            scanf("%lf%lf%lf",&p[i].b,&p[i].e,&p[i].w);
            p[i].c=1.0/(p[i].w+s)-1.0/(p[i].w+r);
        }
        sort(p,p+N,cmp1);
        double res=0;
        for(int i=0;i<N;i++){
            if(i==0){
                res+=p[i].b;
            }else{
                if(p[i].b-p[i-1].e>=0){
                    res+=p[i].b-p[i-1].e;
                }//else while(1);
            }
        }
        if(x-p[N-1].e>=0) res+=x-p[N-1].e;
        //else while(1);
        p[N].b=0;
        p[N].e=res;
        p[N].w=0;
        p[N].c=1.0/(p[N].w+s)-1.0/(p[N].w+r);
        N++;
        sort(p,p+N,cmp);
        for(int i=0;i<N;i++){
            double tp=(p[i].e-p[i].b)/(r+p[i].w);
            //cout<<p[i].e<<" "<<p[i].b<<" "<<p[i].w<<endl;
            if(tp>t){
                ans+=t+((p[i].e-p[i].b)-t*(r+p[i].w))/(s+p[i].w);
                t=0;
            }else{
                ans+=tp;
                t-=tp;
            }
            //cout<<ans<<endl;
        }
        printf("Case #%d: %lf\n",ca,ans);
    }
    return 0;
}
