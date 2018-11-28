#include <iostream>
#include <iomanip>
#include <cmath>
#define SQR(x) ((x)*(x))
using namespace std;
int t;
struct pt{
    long double x,y,r;
} p[5005],q[1005];

int main(){
    cin >> t;
    int o = t;
    while (t--){
        cout << "Case #"<< o-t <<":";
        int n,m;
        cin >> n >> m;
        for (int i = 0; i < n; ++i)
            cin >> p[i].x >> p[i].y;
        for (int i = 0; i < m; ++i){
            long double x1,x2,y1,y2,r1,r2;
            x2 = p[1].x;
            y2 = p[1].y;
            x1 = p[0].x;
            y1 = p[0].y;
            cin >> q[i].x >> q[i].y;
            r1 = sqrt(SQR(x1-q[i].x)+SQR(y1-q[i].y));
            r2 = sqrt(SQR(x2-q[i].x)+SQR(y2-q[i].y));
            x2-=x1;
            y2-=y1;
            y2 = sqrt(SQR(x2)+SQR(y2));
            x1 = y1 = x2 = 0;
            long double r,R,d;
            r = r2;
            R = r1;
            d = y2;
            long double ans = (long double)r*r*acos((d*d+r*r-R*R)/2/d/r)+(long double)R*R*acos((d*d+R*R-r*r)/2/d/R)-(long double)sqrt(((long double)-d+r+R)*(d+r-R)*(d-r+R)*(d+r+R))/2;
            cout <<" "<<fixed <<setprecision(8)<<ans;
        }
        cout << endl;
    }
    
    
}
