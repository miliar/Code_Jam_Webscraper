#include <iostream>
#include <math.h>
#include <iomanip>
#define eps 1e-9
using namespace std;

double x[3], y[3], r[3];

double dist(double p1x, double p1y, double p2x, double p2y)
{
       return sqrt((p1x-p2x)*(p1x-p2x)+(p1y-p2y)*(p1y-p2y));
}
double solve2(int i, int j)
{
    double d = dist(x[i], y[i], x[j], y[j]);
    
    if (d + r[i] < r[j] + eps) return r[j];
    if (d + r[j] < r[i] + eps) return r[i];
    return (d + r[i] + r[j])/2.;
}
void solve()
{
     int N;
     cin >> N;
     
     for (int i = 0; i < N; i++) cin >> x[i] >> y[i] >> r[i];
     
     if (N == 1) cout << r[0] << endl;
     else if (N == 2) cout << max(r[0], r[1]) << endl;
     
    
     else cout <<  setiosflags(ios::fixed) << setprecision(6) <<
                       min( max(r[0], solve2(1, 2)),
                       min(
                        max(r[1], solve2(0, 2)),
                        max(r[2], solve2(0, 1)))) << endl; 
}
int main()
{
    int C;
    cin >> C;
    for (int i = 0; i < C; i++)
    {
        cout << "Case #" << i + 1 << ": ";
        solve();
    }
    return 0;
}
