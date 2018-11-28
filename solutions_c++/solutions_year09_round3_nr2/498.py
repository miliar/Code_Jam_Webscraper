#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include<iostream>
#include<fstream>

using namespace std;

int main()
{
    ifstream fin ("in.txt");
    ofstream outfile("output.txt");
    
    int t,n;
    
    cin>>t;
    
    
    for(int i=0;i<t;i++)
    {
            cin>>n;

            double x1,y1,z1,vx1,vy1,vz1;
            double X = 0, Y = 0, Z = 0, VX = 0, VY = 0, VZ = 0;
            vector <double> x(n),y(n),z(n),vx(n),vy(n),vz(n);
            for(int j=0;j<n;j++)
            {
                    cin>>x[j]>>y[j]>>z[j]>>vx[j]>>vy[j]>>vz[j];
                    X += x[j];
                    Y += y[j];
                    Z += z[j];
                    VX += vx[j];
                    VY += vy[j];
                    VZ += vz[j];
           }        
           
           double nr = X*VX + Y*VY + Z*VZ;
           double dr = VX*VX + VY*VY + VZ*VZ;
           double t = 0;
           if (nr > 0) t = 0;
           else if (dr!= 0)
              t = (-1.0)*nr/dr;
              
           double dx = 0, dy = 0, dz = 0;
           for (int j = 0; j < n; j++) {
               dx += x[j]+(vx[j]*t);
               dy += y[j]+(vy[j]*t);
               dz += z[j]+(vz[j]*t);
           }
           double d = sqrt(pow(dx,2.0)+pow(dy,2.0)+pow(dz,2.0))/(double)n;
           outfile << fixed;
           outfile << "Case #" << i+1 << ": " << setprecision(8) << d << " " << t << "\n";
           
    }
                    
    
    
    
    
    
    
    //outfile<<"Case"<<" "<<"#"<<X<<":"<<" "<<K<<endl;
    
    
    
    //system("pause");
    
    return 0;
    
}
