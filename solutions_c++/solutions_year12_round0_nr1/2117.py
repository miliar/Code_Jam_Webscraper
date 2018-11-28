
// Tomasz Kulczynski
#include <cstdio>
#include <iostream>
#include <cstring>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <cmath>
#include <cstdlib>
#include <numeric>
#include <cassert>
using namespace std;

#define X first
#define Y second
#define MP make_pair
#define PB push_back
typedef long long LL;
typedef double D;
typedef long double LD;
typedef vector<int> VI;
typedef pair<int,int> PII;
#define REP(i,n) for (int i=0;i<(n);++i)
#define FOR(i,a,b) for (VAR(i,a);i<=(b);++i)
#define FORD(i,a,b) for(VAR(i,a);i>=(b);--i)
#define FORE(e,v) for(VAR(e,(v).begin());e!=(v).end();++e)
#define VAR(a,b) __typeof(b) a=(b)
#define SIZE(a) ((int)(a).size())
#define ALL(x) (x).begin(),(x).end()
#define CLR(x,a) memset(x,a,sizeof(x))

string a = "yqeejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jv";
string b = "azoour language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give up";

map<char, char> ma;
set<char> u;

int main() {
    REP(i, SIZE(a))
        ma[a[i]] = b[i];
    REP(i, SIZE(a))
        if(ma[a[i]] != b[i])
            assert(false);
    FORE(i, ma) u.insert(i->Y);
//    FOR(i, 'a', 'z') if(!u.count(i)) printf("%c\n",i);
    ma['z'] = 'q';
//    FOR(i, 'a', 'z') if(!ma.count(i)) printf("%c\n",i);
    int tt;
    scanf("%d",&tt);
    char buf[213];
    gets(buf);
    FOR(cas, 1, tt) {
        string s;
        gets(buf);
        s = buf;
        REP(i, SIZE(s)) s[i] = ma[s[i]];
        printf("Case #%d: %s\n", cas, s.c_str());
    }
    return 0;
}
