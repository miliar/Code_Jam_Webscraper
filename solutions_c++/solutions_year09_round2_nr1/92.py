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
typedef long double ld;
typedef pair<int, int> pii;

struct Node
{
    int pr;
    int l, r;
    string f;
    double w;
};

#define VMAX 10000

int n;
Node t[VMAX];
int kv;


void solve(int tc)
{
    printf("Case #%d:\n", tc);
    int l;
    scanf("%d\n", &l);

    string s = "";
    forn(it, l)
    {
        string t;
        getline(cin, t);
        s += " " + t;    
    }

    string str = "";
    forv(i, s)
    {
        if (s[i] == ')' || s[i] == '(')
        {
            str += " ";
            str += s[i];
            str += " ";
        }        
        else
        {
            str += s[i];
        }
    }

    istringstream ssin(str);

    forn(i, VMAX)
    {
        t[i].pr = t[i].l = t[i].r = -1;
        t[i].f = "";
        t[i].w = 0;
    }

    kv = 0;

    int cur = -1;

    while (ssin >> s)
    {
        if (s == "(")
        {
            t[kv].pr = cur;
            ssin >> t[kv].w;

            if (cur != -1)
            {
                if (t[cur].l == -1)
                {
                    t[cur].l = kv;
                }
                else
                {
                    t[cur].r = kv;
                }
            }
            
            ssin >> s;

            if (s != ")")
            {
                t[kv].f = s;
                cur = kv;                               
            }

			kv++; 
        }
        else
        if (s == ")")
        {
            cur = t[cur].pr;
        }
    }

    scanf("%d\n", &n);

    forn(i, n)
    {
        getline(cin, s);
        istringstream ssin(s);

		ssin >> str;

        int k;
        ssin >> k;
        set<string> f;

        while (ssin >> str)
        {
            f.insert(str);
        }

        assert((int)f.size() == k);

        int cur = 0;

        double p = 1;

        while (true)
        {
            p *= t[cur].w;
			if (t[cur].f == "") break;
            if (f.count(t[cur].f)) cur = t[cur].l; else cur = t[cur].r;                        			
        }
        
        printf("%.8lf\n", p);
    }
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
            
