/*
    Title:
    Author: RudySnow
    Algorithm:
    Date:
    License:
    Quote: Night Gathers, and My Watch Begins, it shall Never End until My Death
*/

#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <memory.h>
#include <cstring>
#include <cmath>
#include <ctime>
#include <algorithm>
#include <set>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>

using namespace std;

void Solve()
{
    char hs[] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i',
    'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};
    int test;
    string str;
    int cas = 1;
    for (cin >> test, getchar(); test--; ++cas)
    {
        getline(cin, str);
        cout << "Case #" << cas << ": ";
        for (int i = 0; i < static_cast<int>(str.length()); ++i)
        {
            if ('a' <= str[i] && str[i] <= 'z')
            {
                cout << hs[static_cast<int>(str[i]) - 'a'];
            }
            else
            {
                cout << str[i];
            }
        }
        cout << endl;
    }

    return ;
}
int main()
{
    freopen("A-small-attempt4.in", "r", stdin);
    freopen("A-small-attempt4.out", "w", stdout);
    Solve();
    return 1;
}
