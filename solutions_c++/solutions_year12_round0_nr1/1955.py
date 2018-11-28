#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <cctype>
#include <cstring>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <string>
#include <algorithm>
#define FOR(i,a,b) for(int i=int(a); i<int(b); ++i)
#define FORD(i,a,b) for(int i=int(a)-1; i>=int(b); --i)
#define FORE(i,q) for(typeof((q).begin()) i=(q).begin(); i!=(q).end(); ++i)
using namespace std;

typedef long long LG;
typedef long double LD;

char S[101], T[257];

void preproc() {
    T['a'] = 'y';
    T['b'] = 'h';
    T['c'] = 'e';
    T['d'] = 's';
    T['e'] = 'o';
    T['f'] = 'c';
    T['g'] = 'v';
    T['h'] = 'x';
    T['i'] = 'd';
    T['j'] = 'u';
    T['k'] = 'i';
    T['l'] = 'g';
    T['m'] = 'l';
    T['n'] = 'b';
    T['o'] = 'k';
    T['p'] = 'r';
    T['q'] = 'z';
    T['r'] = 't';
    T['s'] = 'n';
    T['t'] = 'w';
    T['u'] = 'j';
    T['v'] = 'p';
    T['w'] = 'f';
    T['x'] = 'm';
    T['y'] = 'a';
    T['z'] = 'q';
    T[' '] = ' ';
}

void testcase(int zzz) {
    gets(S);
    int n = strlen(S);
    printf("Case #%d: ", zzz);
    FOR(i,0,n) printf("%c", T[S[i]]);
    printf("\n");
}

int main() {
    int ZZZ; scanf("%d%*c", &ZZZ);
    preproc();
    FOR(zzz,0,ZZZ) testcase(zzz + 1);
    return 0;
}
