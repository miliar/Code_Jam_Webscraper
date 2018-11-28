#include <iostream>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <string>
#include <cstring>
#include <cmath>
#include <climits>
#include <algorithm>
#include <cstdio>
#include <ctime>
#include <fstream>
#include <sstream>
using namespace std;

typedef unsigned long long ULL;
typedef long long LL;

#define REP(i,n)      FOR(i,0,n)
#define FOR(i,a,b)    for(int i = a; i < b; i++)
#define ROF(i,a,b)    for(int i=a;i>b;i--)
#define min(a,b)      (a<b?a:b)
#define max(a,b)      (a>b?a:b)
#define GI 		      ({int t;scanf("%d",&t);t;})
#define GL 		      ({LL t;scanf("%lld",&t);t;})
#define GD 		      ({double t;scanf("%lf",&t);t;})
#define pb 	          push_back
#define mp 	          make_pair
#define fii 	      freopen("input.txt","r",stdin)
#define fio 	      freopen("output.txt","w",stdout)
#define MOD 	      1000000007
#define INF	          (int)1e9
#define EPS	          1e-9
#define TR(a,it)      for (typeof((a).begin()) it = (a).begin(); it != (a).end(); ++it)

int main()
{
	fii; fio;

	map<char, char> mp;

    mp['y'] = 'a';
    mp['n'] = 'b';
    mp['f'] = 'c';
    mp['i'] = 'd';
    mp['c'] = 'e';
    mp['w'] = 'f';
    mp['l'] = 'g';
    mp['b'] = 'h';
    mp['k'] = 'i';
    mp['u'] = 'j';
    mp['o'] = 'k';
    mp['m'] = 'l';
    mp['x'] = 'm';
    mp['s'] = 'n';
    mp['e'] = 'o';
    mp['v'] = 'p';
    mp['z'] = 'q';
    mp['p'] = 'r';
    mp['d'] = 's';
    mp['r'] = 't';
    mp['j'] = 'u';
    mp['g'] = 'v';
    mp['t'] = 'w';
    mp['h'] = 'x';
    mp['a'] = 'y';
    mp['q'] = 'z';

	int T, t = 0;
	char str[200];

	scanf("%d", &T);
	while (T--) {
	    getchar();
        scanf("%[^\n]s", str);
        int len = strlen(str);

        printf("Case #%d: ", ++t);
        for (int i=0; i<len; i++)
            printf("%c", ((str[i] != ' ') ? mp[str[i]] : ' '));
        printf("\n");
	}

	fprintf(stderr, "Time execute: %.3lf\n", clock() / (double)CLOCKS_PER_SEC);
	return 0;
}
