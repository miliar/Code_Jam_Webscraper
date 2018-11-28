// Artur Kraska, II UWr

#include <algorithm>
#include <iostream>
#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <vector>
#include <queue>
#include <cmath>
#include <list>
#include <set>
#include <map>


#define znak(z)                     ((z) <= '9' ? (z)-'0' : (z) - 'A'+10)
#define forr(it, lim)               for(int it=0; it < (lim); it++)
#define foreach(iter, coll)         for(typeof(coll.begin()) iter = coll.begin(); iter != coll.end(); ++iter)
#define foreachr(iter, coll)        for(typeof(coll.rbegin()) iter = coll.rbegin(); iter != coll.rend(); ++iter)
#define lbound(P,R,PRED)            ({typeof(P) X=P,RRR=(R), PPP = P; while(PPP<RRR) {X = (PPP+(RRR-PPP)/2); if(PRED) RRR = X; else PPP = X+1;} PPP;})
#define CLEAR(TABB)                 memset(TABB, 0, sizeof(TABB));
#define vv(type, name, ...)         type name ## 77[] = { __VA_ARGS__ }; vector <type> name(name ## 77, (name ## 77)+sizeof(name ## 77)/sizeof(name ## 77[0]));
#define testy()                     int tests;scanf("%d", &tests);forr(test, tests)
#define jest(coll, val)             (coll.find(val) != coll.end())
#define deb(X)                      X

#define M   1000000007
#define INF 1000000007

const int MAX_BUF_SIZE = 16384;
char BUFOR[MAX_BUF_SIZE];
int BUF_SIZE, BUF_POS;
char ZZZ;
#define GET(ZZZ){ZZZ='a';if(BUF_POS<BUF_SIZE)ZZZ=BUFOR[BUF_POS++];\
else if(!feof(stdin)){BUF_SIZE=fread(BUFOR,1,MAX_BUF_SIZE,stdin);\
ZZZ=BUFOR[0];BUF_POS=1;}}
#define GI(WW){do{GET(ZZZ);}while(!isdigit(ZZZ));WW=ZZZ-'0';\
while(1){GET(ZZZ);if(!isdigit(ZZZ))break;WW=WW*10+(ZZZ-'0');}}
#define GC(WW){do{GET(ZZZ);}while(!isalpha(ZZZ));WW=ZZZ;}

using namespace std;

int n, m, k;
int wynik;
char slowo[10][10];

int check(char znak)
{
    forr(i, 4)
    {
        int ile = 0;
        forr(j, 4)
            if(slowo[i][j] == znak || slowo[i][j] == 'T')
                ile++;
        if(ile == 4)
            return 1;
    }
    forr(i, 4)
    {
        int ile = 0;
        forr(j, 4)
            if(slowo[j][i] == znak || slowo[j][i] == 'T')
                ile++;
        if(ile == 4)
            return 1;
    }
    {
        int ile = 0;
        forr(j, 4)
            if(slowo[j][j] == znak || slowo[j][j] == 'T')
                ile++;
        if(ile == 4)
            return 1;
    }
    {
        int ile = 0;
        forr(j, 4)
            if(slowo[3-j][j] == znak || slowo[3-j][j] == 'T')
                ile++;
        if(ile == 4)
            return 1;
    }

    return 0;
}

int main()
{
    testy()
    {
        forr(i, 4)
            scanf("%s", slowo[i]);

        int owin = 0, xwin = 0, pelne = 0;

        owin = check('O');
        xwin = check('X');

        forr(i, 4)
            forr(j, 4)
                if(slowo[i][j] == '.')
                    pelne = 1;

        printf("Case #%d: ", test+1);

        if(owin == 1 && xwin == 0)
            printf("O won\n");
        else if(owin == 0 && xwin == 1)
            printf("X won\n");
        else if(owin == 1 && xwin == 1)
            printf("Draw\n");
        else if(!pelne)
            printf("Draw\n");
        else printf("Game has not completed\n");

    }

    return 0;
}

