
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <vector>
#include <list>
#include <map>
#include <queue>
#include <algorithm>
#include <cmath>
#include <set>

using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef vector<int> VI;
typedef vector<int>::iterator VII;
typedef set<int>::iterator SII;
#define FOR(i,n) for(int i = 0; i<(n); i++)
#define FORD(i,n) for(int i=(n)-1; i>=0; i--)
#define FOR1(i,n) for(int i=1; i<=(n); i++)
#define FOR1D(i,n) for(int i=(n); i>=1; i--)
#define NL printf("\n")
//sort(t.begin(),t.end(),greater<int>()); // malejaco
//sort(t.begin(),t.end(),less<int>()); // rosnaco
//char buf[500]; gets(buf); stringstream ss(buf); int x; while(ss > x) {}o

int main() {

    char buf[500];
    int testy = 0;

    gets(buf);
    testy = atoi(buf);


    FOR(t,testy) {
        gets(buf);
        int ile = strlen(buf);

        if (ile == 1) {
            printf("Case #%d: 1\n",t+1);
            continue;
        }
        set<char> zbior;
        FOR(i,ile) zbior.insert(buf[i]);

        map<char,int> wart;

        FOR (i,ile)
        wart[buf[i]] = -1;

        if (buf[0] != buf[1]) {
            wart[buf[1]] = 0;
        } else {
            char b = buf[0];
            FOR (i,ile) {
                if (buf[i] != b) {
                    wart[buf[i]] = 0;
                    break;
                }
            }
 /*
            for (int i = ile -2; ile >=0; --i) {
                if (wart[buf[i]] == -1) {
                    wart[buf[i]] = 0;
                    break;
                }
            }
  */
        }

        int w = 1;
        FOR(i,ile) {
            if (wart[buf[i]] == -1) {
                wart[buf[i]] = w;
                ++w;
            }
        }

        if (zbior.size() == 1) {
            wart[buf[0]] = 1;
        }

        ULL ppp = zbior.size();

        if (zbior.size() == 1)
            ppp = 2;
/*
        FOR (i,ile)
        printf("%c=%d, ",buf[i],wart[buf[i]]);
        NL;
*/
        ULL wyn = 0;
        ULL pods = 1;

        for (int i = ile - 1; i >= 0; --i) {
            wyn += pods * wart[buf[i]];
            pods*=ppp;

        }

         printf("Case #%d: %lld\n",t+1,wyn);
    }

    return 0;
}
