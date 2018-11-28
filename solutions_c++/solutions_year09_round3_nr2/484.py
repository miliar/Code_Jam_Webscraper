#include<iostream>
#include<vector>
#include<cmath>

using namespace std;

vector<double> operator+(const vector<double> &a,const vector<double> &b){
    vector<double> c(a.size());
    for(int i=0;i<a.size();++i)
        c[i]=a[i]+b[i];
    return c;
}

double dist(vector<double> a){
    double res=0;
    for(int i=0;i<a.size();++i)
        res+=a[i]*a[i];
    return res;
}

double dist(vector<double> a,vector<double> b,double t){
    vector<double> c(a.size());
    for(int i=0;i<a.size();++i)
        c[i]=a[i]+t*b[i];
    return dist(c);
}

int main(){
    freopen("B-small-attempt6.in","r",stdin);
    freopen("x.out","w",stdout);
    int tc;
    scanf("%d\n",&tc);
    for(int t=1;t<=tc;++t){
        if(t>1)cout<<endl;
        int n;
        scanf("%d",&n);
        vector<double> a(3),b(3);
        int x,y,z,vx,vy,vz;
        for(int i=0;i<n;++i){
            scanf("%d %d %d %d %d %d",&x,&y,&z,&vx,&vy,&vz);
            a[0]+=x;
            a[1]+=y;
            a[2]+=z;
            b[0]+=vx;
            b[1]+=vy;
            b[2]+=vz;
        }
        for(int i=0;i<3;++i)
            a[i]/=n,b[i]/=n;
        if(b[0]==0&&b[1]==0&&b[2]==0){
            printf("Case #%d: %lf %lf",t,sqrt(dist(a,b,0)),0);
        }
        else{
            double min=0,max=4e4,eps=1e-9;
            while(min+eps*10<max){
                double med=(min+max)/2;
                if(dist(a,b,med-eps)<=dist(a,b,med+eps))
                    max=med;
                else min=med;
            }
            printf("Case #%d: %lf %lf",t,sqrt(dist(a,b,(min+max)/2)),(min+max)/2);
        }    
    }
    return 0;
}
