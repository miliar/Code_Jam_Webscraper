#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <vector>
#include <algorithm>

using namespace std;

const int V = 256;

int c[V * V];
int c1[V * V];
int maxx, maxy, minx, miny;
int* pc1 = c;
int* pc2 = c1;

bool check()
{
    bool ret = false;
    for (int x = minx; x <= maxx; ++x)
    {
        for (int y = miny; y <= maxy; ++y)
            if (pc1[x * V + y])
            {
                if (!pc1[x*V+y-V] && !pc1[x*V+y-1])
                    pc2[x*V+y] = 0;
                else
                {
                    pc2[x*V+y] = 1;
                    ret = true;
                }
            }
            else if (pc1[x*V+y-V] && pc1[x*V+y-1])
            {
                pc2[x*V+y] = 1;
                ret = true;
            }
            else
                pc2[x*V+y] = 0;
    }
    int* pt = pc1;
    pc1 = pc2;
    pc2 = pt;
    return ret;
}

void main()
{
    ifstream fin("C-small.in");
    ofstream fout("A.out");
    int T;
    fin >> T;
    for (int tt = 1; tt <= T; ++tt)
    {
        int R;
        maxx = 0; maxy = 0;
        minx = miny = 0x7FFFFFFF;
        fin >> R;
        memset(c, 0, sizeof(c));
        memset(c1, 0, sizeof(c1));
        pc1 = c, pc2 = c1;
        for (int i = 0; i < R; ++i)
        {
            int x1, y1, x2, y2;
            fin >> x1 >> y1 >> x2 >> y2;
            if (x1 < minx) minx = x1;
            if (y1 < miny) miny = y1;
            if (x2 > maxx) maxx = x2;
            if (y2 > maxy) maxy = y2;
            for (int x = x1; x <= x2; ++x)
                for (int y = y1; y <= y2; ++y)
                    c[x * V + y] = 1;
        }
        int s = 1;
        while (check()) ++s;
        fout << "Case #" << tt << ": " << s << endl;
    }
    fout.close();
    fin.close();
}
