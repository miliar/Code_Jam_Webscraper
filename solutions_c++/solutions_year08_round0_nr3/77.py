#include <iostream>
#include <cstdlib>
#include <cmath>

using namespace std;

double sdrand() {
    return (drand48()-0.5)*2.0;
}

int arredonda(double n) {
    if(n < 0) {
        return -int(-n+0.5);
    } else {
        return int(n+0.5);
    }
}

template <class T> T Q(T x) {
    return x*x;
}

bool scan_circulo(double& x, double y, double raio2) {
    double delta = -y*y + raio2;
    if(delta < 0) {
        x = 0;
        return false;
    }
    double sqrt_delta = sqrt(delta);
    x = sqrt_delta;
    return true;
}


const int REPETE = 100000000;

double odd(double f, double R, double t, double r, double g) {
    double R2 = R*R;
    double mr = (R-t-f);
    if(mr <= 0) {
        return 1.0;
    }
    if(f+f >= g) {
        return 1.0;
    }
    mr *= mr;

    double sqsz = g+r+r;
    int strings = int(R / sqsz + 1.0);

    double area = 0;

    for(int i=0;i<strings;++i) {
        for(int j=0;j<strings;++j) {
            double x1 = i*sqsz + r+f, y1 = j*sqsz + r+f;
            double d1 = x1*x1 + y1*y1;
            if(d1 >= mr) {
                continue;
            }
            double x2 = (i+1)*sqsz-r-f, y2 = (j+1)*sqsz-r-f;
            double d2 = x2*x2 + y2*y2;
            if(d2 <= mr) {
                area += Q(g-f-f);
                continue;
            }
            double d12 = x1*x1 + y2*y2;
            double d21 = x2*x2 + y1*y1;
            if(d12 <= mr and d21 <= mr) {
                /* caso 1, tira uma pontinha */
                double p1x = x2, p1y;
                scan_circulo(p1y, p1x, mr);
                double p2x, p2y = y2;
                scan_circulo(p2x, p2y, mr);
                double a1 = atan2(p1y, p1x);
                double a2 = atan2(p2y, p2x);
                double angle = a2-a1;
                area += mr*angle / 2.0 - (p1x*p2y - p1y*p2x) / 2.0;
                area += (p2x-x1)*(y2-y1) + (y2-y1+p1y-y1)*(x2-p2x)/2.0;
            } else if(d12 > mr and d21 <= mr) {
                /* caso 2, tira parte de cima */
                double p1x = x2, p1y;
                scan_circulo(p1y, p1x, mr);
                double p2x = x1, p2y;
                scan_circulo(p2y, p2x, mr);
                double a1 = atan2(p1y, p1x);
                double a2 = atan2(p2y, p2x);
                double angle = a2-a1;
                area += mr*angle / 2.0 - (p1x*p2y - p1y*p2x) / 2.0;
                area += (p2y-y1+p1y-y1)*(x2-x1)/2.0;
            } else if(d12 <= mr and d21 > mr) {
                /* caso 3, tira parte do lado */
                double p1x, p1y = y1;
                scan_circulo(p1x, p1y, mr);
                double p2x, p2y = y2;
                scan_circulo(p2x, p2y, mr);
                double a1 = atan2(p1y, p1x);
                double a2 = atan2(p2y, p2x);
                double angle = a2-a1;
                area += mr*angle / 2.0 - (p1x*p2y - p1y*p2x) / 2.0;
                area += (p1x-x1+p2x-x1)*(y2-y1)/2.0;
            } else if(d12 > mr and d21 > mr) {
                /* caso 4, sobra o canto */
                double p1x, p1y = y1;
                scan_circulo(p1x, p1y, mr);
                double p2x = x1, p2y;
                scan_circulo(p2y, p2x, mr);
                double a1 = atan2(p1y, p1x);
                double a2 = atan2(p2y, p2x);
                double angle = a2-a1;
                area += mr*angle / 2.0 - (p1x*p2y - p1y*p2x) / 2.0;
                area += (p1x-x1)*(p2y-y1)/2.0;
            }
        }
    }

    return 1 - area / (M_PI * R2/4.0);
}

int main(void) {
    int N;
    cin >> N;
    for(int C=0;C<N;++C) {
        double f, R, t, r, g;
        cin >> f >> R >> t >> r >> g;
        printf("Case #%d: %.7f\n", C+1, odd(f, R, t, r, g));
    }
    return 0;
}
