#include<iostream>
#include<stdio.h>
#include<vector>
#include<algorithm>

using namespace std;

double eps=1e-7,t;

double f(int len,int s,int r,int e){
    double res=0,t1=1.0*len/(r+e);
    res+=min(t1,t);
    res+=max((len-min(t1,t)*(r+e))/(s+e),0.);
    t-=min(t1,t);
    return res;
}

int main(){
    freopen("A-large.in","r",stdin);
    freopen("x.out","w",stdout);
    int tc,n,x,s,r;
    cin>>tc;
    for(int q=1;q<=tc;q++){
        cin>>x>>s>>r>>t>>n;
        int xx=x,a,b,e;
        double res=0;
        vector<pair<int,int> > V;
        for(int i=0;i<n;i++){
            cin>>a>>b>>e;
            V.push_back(make_pair(e,b-a));
            xx-=b-a;
        }
        res+=f(xx,s,r,0);
        sort(V.begin(),V.end());
        for(int i=0;i<n;i++)
            res+=f(V[i].second,s,r,V[i].first);
        printf("Case #%d: %.7lf\n",q,res);
    }
    return 0;
}
