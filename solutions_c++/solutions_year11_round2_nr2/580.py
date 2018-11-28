#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <math.h>
#include <vector>
#include <fstream>
#include <iomanip>

using namespace std; 

ifstream fin("B-small-attempt0.in");
ofstream fout("B-small.out");

#define pre setprecision(9)
#define ll long long
#define MAX(a,b) ((a)>(b)?(a):(b))

int N, T, size;
int D;
int a[1000005];
double temp[1000005];
bool can(double t) {
     temp[1] = a[1]-t;
     for(int i = 2;i<=size;i++) {
          temp[i] = a[i]-t;
          if(temp[i]+2*t-temp[i-1]<D) return false;
          temp[i] = MAX(temp[i],temp[i-1]+D);
     }
     return true;
}

int main() {
    fin>>T;
    for(int k = 1;k<=T;k++) {
        fin>>N;
        fin>>D;
        size = 0;
        for(int i = 1;i<=N;i++) {
            int P,V;
            fin>>P>>V;
            for(int j = 0;j<V;++j)
                a[++size] = P;
        }
        double low = 0, high = 1000000000;
        double res = 0;
        sort(a+1,a+1+size);
        for(int i = 0;i<=50;i++) {
            double mid = (low+high)/2;
            if(can(mid)) {
                high = mid;
                res = mid;
            }
            else low = mid;
        }
        fout<<"Case #"<<k<<": ";
        fout<<pre<<res<<endl;
    }
    return 0;
}


