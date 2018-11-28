#include <iostream>
#include <string>
#include <iomanip>
#include <cmath>

#define REP(i, a, b) for(i = a; i < b; i++)
#define rep(i, n) REP(i, 0, n)
#define REPD(i, a, b) for(i = a; i > b; i--)
#define repd(i, n) REPD(i, n, 0)
#define UTL(i, a, b) for(i = a; i <= b; i++)
#define utl(i, n) UTL(i, 1, n)
#define UTLD(i, a, b) for(i = a; i >= b; i--)
#define utld(i, n) UTLD(i, n, 1)

using namespace std;

int main()
{
    freopen("data.in", "r", stdin);
    freopen("data.out", "w", stdout);

    int n, in;
    int num, i, j;

    double x, y, z;
    double vx, vy, vz;

    double tmp;

    double a, b, c;

    double md;
    double mt;

    double dlt;

    cin >> n;

    utl(in, n) {
        cin >> num;
        x = 0;
        y = 0;
        z = 0;
        vx = 0;
        vy = 0;
        vz = 0;
        rep(i, num) {
            cin >> tmp;
            x += tmp;
            cin >> tmp;
            y += tmp;
            cin >> tmp;
            z += tmp;
            cin >> tmp;
            vx += tmp;
            cin >> tmp;
            vy += tmp;
            cin >> tmp;
            vz += tmp;
        }
        x /= num;
        y /= num;
        z /= num;
        vx /= num;
        vy /= num;
        vz /= num;

        a = vx * vx + vy * vy + vz * vz;
        b = 2 * (x * vx + y * vy + z * vz);
        c = x * x + y * y + z * z;

        //cout << a << " " << b << " " << c << endl;

        if(a == 0) {
            mt = 0;
        } else {
            mt = - (b / (a * 2));
            if(mt < 0) mt = 0;
        }

        md = a * mt * mt + b * mt + c;

        cout << fixed;
        cout << "Case #" << in << ": " << setprecision(8) << sqrt(abs(md)) << " " << mt << endl;
    }

    return 0;
}
