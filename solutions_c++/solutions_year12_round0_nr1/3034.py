#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>
#include <string>
#include <cstdlib>
#include <set>
#include <map>
#include <algorithm>
#include <ctime>
using namespace std;


#define forn(i, n) for(int i = 0; i < n; i++)

int t;
string g;
int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    string goog = "ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jvy qeez";
    string engl = "our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give upa zooq";
    cin >> t;
    getline(cin, g);
    forn(i, t)
    {
        getline(cin, g);
        printf("Case #%d: ", i + 1);
        forn(j, g.length())
            forn(k, goog.length())
                if(g[j] == goog[k])
                {
                    cout << engl[k];
                    break;
                }
        printf("\n");
    }
}
