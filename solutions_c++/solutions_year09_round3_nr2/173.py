#include <cstdio>
#include <iostream>
#include <sstream>

#include <cstring>
#include <cstdlib>

#include <list>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <string>

#include <complex>
#include <cmath>

#include <algorithm>
#include <numeric>
#include <utility> 

using namespace std;

char buffer[1000];

double c_x;
double c_y;
double c_z;

double c_vx;
double c_vy;
double c_vz;

double dist(double x, double y, double z)
{
    return sqrt(x*x + y*y + z*z);
}

int main(int argc, char** argv)
{
    int T;
    
    scanf("%d", &T);
    
    for(int t = 1; t <= T; ++t)
    {
        c_x = 0;
        c_y = 0;
        c_z = 0;
        
        c_vx = 0;
        c_vy = 0;
        c_vz = 0;
        
        int N;
        scanf("%d", &N);
        
        for(int i = 0; i < N; ++i)
        {
            int tx, ty, tz, tvx, tvy, tvz;
            scanf("%d %d %d %d %d %d", &tx, &ty, &tz, &tvx, &tvy, &tvz);
            
            c_x += tx;
            c_y += ty;
            c_z += tz;
            
            c_vx += tvx;
            c_vy += tvy;
            c_vz += tvz;
        }
        
        c_x /= N;
        c_y /= N;
        c_z /= N;
        
        c_vx /= N;
        c_vy /= N;
        c_vz /= N;
        
        double num = c_x*c_vx + c_y*c_vy + c_z*c_vz;
        double den = c_vx*c_vx + c_vy*c_vy + c_vz*c_vz;
        
        if(den < 1e-8)
        {
            printf("Case #%d: %lf %lf\n", t, dist(c_x, c_y, c_z), 0.0);
        }
        else
        {
            double time = -num/den;
            
            if(time < 0)
                time = 0;
            
            double nx = c_x + time*c_vx;
            double ny = c_y + time*c_vy;
            double nz = c_z + time*c_vz;
            
            printf("Case #%d: %lf %lf\n", t, dist(nx, ny, nz), time);
        }
    }
    
    return 0;
}