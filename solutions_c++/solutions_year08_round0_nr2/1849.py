#pragma comment(linker, "/STACK:1000000000")

#define _CRT_SECURE_NO_DEPRECATE

#include <cstdio>
#include <vector>
#include <algorithm>
#include <cmath>
#include <string>
#include <map>
#include <set>
#include <iostream>
#include <cstring>
#include <utility>
#include <memory>
#include <cstdlib>
#include <cctype>
#include <queue>
#include <sstream>

using namespace std;

#define forn(i, n) for(int i = 0; i < (int)(n); ++i)
#define forv(i, v) forn(i, v.size())
#define all(a) a.begin(), a.end()
#define pb push_back
#define mp make_pair
#define sqr(a) ((a) * (a))
#define two(n) (1 << (n))
#define has(mask, i) (((mask) & two(n)) != 0) ? true : false

typedef long long int64;

const double EPS = 1e-8;
const double PI = 3.1415926535897932384626433832795;
const int INF = 1000000000;

struct Time
{
    int h, m;

    Time(const string& time)
    {
        this->h = atoi(time.substr(0, 2).c_str());
        this->m = atoi(time.substr(3, 2).c_str());
    }

    Time(int time)
    {
        this->h = time / 60;
        this->m = time % 60;
    }

    Time(const Time& a)
    {
        this->h = a.h;
        this->m = a.m;
    }

    Time()
    {
    }
};

bool operator < (const Time& a, const Time& b)
{
    if (a.h != b.h)
        return a.h < b.h;

    return a.m < b.m;
}

Time operator + (const Time& a, const Time&b)
{
    Time result(a);

    result.m += b.m;

    result.h += result.m / 60;
    result.m = result.m % 60;

    return result;
}

struct Train
{
    Time departure, arrival, nextDeparture;

    Train(const string& departure, const string& arrival, const Time& turnaround)
    {
        this->departure = Time(departure);
        this->arrival = Time(arrival);
        this->nextDeparture = arrival + turnaround;
    }
};

bool operator < (const Train& a, const Train& b)
{
    return a.departure < b.departure;
}

vector<Train> trainsA, trainsB;

set<pair<Time, int> > a, b;
int resA, resB;

void solve()
{
    a.clear(), b.clear();
    resA = 0, resB = 0;

    forv(i, trainsA)
        a.insert(mp(trainsA[i].departure, i));

    forv(i, trainsB)
        b.insert(mp(trainsB[i].departure, i));

    while (!a.empty() && !b.empty())
    {
        pair<Time, int> cur;
        bool side;

        if (a.begin()->first < b.begin()->first)
        {
            cur = *a.begin();

            ++resA;
            a.erase(a.begin());

            side = false;
        }
        else
        {
            cur = *b.begin();

            ++resB;
            b.erase(b.begin());

            side = true;
        }

        while (true)
        {
            pair<Time, int> next;

            if (!side)
            {
                set<pair<Time, int> >::iterator it = b.lower_bound(mp(Time(trainsA[cur.second].nextDeparture), -1));
                if (it == b.end())
                    break;

                next = *it;
                b.erase(it);
            }
            else
            {
                set<pair<Time, int> >::iterator it = a.lower_bound(mp(Time(trainsB[cur.second].nextDeparture), -1));
                if (it == a.end())
                    break;

                next = *it;
                a.erase(it);
            }

            cur = next;
            side = !side;
        }
    }

    resA += a.size();
    resB += b.size();
}

char buf[100];

int main()
{
#ifdef _DEBUG
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
#endif

    int tests;
    scanf("%d", &tests);

    forn(test, tests)
    {
        int turnaround, na, nb;
        scanf("%d%d%d", &turnaround, &na, &nb);

        Time turnaroundTime(turnaround);

        trainsA.clear(), trainsB.clear();

        forn(i, na)
        {
            scanf("%s", buf);
            string departure = buf;
            scanf("%s", buf);
            string arrival = buf;

            trainsA.pb(Train(departure, arrival, turnaroundTime));
        }

        forn(i, nb)
        {
            scanf("%s", buf);
            string departure = buf;
            scanf("%s", buf);
            string arrival = buf;

            trainsB.pb(Train(departure, arrival, turnaroundTime));
        }

        solve();

        printf("Case #%d: %d %d\n", test + 1, resA, resB);
    }

    return 0;
}
