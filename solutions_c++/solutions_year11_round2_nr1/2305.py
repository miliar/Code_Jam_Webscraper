#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <list>
#include <algorithm>
#include <sstream>
using namespace std;

typedef long long LL;

#define chkB(a,n) (a[n>>3]&(1<<(n&7))) //char array
#define setB(a,n) (a[n>>3]|=(1<<(n&7))) //char array
#define UN(v) { SORT(v); v.erase(unique(v.begin(), v.end()),v.end()); }
#define SORT(c) sort((c).begin(),(c).end());
#define FOR(i,a,b) for (i=a; i<b; i++)
#define FORu(i,a,b) for (i=a; i>=b; i--)
#define FORstr(i,a,b) for (i=a; b[i]!=NULL; i++)
#define CL(a,b) memset(a, b, sizeof (a))
#define pb push_back
#define MK make_pair
#define inf (1<<30)
#define infL ((1<<63)-1)LL
#define pi double(2.0*acos(0))

char input[120][120];

double f(int str, int len) {
    int i, wp = 0, total = 0; FOR(i,0,len) if (input[str][i] == '0') total++; else if (input[str][i] == '1') { wp++; total++; }
    return (double)wp/(double)total;
}

double f1(int bad, int len) {
    int i, wp = 0, total = 0, j;
    double ret = 0.0, count = 0.;
    FOR(j,0,len) { if (j==bad || input[bad][j] == '.') continue; wp = total = 0; count++;
        FOR(i,0,len) {
            if (i==bad) continue; else if (input[j][i] == '0') total++; else if (input[j][i] == '1') { wp++; total++; }
        }
        ret += ( (double)wp/(double)total );
    }
    return ret/count;
}

double f3(int str, double owp[], double wp, int line) {
    double ret = wp, total = 0., count = 0.;
    int i;
    FOR(i,0,line) if (input[str][i] != '.') { total += owp[i]; count++; }
    return total/count;
}

int main() {
    freopen("1.txt","r",stdin);
    freopen("2.txt","w",stdout);
    int kase, tCase = 0; scanf ("%d",&kase);

    while (kase--) {
        int line, i, j; scanf ("%d",&line);
        FOR(i,0,line) scanf ("%s",input[i]);
        double wp[120], owp[120], oowp[120], res[120];
        FOR(i,0,line) wp[i] = f(i,line);
        FOR(i,0,line) owp[i] = f1(i, line);
        FOR(i,0,line) oowp[i] = f3(i,owp, wp[i], line);
        FOR(i,0,line) res[i] = (0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i]);

        printf ("Case #%d:\n",++tCase);
        FOR(i,0,line) printf ("%lf\n",res[i]);
    }

    return 0;
}
