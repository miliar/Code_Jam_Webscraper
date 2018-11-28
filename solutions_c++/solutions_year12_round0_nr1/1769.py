
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <utility>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstdio>
#include <cstring>
//#include <conio.h>

using namespace std;

#define oo 1000000000
#define fi first
#define se second
#define sqr(a) ((a)*(a))
#define FR(i,n) for (int i = 0; i < (n); i++)
#define DN(i,a) for(int i = (a)-1; i >= 0; i--)
#define FOR(i,a,b) for (int i = (a); i <= (b); i++)
#define DOWN(i,a,b) for(int i = (a); i >= (b); i--)
#define FORV(i,a) for(typeof(a.begin()) i = a.begin(); i != a.end(); i++)

typedef pair<int, int> PII;
typedef vector<int> VI;

char Map[255], s[255];
int T, res = 0;
bool dd[255];

void make(string s1, string s2) {
    int n = s1.length();
    FR(i, n) {
        Map[s1[i]] = s2[i];
        dd[s2[i]] = true;
    }

}

void init() {
    Map['q'] = 'z';
    dd['z'] = true;
    string s1, s2;
    s1 = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
    s2 = "our language is impossible to understand";
    make(s1, s2);
    s1 = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
    s2 = "there are twenty six factorial possibilities";
    make(s1, s2);
    s1 = "de kr kd eoya kw aej tysr re ujdr lkgc jv";
    s2 = "so it is okay if you want to just give up";
    make(s1, s2);
    FOR(i, 'a', 'z')
        if (!dd[i]) Map['z'] = i;
}

int main () {
    freopen("A-small-attempt1.in", "r", stdin);
    freopen("A.out", "w", stdout);
    init();
    cin >> T;
    gets(s);
    for (int i = 'a'; i <= 'z'; i++) if (Map[i] == 0) cout << (char)i << endl;
    FOR(i, 1, T) {
        printf("Case #%d: ", i);
        gets(s);
        FR(j, strlen(s)) {
            cout << Map[s[j]];
        }
        cout << endl;
    }
    return 0;
}
