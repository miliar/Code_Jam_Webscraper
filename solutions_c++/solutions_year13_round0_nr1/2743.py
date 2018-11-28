// -*- C++ -*-
// File: tictactoetomek.cpp
// Copyright (C) 2013
#include <algorithm>
#include <string>
#include <vector>
#include <queue>
#include <iostream>
#include <cmath>
#include <sstream>
#include <map>
#include <set>
#include <numeric>
#include <memory.h>
#include <cstdio>
#include <assert.h>

using namespace std;

#define pb push_back
#define INF 1011111111
#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++)
#define rep(i,n) FOR(i,0,n)
#define CL(a,v) memset((a),(v),sizeof(a))
#define mp make_pair
#define X first
#define Y second
#define all(c) (c).begin(), (c).end()
#define SORT(c) sort(all(c))

typedef long long ll;
typedef vector<int> VI;
typedef pair<int,int> pii;

/*** TEMPLATE CODE ENDS HERE */

bool check_winer(string s[4], char C) {
    bool yep = true;

    // check rows
    rep(i,4) {
        yep = true;
        rep(j,4) yep &= s[i][j] == C || s[i][j] == 'T';
        if(yep) return true;
    }
    // check columns
    rep(j,4) {
        yep = true;
        rep(i,4) yep &= s[i][j] == C || s[i][j] == 'T';
        if(yep) return true;
    }
    // check diagonals
    {
        yep = true;
        rep(i,4) yep &= s[i][i] == C || s[i][i] == 'T';
        if(yep) return true;

        yep = true;
        rep(i,4) yep &= s[i][3-i] == C || s[i][3-i] == 'T';
        if(yep) return true;
    }
    return false;
}

bool is_complete(string s[4]) {
    rep(i,4) rep(j,4) if(s[i][j]=='.') return false;
    return true;
}

int main() {
#ifdef LOCAL_HOST
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
#endif

    ios_base::sync_with_stdio(false);

    int T;
    cin >> T;

    string s[4];

    FOR(cs,1,T+1) {
        rep(i,4) cin >> s[i];
        string res = "";

        if(check_winer(s, 'X') && check_winer(s, 'O')) {
            cout << "Conflict in given data\n";
            assert(false);
        }

        if(check_winer(s, 'X')) {
            res = "X won";
        }
        else if(check_winer(s, 'O')) {
            res = "O won";
        }
        else if(is_complete(s)) {
            res = "Draw";
        }
        else {
            res = "Game has not completed";
        }

        cout << "Case #" << cs << ": " << res << endl;
    }

// #ifdef LOCAL_HOST
//     printf("TIME: %.3lf\n",double(clock())/CLOCKS_PER_SEC);
// #endif

    return 0;
}
