//Headers
#include <set>
#include <map>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <cctype>
#include <cstdio>
#include <string>
#include <vector>
#include <cassert>
#include <cstdlib>
#include <cstring>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <climits>
#include <clocale>
//Defines
#define pow2(i) (1<<i)
#define bit(i) (1<<i)
#define isOdd(i) (i&1)
#define isEven(i) (!(i&1))
#define isPrime(i) ((i==2) || ((i&1) && !pTest[i])) //pTest has to be the bool array's name
#define sz(i) i.size()
#define vec(type,name) vector< type > name
#define rep(i,a,b) for(int i=a ; i<=b ; i++)
#define swap(type,a,b) {type t=a; a=b; b=t;}
#define sum(a,n) ( (n*(n+1)/2) - (a-1)*a/2 )
#define iscap(i) (i>='A'&&i<='Z')
#define issmall(i) (i>='a'&&i<='z')
#define isnum(i) (i>='0'&&i<='9')
#define issymbol(i) (!(i>='a'&&i<='z') && !(i>='A'&&i<='Z') && !(i>='0'&&i<='9'))
#define mk(i,j) make_pair(i,j)
#define ERROR 1e-11
//Type Defs
typedef long long lint;
typedef unsigned long long ulint;
typedef long double ldouble;

using namespace std;

char mp[1000], fin[1000];
char input[200], output[200];

int main()
{
    //     TEST CASE     //
    int kase=1, kounter=1, i;
    freopen("A-small-attempt0.in","r",stdin);
    freopen("output.txt","w+",stdout);

    mp['a'] = 'y';
    mp['b'] = 'n';
    mp['c'] = 'f';
    mp['d'] = 'i';
    mp['e'] = 'c';
    mp['f'] = 'w';
    mp['g'] = 'l';
    mp['h'] = 'b'; //
    mp['i'] = 'k';
    mp['j'] = 'u';
    mp['k'] = 'o';
    mp['l'] = 'm';
    mp['m'] = 'x';
    mp['n'] = 's';
    mp['o'] = 'e';
    mp['p'] = 'v';
    mp['q'] = 'z'; //
    mp['r'] = 'p';
    mp['s'] = 'd';
    mp['t'] = 'r';
    mp['u'] = 'j';
    mp['v'] = 'g';
    mp['w'] = 't';
    mp['x'] = 'h';
    mp['y'] = 'a';
    mp['z'] = 'q';
    mp[' '] = ' ';


    for (i=0 ; i<=1000 ; i++)
    {
        fin[mp[i]] = i;
    }


    scanf("%d",&kase);
    getchar();
    while (kase--)
    {
        gets(input);
        for (i=0 ; input[i] ; i++)
        {
            output[i] = fin[ input[i] ];
        }
        output[i]='\0';
        printf("Case #%d: ",kounter++);
        puts(output);

    }

    return 0;
}
