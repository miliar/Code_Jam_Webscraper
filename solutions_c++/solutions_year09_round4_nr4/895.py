#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <sstream>
using namespace std;
int main(int argc, char** argv)
{
	
    int C;
    int N;
    double x[3];
    double y[3];
    double r[3];
    
    double r1;
    double r2;
    double dist;
    double minrr;
    double minr[3];
    
    scanf("%d", &C);
    for(int casenumber = 0; casenumber < C; ++casenumber)
    {
        scanf("%d", &N);
        for(int i = 0; i < N; ++i)
            scanf("%lf %lf %lf", x + i, y + i, r + i);
        if(N == 1)
        {
            printf("Case #%d: %lf\n", casenumber + 1, r[0]);
            continue;
        }
        else if(N == 2)
        {
            if(r[0] > r[1])
                printf("Case #%d: %lf\n", casenumber + 1, r[0]);
            else  printf("Case #%d: %lf\n", casenumber + 1, r[1]);
            continue;
        }
               
        // 1 & 2 ---- 3
        dist = sqrt( (x[0] - x[1]) * (x[0] - x[1]) + (y[0] - y[1]) * (y[0] - y[1]));
        r1 = r[0] + r[1] + dist;
        r2 = r[2];
        if(r1 >= r2) minr[0] = r1; else minr[0] = r2;
        
        // 1 & 3 ---- 2
        dist = sqrt( (x[0] - x[2]) * (x[0] - x[2]) + (y[0] - y[2]) * (y[0] - y[2]));
        r1 = r[0] + r[2] + dist;
        r2 = r[1];
        if(r1 >= r2) minr[1] = r1; else minr[1] = r2;
        
        // 2 & 3 ---- 3
        dist = sqrt( (x[1] - x[2]) * (x[1] - x[2]) + (y[1] - y[2]) * (y[1] - y[2]));
        r1 = r[1] + r[2] + dist;
        r2 = r[0];
        if(r1 >= r2) minr[2] = r1; else minr[2] = r2;
        
        minrr = minr[0];
        if(minrr > minr[1]) minrr = minr[1];
        if(minrr > minr[2]) minrr = minr[2];
        
        printf("Case #%d: %lf\n", casenumber + 1, minrr / 2);
    }  

	return 0;
}
