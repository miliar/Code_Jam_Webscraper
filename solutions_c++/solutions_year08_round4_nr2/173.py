#include <vector>
#include <string>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <ctime>
#include <algorithm>
#include <map>
#include <utility>

using namespace std;

int gcd(int a, int b)
{
    if (b == 0) return a;
    return gcd(b, a % b);
}

int main(int argc, char **argv)
{
    int NNNNN;
    cin >> NNNNN;
    for (int cccccc=1;cccccc<=NNNNN;++cccccc)
    {
        cout << "Case #" << cccccc << ": ";
        
        // CODE
        int A, M, N;
        cin >> N >> M >> A;
        if (A>N*M) {cout << "IMPOSSIBLE" << endl; continue;}
        bool ok = false;
        for (int x1=1;x1<=N;++x1)
        {
            if (A % x1 == 0 && A / x1 <= M)
            {
                cout << "0 0 0 " << A/x1 << " " << x1 << " 0" << endl;
                ok = true;
                break;
            }
            for (int y2=A / x1 + 1;y2<=M;++y2)
            {
                int full = x1 * y2 - A;
                for (int y1=1;y1<=sqrt((double)full)+0.1 && y1 <= y2;++y1)
                {
                    if (full % y1 == 0 && full / y1 <= x1)
                    {
                        cout << "0 0 " << x1 << " " << y1 << " " << full / y1 << " " << y2 << endl;
                        ok = true;
                        break;
                    }
                }
                if (ok) break;
            }
            if (ok) break;
        }
        if (!ok) cout << "IMPOSSIBLE" << endl;
        // END OF CODE
    }
    return 0;
}