#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sstream>

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
typedef vector<long>::iterator VLI;
typedef set<int>::iterator SII;
#define FOR(i,n) for(int i = 0; i<(n); i++)
#define FORD(i,n) for(int i=(n)-1; i>=0; i--)
#define FOR1(i,n) for(int i=1; i<=(n); i++)
#define FOR1D(i,n) for(int i=(n); i>=1; i--)
#define NL printf("\n")

//sort(t.begin(),t.end(),greater<int>()); // malejaco
//sort(t.begin(),t.end(),less<int>()); // rosnaco
//char buf[500]; gets(buf); stringstream ss(buf); int x; while(ss > x) {}


int t[1000];

long testuj(int *num, int ilewiez, int ilezwol) {
    long wyn = 0;
    FOR(i,ilewiez)
    t[i] = 1;

    FOR(i,ilezwol) {
        t[num[i]] = 0;
        for (int j = num[i] - 1; j >= 0; --j)
            if (t[j]) ++wyn;
            else break;
        for (int j = num[i] + 1; j < ilewiez; ++j)
            if (t[j]) ++wyn;
            else break;
    }

    return wyn;

}

int main() {

    char buf[1024];
    int numery[10];
    int tests;

    scanf("%d",&tests);

    FOR(t,tests) {
        int wiez,wyp;
        scanf("%d %d",&wiez,&wyp);
        FOR(i,wyp) {
            int num;
            scanf("%ld",&num);
            --num;
            numery[i] = num;
        }
/*
        FOR(i,wyp)
        printf("%d ",numery[i]);
        NL;
*/
        int ile = wyp;
        sort(numery, numery+ile,less<int>());

        long wyn = testuj(numery,wiez,ile);
        while (next_permutation(numery,numery+ile)) {
            long tmp = testuj(numery,wiez,ile);
            if (tmp < wyn)
                wyn = tmp;
        }
        printf("Case #%d: %ld\n",t+1,wyn);
    }


    return 0;

}

