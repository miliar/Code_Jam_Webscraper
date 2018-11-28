#define _CRT_SECURE_NO_DEPRECATE
#pragma warning(disable:4530)
#include <string>
#include <vector>
#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <sstream>
#include <set>
#include <cmath>
#include <map>
#include <cassert>

using namespace std;

#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n) FOR(i,0,n)
#define FORE(it,x) for(typeof((x).begin())it=(x).begin();it!=(x).end();++it)
#define all(x) (x).begin(),(x).end()
#define CLR(x,v) memset(x,v,sizeof(x))
#define pb push_back
#define sz size()
#define exist(c,x) ((c).find(x)!=(c).end())
#define cexist(c,x) (find(all(c),x)!=(c).end())
#define SMIN(a, b) a = min((a),(b))
#define SMAX(a, b) a = max((a),(b))

typedef long long ll;

char buffer[4096];

string original = "welcome to code jam";

int main(int argc, char *argv[]) {
    freopen(argv[1], "r", stdin);
    int Tests;
    fgets(buffer, 4096, stdin);
    Tests=atoi(buffer);
    FOR(test, 1, Tests+1) {
        printf("Case #%d: ", test);

        fgets(buffer, 4096, stdin);
        int l = strlen(buffer);
        int D[1000][1000];
        D[0][0] = 0;
        FOR(i, 1, l+1) {
            D[0][i] = D[0][i-1] + (buffer[i-1] == original[0] ? 1 : 0);
            D[0][i] %= 10000;
        }
        FOR(k, 1, original.sz) {
            D[k][0] = 0;
            FOR(i, 1, l+1) {
                D[k][i] = D[k][i-1] + ((buffer[i-1] == original[k] )
                    ? D[k-1][i-1] : 0);

                D[k][i] %= 10000;
            }
        }
        printf("%04d\n", D[original.sz - 1][l]);

    }

}
