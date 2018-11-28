#include<iostream>
#include<cmath>
using namespace std;

const int maxN=500+5;
int n,tt,zz;
double x,y,z,sx,sy,sz,vx,vy,vz;

void add(double a,double &b){
    b=b+(a/n);
}
void init(){
    cin>>n;
    sx=0;sy=0;sz=0;
    vx=0;vy=0;vz=0;
    for (int i=1;i<=n;i++){
        cin>>x>>y>>z;
        add(x,sx);add(y,sy);add(z,sz);
        cin>>x>>y>>z;
        add(x,vx);add(y,vy);add(z,vz);
    }
}
bool cmp(double a,double b){
    if (abs(a-b)<1e-8) return true;
    else return false;
}
void work(){
    double a,b,c,t,ans;
    a=(vx*vx+vy*vy+vz*vz);
    b=2*(sx*vx+sy*vy+sz*vz);
    c=(sx*sx+sy*sy+sz*sz);
    if (cmp(a,0)) t=0;else {
        t=b/((-2)*a);
        if (t<0) t=0;
    }
    ans=a*t*t+b*t+c;
  
    //printf("%.2lf %.2lf %.2lf\n",vx,vy,vz);
    //printf("%.2lf %.2lf %.2lf\n",sx,sy,sz);
    //printf("%.2lf %.2lf %.2lf\n",a,b,c);
    cout<<"Case #"<<zz<<": ";
    printf("%.8lf %.8lf\n",sqrt(abs(ans)),t);
}
int main(){
    freopen("2.in","r",stdin);
    freopen("2.out","w",stdout);
    cin>>tt;
    for (zz=1;zz<=tt;zz++){
    init();
    work();}
    return 0;
}
