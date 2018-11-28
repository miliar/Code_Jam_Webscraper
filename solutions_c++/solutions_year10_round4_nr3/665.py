#define _CRT_SECURE_NO_WARNINGS
#include <algorithm>
#include <cctype>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <functional>
#include <iostream>
#include <fstream>
#include <map>
#include <set>
#include <stack>
#include <sstream>
#include <string>
#include <vector>
#include <queue>

using namespace std;
fstream inp, out;

const int oo = 0x3f3f3f3f;
const int R = 12;
const int N = 102;

int main(int argc, char *argv[])
{
    int lower = 0, upper = oo;
    if (argc < 2) { cout << "specify input/output" << endl; return 1;}
    if (argc >= 3) { sscanf(argv[2], "%d", &lower); }
    if (argc >= 4) { sscanf(argv[3], "%d", &upper); }
    char lowers[32];
    sprintf(lowers, "%07d", lower);
    string iname = string(argv[1]);
    string oname = iname.substr(0, iname.size() - 3) + string(".") + string(lowers) + string(".out");
    inp.open (iname.c_str(), fstream::in);
    out.open (oname.c_str(), fstream::out);
    int T;
    inp >> T;
    for (int cs = 1; cs <= T; ++cs)
    {
        int n;
        inp >> n;
        int x1[R], y1[R], x2[R], y2[R];
        for (int i = 0; i < n; ++i)
            inp >> x1[i] >> y1[i] >> x2[i] >> y2[i];
        if (lower <= cs && cs < upper)
        {
           int a[N+2][N+2];
           memset(a, 0, sizeof(a));
           int b[N+2][N+2];
           int c = 0;
           for (int i = 0; i < n; ++i)
           for (int x = x1[i]; x <= x2[i]; ++x)
           for (int y = y1[i]; y <= y2[i]; ++y)
                if (!a[x][y]) {a[x][y] = 1; c++;}
           int t = 0;
           for (t = 0; c > 0; ++t) {
                memset(b, 0, sizeof(b));
                c = 0;
                for (int x = 1; x <= N; ++x)
                for (int y = 1; y <= N; ++y)
                {
                    b[x][y] = a[x][y];
                    if (!a[x-1][y] && !a[x][y-1]) b[x][y] = 0;
                    if (a[x-1][y] && a[x][y-1]) b[x][y] = 1;
                    c += b[x][y];
                }

                memcpy(a, b, sizeof(a));
           }
           cout << "solved case " << cs << endl;
           out << "Case #" << cs << ": " << t << endl; 
        }
    }
    return 0;
}