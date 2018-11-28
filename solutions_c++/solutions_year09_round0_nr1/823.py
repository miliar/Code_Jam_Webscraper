#pragma comment(linker, "/STACK:64000000")
#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <cmath>
#include <cstdio>
#include <cassert>
#include <string>
#include <queue>
#include <stack>
#include <deque>
#include <numeric>
#include <sstream>
#include <ctime>

using namespace std;

#define CIN_FILE "a.in"
#define COUT_FILE "a.out"

#define forn(i, n) for(int i = 0; i < int(n); i++)
#define for1(i, n) for(int i = 1; i <= int(n); i++)
#define forv(i, v) forn(i, v.size())

#define pb push_back
#define mp make_pair
#define all(v) v.begin(), v.end()

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
const int LMAX = 20;
const int NMAX = 5006;
string w[NMAX];
int nw;
bool us[LMAX][26];


int main()
{
    freopen(CIN_FILE, "rt", stdin);
    freopen(COUT_FILE, "wt", stdout);
    int m, L;
    scanf("%d %d %d\n", &L, &nw, &m);
    forn(i, nw)
    {
        getline(cin, w[i]);
    }
    forn(it, m)
    {
        string pat;
        memset(us, 0, sizeof(us));
        getline(cin, pat);
        int l = 0;
        forn(j, L)
        {
            if (isalpha(pat[l]))
            {
                us[j][pat[l]-'a'] = true;
                l++;
                continue;
            }            
            l++;
            int r = l;
            while (isalpha(pat[r]))
            {
                us[j][pat[r]-'a'] = true;
                r++;
            }
            l = r + 1;
        }
        int ans = 0;
        forn(i, nw)
        {
            bool ok = true;
            forn(j, L)
            {
                if (!us[j][w[i][j]-'a'])
                {
                    ok = false;
                    break;
                }
            }
            if (ok) ans++;
        }
        printf("Case #%d: %d\n", it+1, ans);
    }


    return 0;
}
            
