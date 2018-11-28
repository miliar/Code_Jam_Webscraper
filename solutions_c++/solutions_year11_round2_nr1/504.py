#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <cfloat>
#include <climits>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <functional>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>

using namespace std;

//#define NDEBUG

#if defined(NDEBUG)
#define DBG_CODE(cb...)
#else
#define DBG_CODE(cb...) cb
#endif

#define WRITE(x) DBG_CODE(cout << x << endl)
#define WATCH(x) DBG_CODE(cout << #x << "=" << x << endl)

//[a, b) incrementando
#define FORN(i, a, b) for(typeof(b) i = (a); i < (b); i++)
//(a, b] decrementando
#define FORR(i, a, b) for(typeof(a) i = (a) - 1; i >= (b) && i < (a) ; i--)

#define ALL(x) x.begin(), x.end()
#define FOREACH(i, c) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define FOREACHR(i, c) for(typeof((c).rbegin()) i = (c).rbegin(); i != (c).rend(); i++)

char table[100][100];
bool flag[100];
int n;

double WP(int team)
{
    int total = 0;
    int n_wins = 0;
    FORN(i, 0, n){
        if(table[team][i] != '.' and flag[i]){
            total++;
            if(table[team][i] == '1') n_wins++;
        }
    }

    return ((double)n_wins) / ((double)total);
}

double OWP(int team)
{
    flag[team] = false;
    double sum = 0.0;
    int counter = 0;

    FORN(i, 0, n){
        if(table[team][i] != '.'){
            sum += WP(i);
            counter++;
        }
    }

    flag[team] = true;

    return sum / ((double)counter);
}

double OOWP(int team)
{
    double sum = 0.0;
    int counter = 0;

    FORN(i, 0, n){
        if(table[team][i] != '.'){
            sum += OWP(i);
            counter++;
        }
    }

    return sum / ((double)counter);
}

double RPI(int team)
{
    return WP(team) / 4.0 + OWP(team) / 2.0 + OOWP(team) / 4.0;
}

int main()
{
    int NTC;
    scanf("%d", &NTC);
    FORN(TC, 0, NTC){
        scanf("%d", &n);
        FORN(i, 0, n){
            scanf("%*[ \t\n]");
            FORN(j, 0, n){
                table[i][j] = getchar();
            }
        }

        FORN(i, 0, n){
            flag[i] = true;
        }

        printf("Case #%d:\n", TC + 1);
        FORN(i, 0, n){
            printf("%lf\n", RPI(i));
        }

    }
}
