#include<iostream>
#include<vector>
#include<cmath>

using namespace std;
typedef unsigned int uint;



void test()
{
    uint  n;
    cin >> n;
    double x[3], y[3], r[3];
    for(uint i=0;i<n;++i)
        cin >> x[i] >> y[i] >> r[i];
    if(n == 1)
    {
        cout << r[0] << endl;
    }
    else if(n == 2)
    {
        cout << max(r[0], r[1]) << endl;
    }
    else
    {
        double a = sqrt((x[0]-x[1])*(x[0]-x[1]) + (y[0]-y[1])*(y[0]-y[1])) + r[0] + r[1];
        double b = sqrt((x[2]-x[1])*(x[2]-x[1]) + (y[2]-y[1])*(y[2]-y[1])) + r[2] + r[1];
        double c = sqrt((x[0]-x[2])*(x[0]-x[2]) + (y[0]-y[2])*(y[0]-y[2])) + r[0] + r[2];
        double z = max(a, r[2]);
        z = min(z, max(b, r[0]));
        z = min(z, max(c, r[1]));
        cout << z/2.0 << endl;
    }
}

int main()
{
    ios::sync_with_stdio(false);
    uint tno;
    cin >> tno;
    for(uint i=0;i<tno;++i)
    {
        cout << "Case #" << i+1 << ": ";
        test();
    }
    return 0;
}
