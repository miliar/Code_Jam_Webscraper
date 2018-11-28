#include <stdio.h>
#include <assert.h>

#include <string>
#include <algorithm>
#include <iostream>
#include <vector>
typedef unsigned int uint;
using namespace std;


struct trecord {
    trecord(bool _arrive, int m) : arrive(_arrive), mins(m) {};
    int mins;       // minutes
    bool arrive;    // arrive or departure
};

typedef vector<trecord> TV;

int to_mins(const string& s) {
    int h, m;
    sscanf(s.c_str(), "%02d:%02d", &h, &m);
    return 60*h + m;
}

bool cmp(const trecord& l, const trecord& r) {
    if (l.mins == r.mins) {
        if (l.arrive && !r.arrive) return true;
        if (!l.arrive && r.arrive) return false;
        return &l < &r;
    }
    return l.mins < r.mins;
}

int solve(TV& tv) {
    int avail = 0;
    int need = 0;

    for (uint i=0; i<tv.size(); i++) {
        if (tv[i].arrive) {
            ++avail;
        }
        else {
            if (avail==0) {
                ++need;
            }
            else {
                --avail;
            }
        }
    }

    return need;
}

void main(int argc, char** argv) {

    string str;
    int CASES = 0;
    cin >> CASES;   getline(cin, str);

    for (int ncase=0; ncase<CASES; ncase++) {
        int T;  cin >> T;   getline(cin, str);
        int NA;  cin >> NA;
        int NB;  cin >> NB;   getline(cin, str);
        TV a;
        TV b;
        for (int i=0; i<NA; i++) {
            getline(cin, str, ' ');
            // departure from A
            trecord t0(false, to_mins(str));
            a.push_back(t0);
            // arrive to B
            getline(cin, str);
            trecord t1(true, to_mins(str) + T);
            b.push_back(t1);
        }

        for (int i=0; i<NB; i++) {
            getline(cin, str, ' ');
            // departure from B
            trecord t0(false, to_mins(str));
            b.push_back(t0);
            // arrive to A
            getline(cin, str);
            trecord t1(true, to_mins(str) + T);
            a.push_back(t1);
        }

        sort(a.begin(), a.end(), cmp);
        sort(b.begin(), b.end(), cmp);

        int na = solve(a);
        int nb = solve(b);

        printf("Case #%i: %d %d\n", ncase+1, na, nb);
    }
    return;
}

