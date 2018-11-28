#include <cstdio>
#include <iostream>
#include <cassert>
#include <cstdlib>
#include <cstring>
#include <cmath>

using namespace std;

double cir_data[40][3]; 
int set1[40];
int set2[40];
int n1, n2;



int main()
{
    int C;
    
    cin >> C;

    for(int i=1; i<=C; i++)
    {
        int N;
        cin >> N;
        double ans;
        
        for(int j=0; j<N; j++)
        {
            cin >> cir_data[j][0];
            cin >> cir_data[j][1];
            cin >> cir_data[j][2];
        }
        
        if(N==1)
        {
            ans = cir_data[0][2];    
            goto report;
        }
        if(N==2)
        {
            ans = cir_data[0][2];
            if(ans < cir_data[1][2])
                ans = cir_data[1][2];
            goto report;
        }
            double d1, d2, d3;
            double x1, x2, x3, y1, y2, y3;
        if(N==3)
        {
            x1 = cir_data[0][0];
            y1 = cir_data[0][1];
            x2 = cir_data[1][0];
            y2 = cir_data[1][1];
            x3 = cir_data[2][0];
            y3 = cir_data[2][1];
            d1 = sqrt( (x2-x3)*(x2-x3)+(y2-y3)*(y2-y3) ) + cir_data[1][2] + cir_data[2][2];
            d2 = sqrt( (x1-x3)*(x1-x3)+(y1-y3)*(y1-y3) ) + cir_data[0][2] + cir_data[2][2];
            d3 = sqrt( (x2-x1)*(x2-x1)+(y2-y1)*(y2-y1) ) + cir_data[1][2] + cir_data[0][2];
            d1 /= 2;
            d2 /= 2;
            d3 /= 2;
            if( d1 < cir_data[0][2] )
                d1 = cir_data[0][2];
            if( d2 < cir_data[1][2] )
                d2 = cir_data[1][2];
            if( d3 < cir_data[2][2] )
                d3 = cir_data[2][2];
                
            ans = d1;
            if(ans>d2)
                ans = d2;
            if(ans>d3)
                ans = d3;
            
        }
        

report:        
        cout << "Case #" << i << ": ";
        printf("%0.6f\n", ans);
    }
    
//    cin >> C;
    return 0;
}
