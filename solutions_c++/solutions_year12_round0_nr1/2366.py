#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <set>
#include <map>
#include <queue>
#include <cassert>
#include <math.h>
#include <string.h>
#include <stdio.h>
using namespace std;
#define SCAN_INT() (*({int _si;assert(1==scanf("%d", &_si)); &_si;}))
#define REP(i,n) for( int i=0;i<int(n);++i)
#define SZ size()
namespace my_namespace {
};
using namespace my_namespace;
string googlese =
 "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
string english =
 "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";
void problem()
{
    assert(googlese.SZ == english.SZ);
    map < char, char >ma;
    REP(i, googlese.SZ) {
        char from = googlese[i];
        char to = english[i];
        if (ma.count(from))
            assert(ma[from] == to);
        else
            ma[from] = to;
    }
    ma['z'] = 'q';
    ma['q'] = 'z';
    char b[120];
    assert(1 == scanf("%[^\n]\n", b));
    int l = strlen(b);
    REP(i, l) {
        if (!ma.count(b[i])) {
            fprintf(stderr, "didn't find: '%c'\n", b[i]);
            exit(1);
        }
        b[i] = ma[b[i]];
    }
    printf("%s\n", b);
}
int main()
{
    int n = SCAN_INT();
    assert(0 == scanf("\n"));
    REP(i, n) {
        printf("Case #%d: ", i + 1);
        problem();
    }
    return 0;
}
