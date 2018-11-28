#include<iostream>
#include<cmath>
using namespace std;

int x[3],y[3],r[3];

double sqr(double x){return x*x;}

double work(int i1,int i2,int i3){
    double tmp=double(sqrt(sqr(x[i1]-x[i2])+sqr(y[i1]-y[i2]))+r[i1]+r[i2])/2;
    if (tmp>r[i3]) return tmp;
    else return r[i3];
}

int main(){
    int C,I,n,i;
    cin>>C;
    for (I=1;I<=C;++I){
        cout<<"Case #"<<I<<": ";
        cin>>n;
        for (i=0;i<n;++i) cin>>x[i]>>y[i]>>r[i];
        if (n==1) cout<<r[0];
        else if (n==2){
            if (r[0]>r[1]) cout<<r[0];
            else cout<<r[1];
        }else{
            double res=work(0,1,2);
            double tmp=work(0,2,1);
            if (tmp<res) res=tmp;
            tmp=work(1,2,0);
            if (tmp<res) res=tmp;
            cout<<res;
        }
        cout<<endl;
    }
    return 0;
}
