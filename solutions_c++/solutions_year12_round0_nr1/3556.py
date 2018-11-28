#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <deque>
#include <set>
#include <map>
#include <string>
//#include <conio.h>
using namespace std;
#define FOR(i, a, b) for(int i=a; i<=b; i++)
#define DOW(i, a, b) for(int i=a; i>=b; i--)
#define FOREACH(it, c) for(typeof(c.begin()) it=c.begin(); it!=c.end(); it++)
#define RESET(c, val) memset(c, val, sizeof(c))

string s, t;
int test;
char nex[300];

int main() {
    freopen("test.in", "r", stdin);
    freopen("test.out", "w", stdout);
    nex['z']='q'; nex['q']='z';
    s="ejp mysljylc kd kxveddknmc re jsicpdrysi";
    t="our language is impossible to understand";
    FOR(i, 0, s.length()-1) nex[s[i]]=t[i];
    s="rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
    t="there are twenty six factorial possibilities";
    FOR(i, 0, s.length()-1) nex[s[i]]=t[i];
    s="de kr kd eoya kw aej tysr re ujdr lkgc jv";
    t="so it is okay if you want to just give up";
    FOR(i, 0, s.length()-1) nex[s[i]]=t[i];
    scanf("%d\n", &test);
    FOR(i, 1, test) {
        cout << "Case #" << i << ": ";
        getline(cin, s);
        FOR(j, 0, s.length()-1) printf("%c", nex[s[j]]);
        if (i<test) printf("\n");
    }
    //getch();
    return 0;
}
