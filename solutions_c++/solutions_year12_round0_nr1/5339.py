/*
ID: miyubai2
PROG:
LANG: C++
Mail to   : miyubai@gamil.com
My Blog   : www.miyub.com
Author By : MiYu
Test      : 1
Complier  : g++ mingw32-3.4.2
Program   :
Doc Name  :
*/
//#pragma warning( disable:4789 )
#ifdef LOCAL
//#pragma comment ( lib, "yzfy_graphics6.lib" )
//#include "graphics.h"
#endif
#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <utility>
#include <queue>
#include <stack>
#include <list>
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <ctime>
using namespace std;

#ifdef LOCAL
     #define SP system("pause");
     #define DBG Debug();
     #define BUG(x) x
#else
     #define SP
     #define DBG
     #define BUG(x)
#endif
void Debug () {
    freopen ( "A-small-attempt1.in", "r", stdin );
    freopen ( "A-small-attempt1.out", "w", stdout );
}
#pragma comment(linker, "/STACK:102400000,102400000")
#define MEM(x,y) memset(x,y,sizeof(x))
int N, M, T;
char h[256];
string a[3] = {
	"ejp mysljylc kd kxveddknmc re jsicpdrysi",
	"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
	"de kr kd eoya kw aej tysr re ujdr lkgc jv"	
};
string b[3] = {
	"our language is impossible to understand",
	"there are twenty six factorial possibilities",
	"so it is okay if you want to just give up"
};
void init () {
	for ( int i = 0; i < 3; ++ i ) {
		int n = a[i].size();
		for ( int j = 0; j < n; ++ j ) {
			h[a[i][j]] = b[i][j];	
		}	
	}
	h['z'] = 'q';
	h['q'] = 'z';
}
int read () {
    if ( scanf ( "" ) == EOF ) return 0;
    return 1;
}
void prs () {
	static int ca = 1;
	char s[110];
	gets (s);
	printf ( "Case #%d: ", ca++ );
	char *p = s;
	while ( *p ) putchar ( h[*p++] );
	puts("");
}
int main ()
{
    BUG(DBG)
    scanf ("%d\n", &T);
    while ( T -- ) {
        init ();
		prs();
    }
    SP
    return 0;
}
