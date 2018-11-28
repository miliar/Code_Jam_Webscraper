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

struct Rec
{
    int l, p, id;    
};

bool Cmp(const Rec& r1, const Rec& r2)
{
    return r1.l * r2.p < r1.p * r2.l;
}
void solve(int test)
{
    printf("Case #%d: ", test);

    int n;
    cin >> n;

    vector<Rec> v(n); 
    forn(i, n)
    {
        cin >> v[i].l;
    }
    forn(i, n)
    {
        cin >> v[i].p;
        v[i].id = i;
    }

    sort(all(v), Cmp);

    forv(i, v)
    {
        if (i) cout << " ";
        cout << v[i].id;
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