#include <algorithm>
#include <iostream>
#include <sstream>
#include <cmath>
#include <string>
#include <vector>
#define  f(x,y,i) for(int i=x;i<y;i++)
using namespace std;

double modulo(int a,int b,int c){
    return sqrt(a*a+b*b+c*c);
}

int main()
{
    int T,N; vector<int> x(3); vector<int> v(3); long long p;
    vector<int> xx(3,0); vector<int> vv(3,0);
    cin>>T;
    f(1,T+1,k){
        cin>>N;
        xx.clear(); xx.resize(3,0);
        vv.clear(); vv.resize(3,0);
        f(0,N,j){
            cin>>x[0]>>x[1]>>x[2]>>v[0]>>v[1]>>v[2];
            f(0,3,i){xx[i]+=x[i]; vv[i]+=v[i];}
        }
        p=0;
        double pos;
        f(0,3,i)p+=(long long)xx[i]*(long long)vv[i];
        if(p>=0){
            printf("Case #%d: ",k);
            pos=modulo(xx[0],xx[1],xx[2]);
            cout<<pos/N<<" "<<"0.00000000"<<endl;            
            continue;
        }
        long long q=0; f(0,3,i) q+=(long long)vv[i]*(long long)vv[i];
        double t=(double)p/(double)q; t=-t; 
        pos=sqrt((xx[0]+t*vv[0])*(xx[0]+t*vv[0])+(xx[1]+t*vv[1])*(xx[1]+t*vv[1])+(xx[2]+t*vv[2])*(xx[2]+t*vv[2]));
        printf("Case #%d: %.8f %.8f\n",k,pos/N,t);
        
    }
}
