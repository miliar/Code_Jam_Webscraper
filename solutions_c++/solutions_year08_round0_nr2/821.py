#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <map>
#include <queue>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

int _a;

#define FOR(i , n) for(int i = 0 ; i < n ; i++)
#define FOT(i , a , b) for(int i = a ; i < b ; i++)
#define GETINT (scanf("%d" , &_a) , _a)
#define pb push_back
#define mp make_pair
#define s(a) (int(a.size()))
#define PRINT(a) cerr << #a << " = " << a << endl

typedef long long ll;
typedef long double ld;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int , int> PII;


vector< PII > at, bt;


void go(vector< PII > &first, vector< PII > &next, int index)
{
    //cerr << first[index].first << ' ' << first[index].second << endl;
    int end = first[index].second;
    first.erase(first.begin() + index);

    FOR(i, next.size()) {
        if(next[i].first >= end) {
            go(next, first, i);
            break;
        }
    }
    return;
}


int main() {
    int cases = GETINT;
    FOT(t, 1, cases + 1) {
        int turn = GETINT;
        int na = GETINT;
        int nb = GETINT;
        int as, bs;
        as = bs = 0;
        at.clear();
        bt.clear();

        FOR(i, na + nb) {
            int dh, dm, ah, am;
            char _c;
            scanf("%d%c%d %d%c%d", &dh, &_c, &dm, &ah, &_c, &am);
            if (i < na) at.pb(mp(dh * 60 + dm, ah * 60 + am + turn));
            else bt.pb(mp(dh * 60 + dm, ah * 60 + am + turn));
        }
        sort(at.begin(), at.end());
        sort(bt.begin(), bt.end());
        int tota, totb;
        tota = totb = 0;
        while(s(at) > 0 || s(bt) > 0) {
            int what = -1, least = 100000000;
            if(s(at) > 0) what = 0, least = at[0].first;
            if(s(bt) > 0 && bt[0].first < least) what = 1, least = bt[0].first;
            if(what == 0) tota++, go(at, bt, 0);
            if(what == 1) totb++, go(bt, at, 0);
        }
        printf("Case #%d: %d %d\n", t, tota, totb);
    }
    return 0;
}
