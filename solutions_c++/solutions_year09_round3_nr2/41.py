#include <iostream>
#include <string>
#include <cmath>
using namespace std;

double a0, a1, a2, b0, b1,b2;
double rd, rt=0;
double a, b,c;
int n;
void gao(double t) {
     if (t >= 0 && a*t*t+b*t+c<rd) {
           rd = a*t*t+b*t+c;
           rt = t;
     }
}
void done() {
      a = (b0*b0+b1*b1+b2*b2);
      b=2*(a0*b0+a1*b1+a2*b2);
      c = a0*a0+a1*a1+a2*a2;
     double t1 = -b/2/a;
     double t2 = 0, t3 =0;
     double t4 = 0;
     if (b*b-4*a*c>=0) {
        t2 = (-b+sqrt(b*b-4*a*c))/2/a;
        t3 = (-b-sqrt(b*b-4*a*c))/2/a;
     }
     rd=c, rt=0;
     gao(t1);
     gao(t2);
     gao(t3);
     gao(t4);
     cout.setf(ios::fixed);
     cout.precision(8);
     if (rd<0)rd=0;
     cout << sqrt(rd)/n << " " << rt <<endl;
}
int main() {
    int as;
    cin >> as;
    for (int kk=0; kk < as; ++kk) {
        cout << "Case #" << kk+1 << ": ";
        cin >> n;
        int x,y,z,dx,dy,dz;
        a0=a1=a2=0;
        b0=b1=b2=0;
        for (int i =0; i <n; ++i) {
            cin >> x>>y>>z>>dx>>dy>>dz;
            a0+=x;
            a1+=y;
            a2+=z;
            b0+=dx;
            b1+=dy;
            b2+=dz;
        }
        done();
    }
    return 0;
}
