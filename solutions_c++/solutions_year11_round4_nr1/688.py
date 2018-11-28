#include<stdio.h>
#include<stdlib.h>
#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
struct way{
    int l,w;
    bool operator < (const way &o)const{
        if(w!=o.w)return w<o.w;
        return l<o.l;
    }
};
void solve(int test){
    printf("Case #%d: ",test);
    int x,s,r,t,n;
    cin >> x >> s >> r >> t >> n;

    double ans=0.0,rem=1.0*t;
    int now=0;
    vector<way> v;
    for(int i=0;i<n;i++){
        way tmp;
        int ss,ee,ww;
        cin >> ss >>ee >>ww;
        tmp.l=ee-ss;
        x-=tmp.l;
        tmp.w=ww+s;
        v.push_back(tmp);
    }
    way tmp;
    tmp.l=x;
    tmp.w=s;
    v.push_back(tmp);
    sort(v.begin(),v.end());
    int i=0;
    way otw;
    //double rem=t;
    double a=r-s;
    for(i=0;i<=n;i++){
        double time=v[i].l*1.0/(v[i].w+a);
        if(time<rem){
            rem-=time;
            ans+=time;
        }
        else{
            double go=rem*(v[i].w+a);
            ans+=rem;
            rem=0;
            ans+=(v[i].l-go)/v[i].w;
        }

    }
    printf("%.8lf\n",ans);
    return;
}
int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int n;
    cin >> n;
    for(int i=1;i<=n;i++)
    solve(i);
}
