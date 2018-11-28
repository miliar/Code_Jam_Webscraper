// Artur Kraska, II UWr

#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <cmath>
#include <list>
#include <set>
#include <map>

#define znak(z)                     ((z) <= '9' ? (z)-'0' : (z) - 'A'+10)
#define foreach(iter, coll)         for(typeof(coll.begin()) iter = coll.begin(); iter != coll.end(); ++iter)
#define foreachr(iter, coll)        for(typeof(coll.rbegin()) iter = coll.rbegin(); iter != coll.rend(); ++iter)
#define lbound(P,R,PRED)            ({typeof(P) X=P,RRR=(R), PPP = P; while(PPP<RRR) {X = (PPP+(RRR-PPP)/2); if(PRED) RRR = X; else PPP = X+1;} PPP;})

#define M 1000000007

using namespace std;

int n, k, wynik, tab[1000007];
char z[128], slowo[1005], slowo2[1005];
bool b[128];

void pom(char *f, char *s)
{
    for(int i=0; f[i]; i++)
    {
        z[f[i]] = s[i];
        b[s[i]] = 1;
    }
}

void ustaw()
{
    z['a'] = 'y';
    z['b'] = 'h';
    z['c'] = 'e';
    z['d'] = 's';
    z['e'] = 'o';
    z['f'] = 'c';
    z['g'] = 'v';
    z['h'] = 'x';
    z['i'] = 'd';
    z['j'] = 'u';
    z['k'] = 'i';
    z['l'] = 'g';
    z['m'] = 'l';
    z['n'] = 'b';
    z['o'] = 'k';
    z['p'] = 'r';
    z['q'] = 'z';
    z['z'] = 'q';
    z['r'] = 't';
    z['s'] = 'n';
    z['t'] = 'w';
    z['u'] = 'j';
    z['v'] = 'p';
    z['w'] = 'f';
    z['x'] = 'm';
    z['y'] = 'a';
    z[' '] = ' ';
}

/*
ejp mysljylc kd kxveddknmc re jsicpdrysi
our language is impossible to understand
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
there are twenty six factorial possibilities
de kr kd eoya kw aej tysr re ujdr lkgc jv
so it is okay if you want to just give up
y qee
a zoo
*/

int main()
{/*
    for(int i=0; i<4; i++)
    {
        cin.getline(slowo, 1000);
        cin.getline(slowo2, 1000);
        pom((char*)slowo, (char*)slowo2);
    }

    for(int i='a'; i<='z'; i++)
    {
        printf("z['%c'] = '%c';\n", i, z[i]);
        if(!b[i])   printf("z['z'] = '%c';\n", i);
    }*/

    ustaw();

    scanf("%d", &n);
    cin.getline(slowo, 1000);
    for(int i=0; i<n; i++)
    {
        cin.getline(slowo, 1000);
        printf("Case #%d: ", i+1);
        for(int i=0; slowo[i]; i++)
            printf("%c", z[slowo[i]]);
        printf("\n");
    }

	return 0;
}
