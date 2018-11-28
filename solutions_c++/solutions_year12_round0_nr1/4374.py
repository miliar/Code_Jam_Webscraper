// Template begins

#pragma comment (linker, "/STACK:214721677")
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <math.h>
#include <string.h>
#include <stdlib.h>

#include <iostream>
#include <algorithm>
#include <vector>
#include <deque>
#include <list>
#include <set>
#include <map>
#include <bitset>
#include <string>
#include <ctime>

using namespace std;

#define REP(i,n) for (int i=0, _n=(n)-1; i <= _n; ++i)
#define REPD(i,n) for (int i=(n)-1; i >= 0; --i)
#define FOR(i,a,b) for (int i=(a), _b=(b); i <= _b; ++i)
#define FORD(i,a,b) for (int i=(a), _b=(b); i >= _b; --i)
#define X first
#define Y second
#define pb push_back
#define mp make_pair
#define sz(a) ((int) ((a).size()))
template < class T > T sqr (T a) { return (a) * (a); }
template < class T > T abs (T a) { return (a < 0) ? -(a) : (a); }
const double Pi = acos(-1.0);
const double eps = 1e-10;
const int INF = 1000*1000*1000;
const double phi = 0.5 + sqrt(1.25);
typedef long long ll;
typedef pair <int, int> pii;
typedef pair <double, double> pdd;

// Template ends

struct comp {
    bool operator () (pair<ll, int> a, pair<ll, int> b) {
        return a.Y < b.Y;
    }
} myComp;

struct comp2 {
    bool operator () (pii a, pii b) {
        return a.X > b.X;
    }
} byF;

struct comp3 {
    bool operator () (pii a, pii b) {
        return a.Y < b.Y;
    }
} byId;

int main() {
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    int T;
    string in  = " abcdefghijklmnopqrstuvwxyz";
    string out = " yhesocvxduiglbkrztnwjpfmaq";

    scanf("%d\n", &T);
    REP(i, T) {
        string s;
        getline(cin, s);

        string toPrint = "";
        REP(j, sz(s)) {
            int id = in.find(s[j]);
            toPrint += out[id];
        }

        printf("Case #%d: ",i + 1);
        cout <<  toPrint << "\n";

    }
    return 0;
}