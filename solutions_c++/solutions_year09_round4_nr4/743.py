#include<cmath>
#include<iostream>

using namespace std;
int N,T,px[3],py[3],pr[3];

double dist(double x1,double y1,double x2,double y2) {
    return sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1));
}

double join(int i,int j) {
    return (dist(px[i],py[i],px[j],py[j])+pr[i]+pr[j])/2;
}

int main() {
    cin>>T;
    for(int t=1;t<=T;t++) {
        cout<<"Case #"<<t<<": ";
        cin>>N;
        for(int i=0;i<N;i++) cin>>px[i]>>py[i]>>pr[i];
        if(N==1) cout<<pr[0]<<"\n";
        if(N==2) cout<<max(pr[0],pr[1])<<"\n";
        if(N==3) {
        double sol=999999999;
        sol=min(sol,join(0,1));
        sol=min(sol,join(0,2));
        sol=min(sol,join(1,2));
        for(int i=0;i<N;i++) sol=max(sol,(double)pr[i]);
        cout<<sol<<"\n";
        }
    }
    return 0;
}
