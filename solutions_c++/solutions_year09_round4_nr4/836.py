#include<iostream>
#include<string>
#include<map>
#include<algorithm>
#include<vector>
#include<cstdio>
#include<queue>
#include<set>
#include<sstream>
#include<cmath>
using namespace std;
int x[40],y[40],r[40];
double dist(int x1,int y1,int x2,int y2){
    double X=x1-x2;
    double Y=y1-y2;
    return sqrt(X*X+Y*Y);
}
void procesa(int test){
    cout<<"Case #"<<test<<":";
    int n;
    cin>>n;
    for(int i=0;i<n;++i){
        cin>>x[i]>>y[i]>>r[i];
    }
    if(n==1){
        printf(" %.6lf\n",(double)r[0]);
        return;
    }
    if(n==2){
        printf(" %.6lf\n",max((double)r[0],(double)r[1]));
        return;
    }
    double ret=max((r[0]+r[1]+dist(x[0],y[0],x[1],y[1]))/2,(double)r[2]);
    for(int i=0;i<2;++i)
        for(int j=i+1;j<3;++j){
            ret=min(ret,max((r[i]+r[j]+dist(x[i],y[i],x[j],y[j]))/2,(double)r[3-i-j]));
            //cout<<ret<<endl;
        }
    printf(" %.6lf\n",ret);
}
int main(){
    int N;
    cin>>N;
    int test=1;
    while(N--){
        procesa(test++);
    }
}
