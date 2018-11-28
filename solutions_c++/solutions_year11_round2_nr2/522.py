#include <iostream>
#include <cstdio>
#include <cmath>
using namespace std;

int n, d;
int p[202], c[202];
double eps = 1e-8;

bool check(double t){
    double lastPos = -1e10;
    for(int i=0;i<n;i++){
        for(int j=0;j<c[i];j++){
            if (lastPos + d > p[i] + t + eps){
                // cant move that far
                return false;
            }
            if (lastPos + d < p[i] - t){
                lastPos = p[i]-t;
            } else {
                lastPos = lastPos + d;
            }
        }
    }
    return true;
}

int main(){

    int ntest;
    cin>>ntest;

    for(int test=1;test<=ntest;test++){
        cin>>n>>d;
        for(int i=0;i<n;i++){
            cin>>p[i]>>c[i];
        }

        double L=0;
        double R=100000000;

        while (fabs(R-L)>eps){
            double m = (L+R)/2;
            if (check(m)){
                R = m;
            } else {
                L = m;
            }
        }

        printf("Case #%d: %0.9f\n", test, R);
    }

    return 0;
}
