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

struct event
{
    int who, pos;
};

int n;
vector<event> events;

void read()
{
    events.clear();
    cin >> n;
    forn(i, n)
    {
        string t;
        cin >> t;
        event e = {t == "B" ? 1 : 0, 0};
        cin >> e.pos;
        events.push_back(e);
    }
}

void process()
{
    int t[2] = {0, 0};
    int p[2] = {1, 1};

    forn(i, n)
    {
        int nt = t[events[i].who] + abs(p[events[i].who] - events[i].pos) + 1;
        t[events[i].who] = max(nt, t[events[i].who ^ 1] + 1);
        p[events[i].who] = events[i].pos;
    }

    cout << max(t[0], t[1]) << endl;
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

