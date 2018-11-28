#include <iostream>
#include <cstdio>
#include <math.h>
using namespace std;
#define For(i,a,b) for(int i=a;i<=b;i++)
#define eps 1e-11

int n;
long long x[505], y[505], z[505], vx[505], vy[505], vz[505];
int main(){
    freopen("bl.in", "r", stdin);
    freopen("b.out","w", stdout);
    int n0fTest;
    cin>>n0fTest;
    For(test,1,n0fTest){
        cin>>n;
        For(i,1,n)
            cin>>x[i]>>y[i]>>z[i]>>vx[i]>>vy[i]>>vz[i];
        
        long long X, Y, Z, VX, VY, VZ;
        X=Y=Z=VX=VY=VZ=0;
        For(i,1,n){
            X+=x[i];
            Y+=y[i];
            Z+=z[i];
            VX+=vx[i];
            VY+=vy[i];
            VZ+=vz[i];
        }
        double t;
        if (VX==0 && VY==0 && VZ==0){
            t=0;
        } else {
            t = - ((double) (VX*X + VY*Y + VZ*Z)) / (VX*VX + VY*VY + VZ*VZ);
        }
   //     cout<<n<<" "<<VX<<" "<<VY<<" "<<VZ<<" "<<X<<" "<<Y<<" "<<Z<<" "<<t<<endl;
        if (t<eps) t=0.0;
        
        double d =    (X*X + Y*Y + Z*Z) 
                    + (VX*VX + VY*VY + VZ*VZ)*(t*t)
                    + 2*(X*VX+ Y*VY +Z*VZ)*t;
        d/=(n*n);
//        cout<<d<<" "<<eps<<" "<<(d<-eps)<<endl;
        if (d<eps) d=0.0;
        d=sqrt(d);
//      -1900 -1150 -360 2280 1380 432 1.2
//      Case #29: -1.#IND000000 1.2000000000

        printf("Case #%d: %0.10f %0.10f\n", test, d, t);
    }
    return 0;
}
