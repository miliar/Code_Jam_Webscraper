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

string code = "yhesocvxduiglbkrztnwjpfmaq";

void solve(int test)
{
    printf("Case #%d: ", test);

    string s;
    getline(cin, s);

    forv(i, s)
    {
        if (s[i] >= 'a' && s[i] <= 'z')
        {
            s[i] = code[s[i] - 'a'];
        }
    }
    puts(s.c_str());
}

void temp()
{
    string s1 = "", s2 = "", s;
    forn(i, 3)
    {
        getline(cin, s);
        forv(j, s)
        {
            if (s[j] != ' ') s1 += s[j];    
        }
    }
    forn(i, 3)
    {
        getline(cin, s);
        forv(j, s)
        {
            if (s[j] != ' ') s2 += s[j];    
        }
    }

    string cor(26, '?');

    forv(i, s1)
    {
        cor[s1[i] - 'a'] = s2[i];            
    }

    forn(i, 26)
    {
        cout << char('a' + i);
    }
    cout << endl;
    cout << cor << endl;
}

int main()
{
    freopen(CIN_FILE, "rt", stdin);
    freopen(COUT_FILE, "wt", stdout);

//    temp();
    int tc;
    scanf("%d\n", &tc);
    forn(it, tc) solve(it + 1);
    
    return 0;
}