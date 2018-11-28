#include <iostream>
#include <fstream>
#include <cstdlib>
#include <sstream>
#include <cmath>
#include <iomanip>

#include <algorithm>
#include <vector>
#include <string>
#define fori(N) for(int i=0; i<N; i++)
#define forj(N) for(int j=0; j<N; j++)

using namespace std;


int main(){
    ifstream fin("B-larg.in");
    ofstream fout("B-large.out");
    
    int n;
    fin >> n;
    for(int Z=0; Z<n; Z++){
        long numFlies, a=0, b=0, c=0, tx=0, ty=0, tz=0, tvx=0, tvy=0, tvz=0;
        fin >> numFlies;
        long x[numFlies], y[numFlies], z[numFlies], vx[numFlies], vy[numFlies], vz[numFlies];
        
        fori(numFlies){
            fin >> x[i] >> y[i] >> z[i] >> vx[i]>>vy[i]>>vz[i];
            tx += x[i]; ty+=y[i]; tz+=z[i]; tvx += vx[i]; tvy +=vy[i];tvz+=vz[i];
        }
        a = tvx*tvx + tvy*tvy + tvz*tvz;
        b = 2*(tx*tvx + ty*tvy + tz*tvz);
        c = tx*tx + ty*ty + tz*tz; 
        
        double t;
        if(b>=0 || a == 0) t = 0;
        else t = (double)(-b)/(2*a);
        
        if(Z==2) cout << a << " " << b << " " << c << endl;
        a /= numFlies*numFlies; b/= numFlies*numFlies; c /= numFlies*numFlies;
        if(Z==2) cout << a << " " << b << " " << c << endl;
        
        double mx=0, my=0, mz=0;
        fori(numFlies){
            mx += x[i] + t*vx[i];
            my += y[i] + t*vy[i];
            mz += z[i] + t*vz[i];
        }
        if(Z==2) cout << t << ":" << mx << " " << my << " " << mz << endl;
        mx /= numFlies; my /= numFlies; mz /= numFlies;
        double d = sqrt(mx*mx + my*my + mz*mz);
        //cout << mx/numFlies << " " << my/numFlies << " " << mz/numFlies << endl;
        fout.setf(ios::fixed & ios::floatfield);
        fout.precision(8);
        fout << "Case #" << Z+1 <<": " << d << " " << t << endl;
    }
     
    cin.get();
    return 0;   
}
