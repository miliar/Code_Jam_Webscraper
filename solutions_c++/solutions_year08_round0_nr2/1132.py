#include <cstdio>

#include <map>
#include <algorithm>
#include <string>
#include <set>

using namespace std;

int read_time()
{
    char buf[128];
    int h, m;
    scanf ("%d:%d", &h, &m);
    return h*60 + m;
}

struct train {
    int type;
    int depart, arrive;

    const bool operator < (const train& oth) const {
        return depart < oth.depart || (depart == oth.depart && arrive < oth.arrive);
    }
};

train trains[256];
multiset<int> available[2];

void solve_one(int T)
{
    int turn_around, N, a, b, i, j, k;
    int sol[2];
    scanf ("%d %d %d", &turn_around, &a, &b);

    N = a + b;

    for (i = 0; i < N; i++) {
        trains[i].type = i < a ? 0 : 1;
        trains[i].depart = read_time();
        trains[i].arrive = read_time()  + turn_around;
    }
    
    sort (trains, trains + N);

    available[0].clear();
    available[1].clear();
    sol[0] = sol[1] = 0;

    for (i = 0; i < N; i++) {
        const int type = trains[i].type;
        // printf ("%d %d %d\n", trains[i].type, trains[i].depart, trains[i].arrive);
        if (! available[type].empty() && (*available[type].begin()) <= trains[i].depart) {
            available[type].erase(available[type].begin());
        } else {
            sol[type] ++;
        }
        available[1 - type].insert(trains[i].arrive);
    }


    printf ("Case #%d: %d %d\n", T, sol[0], sol[1]);
}

int main()
{
    int N, i;
    scanf ("%d", &N);

    for (i = 1; i <= N; i++)
        solve_one(i);

    return 0;
}

