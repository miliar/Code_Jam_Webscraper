#include <iostream>
#include <conio.h>
#include <vector>
#include <string>
#include <list>
#include <numeric>
#include <cstring>
#include <set>
#include <queue>
#include <stack>
#include <math.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>
#include <time.h>
#include <bitset>
#include <algorithm>
using namespace std;

#define FOR(i, a, b) for(i=(a); i<(b); i++)
#define IFOR(i, a, b) for(i=(a); i>=(b); i--)
#define FORD(i, a, b, c) for(i=(a); i<(b); i+=(c))
#define REP(i, n) for(i=0; i<(n); i++)
#define MAX(a, b) ((a)>(b)?(a):(b))
#define MIN(a, b) ((a)<(b)?(a):(b))
#define P printf
#define S scanf
#define SZ(x) ((int)x.size())
#define PB(x) push_back(x)
#define INF 1000000000
#define V vector

typedef V<int> VI;
typedef V<string> VS;
typedef long long LL;
typedef pair<int, int> PII;
main()
{
    freopen("inpt.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int T, k, n,i, total;
    cin>>T;
    REP(i, T){
        S("%d%d", &n, &k);
        int index=k/(1<<n);
        k-=index*(1<<n);
        if(k==((1<<n)-1)){
             P("Case #%d: ON\n", i+1);
        }
        else{
             P("Case #%d: OFF\n",i+1);
        }
    }

}
