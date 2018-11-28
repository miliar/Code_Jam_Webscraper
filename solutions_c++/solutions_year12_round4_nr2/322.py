#include <iostream>
#include <string>
#include <string.h>
#include <algorithm>
#include <cstdio>
#include <vector>
using namespace std;

struct node{
    double x;
    int id;
    node(){}
    node(double _x,int _id){
        x=_x;
        id=_id;
    }
    bool operator <(const node& a)const{
        return x<a.x;
    }
};
    
double r,c;
double a[1200];
node b[1200];
double ans[1200][2];
int n;

int main(){
    int _,cas=0;
    scanf("%d",&_);
    while (_--){
        scanf("%d%lf%lf",&n,&r,&c);
        for (int i=1;i<=n;++i){ 
            scanf("%lf",&a[i]);
            b[i]=node(a[i],i);
        }
        sort(b+1,b+n+1);
        
        double x=0,y=0,delta=0;
        ans[b[1].id][0]=0;ans[b[1].id][1]=0;
        x=b[1].x;delta=b[1].x*2;y=0;
        bool cc=true;
        for (int i=2;i<=n;++i){
            if (x+b[i].x<=r){
                ans[b[i].id][0]=x+b[i].x;
                if (cc){
                    ans[b[i].id][1]=y;
                    delta=max(delta,b[i].x);
                }else{
                    ans[b[i].id][1]=y+b[i].x;
                    delta=max(delta,b[i].x*2);
                }
                x+=b[i].x*2;
            }else{
                cc=false;
                y+=delta;
                x=b[i].x;
                ans[b[i].id][0]=0;
                ans[b[i].id][1]=y+b[i].x;
                delta=b[i].x*2;
            }
        }
        printf("Case #%d:",++cas);
        for (int i=1;i<=n;++i) printf(" %.2f %.2f",ans[i][0],ans[i][1]);
        puts("");
    }
    return 0;
}
            
