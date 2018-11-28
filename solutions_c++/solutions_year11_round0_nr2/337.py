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

#define NMAX 255

char comb[NMAX][NMAX];
bool op[NMAX][NMAX];

void output(string& s)
{
    printf("[");

    forv(i, s)
    {
        if (i) printf(", ");
        printf("%c", s[i]);
    }

    printf("]\n");
}
void solve(int test)
{
    printf("Case #%d: ", test);

    memset(comb, 0, sizeof(comb));
    memset(op, 0, sizeof(op));

    int c, d, n;

    cin >> c;
    forn(i, c)
    {
        string tmp;
        cin >> tmp;
        comb[tmp[1]][tmp[0]] = comb[tmp[0]][tmp[1]] = tmp[2];
    }

    cin >> d;
    forn(i, d)
    {   
        string tmp;
        cin >> tmp;
        op[tmp[0]][tmp[1]] = op[tmp[1]][tmp[0]] = true;
    }
    cin >> n;
    string s; cin >> s;

    string res = "";

    forn(i, n)
    {
        if (res != "" && comb[res[res.size() - 1]][s[i]])
        {
            res[res.size() - 1] = comb[res[res.size() - 1]][s[i]];
        }
        else
        {
            bool cl = false;
            forv(j, res)
            {
                if (op[res[j]][s[i]])
                {
                    cl = true;
                    break;
                }
            }
            if (cl)
            {
                res.clear();
            }
            else
            {
                res += s[i];
            }
        }   
    }

    output(res);
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