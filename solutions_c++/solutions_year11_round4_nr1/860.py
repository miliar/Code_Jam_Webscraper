#include <stdio.h>
#include <algorithm>
#include <set>
using namespace std;
struct node{
    int st,en,speed;
}arr[100005];
bool operator<(const node& a,const node& b){
    if(a.speed==b.speed) return (a.en-a.st)>(b.en-b.st);
    return a.speed<b.speed;
}
int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int i,t,x,s,r,n,tt;
    scanf("%d",&tt);
    for(int cs=1;cs<=tt;++cs){
        scanf("%d%d%d%d%d",&x,&s,&r,&t,&n);
        for(i=0;i<n;++i){
            scanf("%d%d%d",&arr[i].st,&arr[i].en,&arr[i].speed);
        }
        int k=n,cur=0;
        for(i=0;i<n;++i){
            if(arr[i].st>cur){
                arr[k].st=cur,arr[k].en=arr[i].st,arr[k].speed=0;
                ++k;
            }
            cur=arr[i].en;
        }
        if(cur<x){
            arr[k].st=cur,arr[k].en=x,arr[k].speed=0;
            cur=x,++k;
        }
        sort(arr,arr+k);
        double res=0;
        for(i=0;i<k;++i){
            double dist=arr[i].en-arr[i].st;
            double sp=arr[i].speed+r;
            double temp=dist/sp;
            if(res+temp<=t) res+=temp;
            else{
                double ex=t-res;
                res=t;
                dist-=ex*sp;
                sp=arr[i].speed+s;
                temp=dist/sp;
                res+=temp;
                break;
            }
        }
        for(++i;i<k;++i){
            double dist=arr[i].en-arr[i].st;
            double sp=arr[i].speed+s;
            double temp=dist/sp;
            res+=temp;
        }
        printf("Case #%d: %.10lf\n",cs,res);
    }
    return 0;
}
