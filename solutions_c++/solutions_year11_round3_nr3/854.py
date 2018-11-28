// C.cpp : Defines the entry point for the console application.
//


#include "stdafx.h"

#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string>
using namespace std;

typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;
typedef long long LL;

#define FOR(i,a,b) for(int i = (a); i < (b); i++)
#define REP(i,n) FOR(i,0,n)

int t;
int n;
LL l, h;
LL a;
vector<LL> vec;

int main()
{
    //freopen("1.in", "r", stdin);
    //freopen("1.out", "w", stdout);

    freopen("C-small-attempt0.in", "r", stdin);
    freopen("C-small-attempt0.out", "w", stdout);

    //freopen("C-large.in", "r", stdin);
    //freopen("C-large.out", "w", stdout);

    cin >> t;
    for (int cc = 1; cc <= t; cc++)
    {
        vec.clear();
        cin >> n >> l >> h;
        for (int i = 0; i < n; i++)
        {
            cin >> a;
            vec.push_back(a);
        }

        LL x;
        bool is_all_ok = false;
        for (x = l; x <= h; x++)
        {
            bool is_ok = true;
            for (int i = 0; i < n; i++)
            {
                if (x % vec[i] == 0 || vec[i] % x == 0)
                {
                }
                else
                {
                    is_ok = false;
                }
            }

            if (is_ok)
            {
                is_all_ok = true;
                break;
            }
        }

        cout << "Case #" << cc << ": ";
        if (is_all_ok)
            cout << x << endl;
        else
            cout << "NO" << endl;
    }

    return 0;
}


