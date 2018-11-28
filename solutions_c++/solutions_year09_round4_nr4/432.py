#include <iostream>
#include <string>
#include <cmath>
using namespace std;

int n;
struct cir{
       double x, y, r;
};
cir b[100];

#define max(x,y) ((x)>(y)?(x):(y))
#define min(x,y) ((x)>(y)?(x):(y))
#define dis(i,j) sqrt((b[i].x-b[j].x)*(b[i].x-b[j].x)+(b[i].y-b[j].y)*(b[i].y-b[j].y))
double done() {
     if (n==1) return b[0].r;
     if (n==2) return b[0].r>b[1].r?b[0].r:b[1].r;
     if (n==3) {
         double rr = max((dis(0,1)+b[0].r+b[1].r)/2, b[2].r);
         if (rr > max((dis(0,2)+b[0].r+b[2].r)/2, b[1].r)) {
                rr=max((dis(0,2)+b[0].r+b[2].r)/2, b[1].r) ;
                }
                if (rr>max((dis(1,2)+b[1].r+b[2].r)/2, b[0].r)) {
                rr=max((dis(1,2)+b[1].r+b[2].r)/2, b[0].r) ;
                }
                return rr;
    }
               return 0;
}
int main() {
    int as;
    cin >> as;
    for (int kk=0; kk < as; ++kk) {
        cout << "Case #" << kk+1 << ": ";
        cin >> n;
        for (int i = 0; i < n; ++i) {
            cin >> b[i].x>>b[i].y>>b[i].r;
            }
       cout << done()<<endl;
    }
    return 0;
}
