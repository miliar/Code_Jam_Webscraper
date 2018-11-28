#pragma comment(linker, "/STACK:64000000")
#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <cmath>
#include <cassert>
#include <sstream>

using namespace std;

#define forn(i, n) for (int i = 0; i < int(n); i++)
#define for1(i, n) for (int i = 1; i <= int(n); i++)
#define forv(i, v) forn(i, v.size())

#define all(x) x.begin(), x.end()
#define pb push_back
#define mp make_pair

#define CIN_FILE "input.txt"
#define COUT_FILE "output.txt"

typedef long double ld;
typedef long long ll;
typedef pair<int, int> pii;

#define NMAX 10004
#define ALP 26

struct Word
{
    int id;
    string g;
    int moves;
};

struct Group
{
    int l, r;
    char can[ALP];
};


int n, m;
string s[NMAX];
Word w[NMAX];
string alp;

Group g[NMAX];

bool Cmp(const Word& w1, const Word& w2)
{   
    if (w1.g != w2.g) return w1.g < w2.g;
    return w1.id < w2.id;
}

string find_best()
{      
    forn(i, n)
    {
        w[i].id = i;
        w[i].g = "";
        forv(j, s[i]) w[i].g += '?';
        w[i].moves = 0;
    }

    forv(i, alp)
    {        
        sort(w, w + n, Cmp);

        int cg = 0;

        int l = 0;
        while (l < n)
        {
            int r = l;
            while (r < n && w[l].g == w[r].g) r++;

            g[cg].l = l;
            g[cg].r = r;
            memset(g[cg].can, 0, sizeof(g[cg].can));

            for (int j = l; j < r; j++)
            {
                int k = w[j].id;
                forv(t, s[k])
                {
                    g[cg].can[s[k][t] - 'a'] = true;
                }
            }

            cg++;
            l = r;
        }

        forn(j1, cg)
        {
            if (!g[j1].can[alp[i] - 'a']) continue;

            for (int j = g[j1].l; j < g[j1].r; j++)
            {
                int k = w[j].id;
                bool f = false;
                forv(t, s[k])
                {
                    if (s[k][t] == alp[i])
                    {
                        w[j].g[t] = alp[i];
                        f = true;
                    }    
                }
                if (!f) w[j].moves++;
            }
        }

    }

    int best = 0;

    forn(i, n)
    {
        if (w[i].moves > w[best].moves ||
        (w[i].moves  == w[best].moves &&
        w[i].id < w[best].id))
        {
            best = i;
        }

    }

    return s[w[best].id];
}

void solve(int test)
{
    cerr << test << endl;
    printf("Case #%d: ", test);

    cin >> n >> m;
    forn(i, n) cin >> s[i];
    
    forn(j, m)
    {
        if (j) cout << " ";
        cin >> alp;
        cout << find_best();
    }
    cout << endl;
}

int main()
{
    freopen(CIN_FILE, "rt", stdin);
    freopen(COUT_FILE, "wt", stdout);

    int tc;
    scanf("%d\n", &tc);
    forn(it, tc) solve(it + 1);
    
    return 0;
}