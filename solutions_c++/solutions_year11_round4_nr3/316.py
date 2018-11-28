#include <cstring>
#include <iostream>
#include <cstdio>
#include <ctime>
#include <vector>
#include <set>
#include <string>
#include <map>
#include <cassert>
#include <queue>
#include <climits>
#include <cstdlib>
#include <algorithm>
#include <cmath>

using namespace std;

#define forn(i, n)  for (int i = 0; i < int(n); i++)

int n;

void read()
{
    cin >> n;
}

void process()
{
    int rmin = 0;
    map<int,int> p;

    int rmax = 1;
    for (int ix = 1; ix <= n; ix++)
    {
        int i = ix;
        bool up = false;

        int j = 2;
        while (j * j <= i)
        {
            int d = 0;
            while (i % j == 0)
            {
                i /= j;
                d++;
            }
            if (d > 0)
            {
                if (p[j] < d)
                    p[j] = d, up = true;
            }
            j++;
        }
        if (i == ix && i > 1)
            rmin++;
        if (i > 1)
        {
            if (p[i] < 1)
                p[i] = 1, up = true;
        }
        rmax += up;
    }

    rmin = max(rmin, 1);

    //cout << rmin << endl;
    //cout << rmax << endl;

    cout << rmax - rmin << endl;
}

int main(int argc, char* argv[])
{
    freopen("input.txt", "rt", stdin);
    
    int cases;
    scanf("%d", &cases);

    int from = (argc > 1 ? atoi(argv[1]) : 1);
    int to = (argc > 2 ? atoi(argv[2]) : cases);

    for (int i = 1; i <= cases; i++)
    {
        read();
        if (from <= i && i <= to)
        {
            printf("Case #%d: ", i);
            process();
        }
    }

    return 0;
}

