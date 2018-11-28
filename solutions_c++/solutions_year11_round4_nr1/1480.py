#include<cstdio>
#include<iostream>
using namespace std;
struct node{
    double st,en,sp;
}e[1004];
int cmp(node x,node y){
    return x.sp<y.sp;
}
int vis[1000007];
int que[1000007];
int main(){
    int T;
    double x,s,t,r;
    int n,i,j;
   freopen ("A-large.in","r",stdin);
   freopen ("Aa.out","w",stdout);
    cin>>T;
    int cas;
    for(cas=1;cas<=T;cas++){
        cin>>x>>s>>r>>t>>n;
        //cout<<x<<" "<<s<<" "<<r<<" "<<t<<" "<<n<<endl; 
        for(i=0;i<n;i++)cin>>e[i].st>>e[i].en>>e[i].sp;
        sort(e,e+n,cmp);
        double tm=0;
        for( i=0;i<n;i++){
            tm+=(e[i].en-e[i].st)/(e[i].sp+s);
            x-= (e[i].en-e[i].st);
        }
        if(r*t<=x){
            tm=tm+t+(x-r*t)/s;
            printf("Case #%d: %.10lf\n",cas,tm);
            continue;
        }
        else {
            t=t-x/r;
            tm+=x/r;
            i=0;
            while(t>0&&i<n){
                tm=tm-(e[i].en-e[i].st)/(e[i].sp+s);
                if( t > (e[i].en-e[i].st)/(e[i].sp+r) ){
                    tm=tm+(e[i].en-e[i].st)/(e[i].sp+r);
                    t=t-(e[i].en-e[i].st)/(e[i].sp+r);
                    i++;
                }
                else {
                    double lf=e[i].en-e[i].st-(e[i].sp+r)*t;
                    tm+=t;
                    tm=tm+lf/(e[i].sp+s);
                    t=0;
                }
            }
            printf("Case #%d: %.10lf\n",cas,tm);
        }
    }
}          
