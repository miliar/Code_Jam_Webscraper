/*
 * Author: fatboy_cw
 * Created Time:  2011/6/4 22:16:39
 * File Name: A.cpp
 */
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
using namespace std;
#define SZ(v) ((int)(v).size())

const double eps=1e-8;

int sgn(double x){
    return (x>eps)-(x<-eps);
}

struct Move{
    int b,e,w;
    bool operator < (const Move &A) const{
        return w<A.w;
    }
}temp[1005],move[5005];

int T; 
int ca,cnt;
int x,s,r,n;
double t;

bool cmp (const Move &m1,const Move &m2){
    return m1.b<m2.b;
}

int main() {
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    scanf("%d",&T);
    while(T--){
        scanf("%d%d%d%lf%d",&x,&s,&r,&t,&n);
        for(int i=1;i<=n;i++){
            scanf("%d%d%d",&temp[i].b,&temp[i].e,&temp[i].w);
        }
        sort(temp+1,temp+1+n,cmp);
        temp[n+1].b=x;
        cnt=0;
        if(temp[1].b){
            move[++cnt].b=0;
            move[cnt].e=temp[1].b;
            move[cnt].w=0;
        }
        for(int i=1;i<=n;i++){
            move[++cnt]=temp[i];
            if(temp[i+1].b>temp[i].e){
                move[++cnt].b=temp[i].e;
                move[cnt].e=temp[i+1].b;
                move[cnt].w=0;
            }
        }    
        sort(move+1,move+1+cnt);
        double ans=0.0;
        //for(int i=1;i<=cnt;i++){
            //cout<<move[i].b<<" "<<move[i].e<<" "<<move[i].w<<endl;
        //}
        for(int i=1;i<=cnt;i++){
            if(sgn(t-(move[i].e-move[i].b)/(double)(r+move[i].w))>=0){
                t-=(move[i].e-move[i].b)/(double)(r+move[i].w);
                ans+=(move[i].e-move[i].b)/(double)(r+move[i].w);
                //cout<<t<<" "<<ans<<endl;
            }
            else{
                ans+=(move[i].e-move[i].b-t*(r+move[i].w))/(double)(s+move[i].w)+t;
                for(int j=i+1;j<=cnt;j++){
                    ans+=(move[j].e-move[j].b)/(double)(s+move[j].w);
                }
                break;
            }
        }
        printf("Case #%d: ",++ca);
        printf("%.7lf\n",ans);
    }       
    return 0;
}

