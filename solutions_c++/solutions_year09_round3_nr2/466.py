#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <cmath>
#include <float.h>
#define For(i,a,b) for(i=a;i<b;i++)
#define Forto(i,n) For(i,0,n)

using namespace std;

double vec(int x, int y, int z) {
    double k;
    k = sqrt(x*x + y*y + z*z);
    return k;
}

int main()
{
    int T, Case = 1;
    int i,j,k;

    cin >> T;

    while (T--) {
        int n;
        double dmin, tmin;
        cin >> n;

        int x,y,z,vx,vy,vz;
        double vvx=0, vvy=0, vvz=0;
        double sumx=0, sumy=0, sumz=0, vsum=0;
        Forto(i,n) {
            scanf("%d %d %d %d %d %d", &x, &y, &z, &vx, &vy, &vz);
            sumx+=x; sumy+=y; sumz+=z;
            vvx+=vx; vvy+=vy; vvz+=vz;
        }
        sumx /= n; sumy /= n; sumz /= n;
        vvx /= n; vvy /= n; vvz /= n;

        if(vvx*vvx + vvy*vvy + vvz*vvz !=0) {
            tmin = -1*(sumx*vvx + sumy*vvy + sumz*vvz) / (vvx*vvx + vvy*vvy + vvz*vvz);
            if(tmin < 0) tmin = 0;
            dmin = (sumx*sumx + 2*sumx*vvx*tmin + vvx*tmin*vvx*tmin) + (sumy*sumy + 2*sumy*vvy*tmin + vvy*tmin*vvy*tmin) + (sumz*sumz + 2*sumz*vvz*tmin + vvz*tmin*vvz*tmin);
            if(dmin<0) dmin = -1*dmin;
            dmin = sqrt(dmin);
        }
        else if(sumx*vvx + sumy*vvy + sumz*vvz) {
            tmin = sumx*sumx + sumy*sumy + sumz*sumz;
            tmin = -1*tmin;
            tmin = tmin / 2;
            tmin = tmin / (sumx*vvx + sumy*vvy + sumz*vvz);
            dmin = 0.0;
        }
        else {
            dmin = sumx*sumx + sumy*sumy + sumz*sumz;
            dmin = sqrt(dmin);
            tmin = 0.0;
        }

        cout << "Case #" << Case++ << ": ";
        printf("%lf %lf\n", dmin, tmin);
    }
}
