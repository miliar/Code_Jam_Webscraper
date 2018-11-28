#include <iostream>
#include <iomanip>
#include <algorithm>
#include <map>
#include <cmath>
#include <vector>

using namespace std;

int fun(int a, int b, int c)
{
    double t = (double) b / a;
    if(t <= c) return 0;
    long long m = (long long)(a) * b;
    m = (long long)(sqrt(m) + 0.5);
    if(m <= 0) m = 1;
    int t1 = fun(a, m, c) + 1;
    int t2 = fun(m, b, c) + 1;
    if(t1 > t2) return t1;
    else return t2;
}

int main(int argc, char *argv[])
{
    int T;
    cin >> T;
    int a, b, c;
    for(int ci = 1; ci <= T; ci++)
    {
        cin >> a >> b >> c;
        cout << "Case #" << ci << ": " << fun(a, b, c) << endl;
    }
    return 0;
}
