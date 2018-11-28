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

#define CIN_FILE "input.txt"
#define COUT_FILE "output.txt"

#define forn(i, n) for(int i = 0; i < int(n); i++)
#define for1(i, n) for(int i = 1; i <= int(n); i++)
#define forv(i, v) forn(i, v.size())

#define pb push_back
#define mp make_pair
#define all(v) v.begin(), v.end()

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

#define DMAX 5005
#define LMAX 20

string s[DMAX];
int n, l, d;
bool a[LMAX][128];

int main()
{
    freopen(CIN_FILE, "rt", stdin);
    freopen(COUT_FILE, "wt", stdout);
    cin >> l >> d >> n;
    forn(i, d)
    {
        cin >> s[i];
    }

    string t;
    forn(i, n)
    {
        cin >> t;
        memset(a, 0, sizeof(a));
        forn(j, l)
        {
            if (t[0] == '(')
            {                
                int p = t.find(')');
                for (int k = 1; k < p; k++)
                {
                    a[j][t[k]] = true;
                }
                t.erase(0, p + 1);
            }
            else
            {
                a[j][t[0]] = true;
                t.erase(0, 1);            
            }
        }        

        int cnt = 0;
        forn(j, d)
        {
            bool ok = true;
            forn(k, l)
            {
                if (!a[k][s[j][k]])
                {
                    ok = false;
                    break;
                }
            }
            if (ok) ++cnt;
        }

        printf("Case #%d: %d\n", i + 1, cnt);
    }
    return 0;
}
            
