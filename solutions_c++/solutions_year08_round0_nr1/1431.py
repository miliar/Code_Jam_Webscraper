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

const int NMAX = 105;
const int INF = 1000000;

int d[NMAX][10 * NMAX];

string name[NMAX];
string query[NMAX * 10];


int main() {
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);

    int n, m, tc;
    scanf("%d\n", &tc);
    string s;
    forn(it, tc) {
        getline(cin, s);
        n = atoi(s.c_str());
        forn(i, n) {
            getline(cin, name[i]);
        }
        getline(cin, s);
        m = atoi(s.c_str());
        forn(i, m) {
            getline(cin, query[i]);
        }
        if (m == 0) {
            printf("Case #%d: %d\n", it+1, 0);
            continue;
        }

        forn(i, n) {
            forn(j, m) d[i][j] = INF;
        }
        forn(i, n) {
            if (name[i] != query[0]) d[i][0] = 0;
        }

        for1(j, m-1) {
            forn(i, n) {
                if (d[i][j-1] == INF) continue;
                if (name[i] == query[j]) {
                    forn(k, n) {
                        if (k == i) continue;
                        d[k][j] = min(d[k][j], d[i][j-1]+1);
                    }                    
                } else {
                    d[i][j] = min(d[i][j-1], d[i][j]);
                }
            }
        }

        int ans = INF;
        forn(i, n) {
            ans = min(ans, d[i][m-1]);            
        }

        printf("Case #%d: %d\n", it+1, ans);
    }


    return 0;
}
