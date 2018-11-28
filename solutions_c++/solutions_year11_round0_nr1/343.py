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


struct Button
{
    char r;
    int id;    
};

void move(int& pos, queue<int> q)
{
    if (q.empty()) return;

    if (q.front() < pos) pos--;
    else if (q.front() > pos) pos++;
}

void solve(int test)
{
    printf("Case #%d: ", test);

    int n;
    cin >> n;

    vector<Button> b(n);
    queue<int> bo;
    queue<int> bb;

    forn(i, n)
    {
        cin >> b[i].r >> b[i].id;
        b[i].id--;

        if (b[i].r == 'O') bo.push(b[i].id); else bb.push(b[i].id);
    }

    int bcur = 0, ocur = 0;

    int ans = 0;

    forv(i, b)
    {
        if (b[i].r == 'O')
        {
            while (ocur != b[i].id)
            {
                ans++;
                move(ocur, bo);
                move(bcur, bb);             
            }

            ans++;
            bo.pop();
            move(bcur, bb);
        }
        else
        {
            while (bcur != b[i].id)
            {
                ans++;
                move(ocur, bo);
                move(bcur, bb);             
            }
            ans++;
            bb.pop();
            move(ocur, bo);
        }
    } 

    cout << ans << endl;
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