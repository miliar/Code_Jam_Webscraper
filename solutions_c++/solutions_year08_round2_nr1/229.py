#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

#define x first
#define y second
#define EPS 1e-9

using namespace std;

typedef pair<double,double> PDD;

bool equal(double a, double b){
    return abs(a-b)<EPS;
}

bool grid(double x, double y){
    if (!equal(x,floor(x)) && !equal(x,ceil(x))) return 0;
    if (!equal(y,floor(y)) && !equal(y,ceil(y))) return 0;
    return 1;
}

int main(){
    int t;
    cin>>t;
    for (int ct=0;ct<t;++ct){
        long long n,A,B,C,D,x0,y0,M;
        cin>>n>>A>>B>>C>>D>>x0>>y0>>M;
        vector<PDD> p(n);
        long long X=x0,Y=y0;
        for (int i=0;i<n;++i){
            p[i].x=X;
            p[i].y=Y;
            X=(A*X+B)%M;
            Y=(C*Y+D)%M;
        }
        long long ans=0;
        for (int i=0;i<p.size();++i){
            for (int j=i+1;j<p.size();++j){
                for (int k=j+1;k<p.size();++k){
                    double x1,y1,x2,y2,x3,y3;
                    x1=p[i].x;
                    y1=p[i].y;
                    x2=p[j].x;
                    y2=p[j].y;
                    x3=p[k].x;
                    y3=p[k].y;
                    double xm,ym;
                    xm=(x1+x2+x3)/3.;
                    ym=(y1+y2+y3)/3.;
                    if (grid(xm,ym)) ++ans;
                }
            }
        }
        cout<<"Case #"<<ct+1<<": "<<ans<<endl;
    }
}
