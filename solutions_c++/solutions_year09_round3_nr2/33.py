#include <iostream>
#include <cmath>
using namespace std;
const double eps = 1e-9;
#define sqr(x) (x)*(x)
pair<double, double> mysolve(double a, double b, double c){
    if (a == 0) 
        if (b != 0) {
            double x = -c / b + eps;
            if (x > 0)
                return make_pair(0, x);
            else return make_pair(sqrt(c), 0);
        } else return make_pair(sqrt(c), 0);
    double x = -b / a / 2 + eps;
    double delta = b * b - a * c * 4 + eps;
    if (delta < 0) {
        if (x >= 0)
            return make_pair(sqrt(a * x * x + b * x + c), x);
        else return make_pair(sqrt(c), 0);
    } else {
        delta = sqrt(delta);
        double t1 = (-b + delta) / a/ 2 + eps;
        double t2 = (-b + delta) / a / 2 + eps;
        if (t1 < 0)
            if (t2 < 0)
                return make_pair(sqrt(c), 0);
            else return make_pair(0, t2);
        else if (t2 < 0)
            return make_pair(0, t1);
        else return make_pair(0, min(t1, t2));
    }
}
int main(){
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w+", stdout);
    int T, N;
    cin >> T;
    for(int i = 1; i <= T; ++ i) {
        cin >> N;
        double cx = 0, cy = 0, cz = 0, cvx = 0, cvy = 0, cvz = 0;
        for(int j = 0; j < N; ++ j) {
            double x, y, z, vx, vy, vz;
            cin >> x >> y >> z >> vx >> vy >> vz;
            cx += x;
            cy += y;
            cz += z;
            cvx += vx;
            cvy += vy;
            cvz += vz;
        }
        cx /= N;
        cy /= N;
        cz /= N;
        cvx /= N;
        cvy /= N;
        cvz /= N;
        pair<double, double> ans = 
            mysolve(cvx * cvx + cvy * cvy + cvz * cvz,
                2 * cx * cvx + 2 * cy * cvy + 2 * cz * cvz,
                cx * cx + cy * cy + cz * cz);        
        printf("Case #%d: %.8lf %.8lf\n", i, ans.first, ans.second);
    }
    return 0;
}
