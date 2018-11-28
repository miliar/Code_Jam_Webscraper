#include <string.h>
#include <iostream>
#include <cstdio>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <cmath>
#include <string>
#include <map>
#include <cassert>
#include <queue>

using namespace std;

#define forn(i, n)  for (int i = 0; i < int(n); i++)

int n;
vector<int> p;

void read()
{
    cin >> n;
    p.resize(n);
    forn(i, n)
    {
        cin >> p[i];
        p[i]--;
    }
}

void process()
{
    vector<int> g(n, 0);
    int sum = 0;
    int cg = 0;
    forn(i, n)
    {
        if (g[i] == 0)
        {
            cg++;
            int j = i;
            int ss = 0;
            while (g[j] == 0)
            {
                g[j] = cg;
                j = p[j];
                ss++;
            }
            if (ss > 1)
                sum += ss;
        }
    }
    printf("%.6lf\n", double(sum));
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

