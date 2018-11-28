#pragma comment(linker, "/STACK:64000000")
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <cmath>
#include <stack>
#include <sstream>
#include <cassert>
#include <cstdlib>
#include <queue>
using namespace std;

#define forn(i, n) for(int i = 0; i < int(n); i++) 
#define forv(i, v) forn(i, v.size())
#define for1(i, n) for(int i = 1; i <= int(n); i++)
#define all(v) v.begin(), v.end()
#define mp make_pair
#define pb push_back

struct Node {
    int time, type;
    int where;
};

vector<Node> v;

int getTime(string s) {
    int h = (s[0] - '0') * 10 + s[1]-'0';
    int m = (s[3] - '0') * 10 + s[4] - '0';
    return h * 60 + m;
}


bool Cmp(const Node &a, const Node &b) {
    return a.time < b.time || (a.time == b.time && a.type < b.type);
}

bool can(int x, int y) {
    forv(i, v) {
        if (!v[i].where) {
            if (v[i].type) {
                if (x == 0) return false;
                x--;
            } else {
                x++;
            }
        } else {
            if (v[i].type) {
                if (y == 0) return false;
                y--;
            } else {
                y++;
            }
        }

    }
    return true;
}

int main() {
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);

    int tc;
    scanf("%d\n", &tc);
    forn(it, tc) {
        int na, nb;
        int st;
        string s;
        getline(cin, s);
        st = atoi(s.c_str());

        getline(cin, s);
        na = atoi(s.substr(0, s.find(" ")).c_str());
        s.erase(0, s.find(" ") + 1);
        nb = atoi(s.c_str());

        Node t;
        v.clear();
        forn(i, na) {
            getline(cin, s);
            t.time = getTime(s.substr(0, s.find(" ")));
            t.type = 1;
            t.where = 0;
            v.pb(t);
            s.erase(0, s.find(" ") + 1);
            while (s.length() && s[0] == ' ') s.erase(0, 1);
            t.time = getTime(s) + st;
            t.type = 0;
            t.where = 1;
            v.pb(t);
        }
        forn(i, nb) {
            getline(cin, s);
            t.time = getTime(s.substr(0, s.find(" ")));
            t.type = 1;
            t.where = 1;
            v.pb(t);
            s.erase(0, s.find(" ") + 1);
            while (s.length() && s[0] == ' ') s.erase(0, 1);
            t.time = getTime(s) + st;
            t.type = 0;
            t.where = 0;
            v.pb(t);
        }

        sort(all(v), Cmp);


        int x, y;
        x = 100, y = 100;

        forn(i, na + 1) {
            forn(j, nb + 1) {
                if (can(i, j) && i + j < x + y) {
                    x = i;
                    y = j;
                }                
            }
        }

//        cout << "/////" << endl;
//        cout << (int)can(2, 2) << endl;

        printf("Case #%d: %d %d\n", it + 1, x, y);
    }


    return 0;
}
