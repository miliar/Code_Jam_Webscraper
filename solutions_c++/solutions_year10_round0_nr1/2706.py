#include <iostream>
#include <cstdio>
#include <algorithm>
#include <utility>
#include <string>
#include <vector>
#include <cmath>
#include <set>
#include <stack>
#include <queue>
#include <map>
#include <sstream>
#include <ctime>
#include <numeric>
#include <cstring>
#include <functional>

using namespace std;

typedef vector<int> VI;
typedef pair<int, int> PII;
typedef vector<PII> VPII;
typedef vector<PII> VPII;
typedef vector<string> VS;
typedef map<string, int> MSI;

#define REP(i, n) for (int i = 0; i < n; ++i)
#define FOR(i, a, b) for (int i = a; i < b; ++i)
#define FORD(i, a, b) for (int i = a-1; i >= b; --i)
#define ALL(x) x.begin(), x.end()
#define SIZE(x) (int)x.size()
#define FOREACH(it, c) for (__typeof(c.begin()) it = c.begin(); it != c.end(); ++it)
#define INF 987654321
#define PB push_back
#define MP make_pair
#define DEBUG(x) cerr<<#x<<": "<<x<<endl;
#define ERR(...) fprintf(stderr, __VA_ARGS__);
#define EPS 1e-9
#define INIT { REP(i,0);FOR(i,0,0);FORD(i,0,0);DEBUG("");ERR("\n");PII b=MP(SIZE(VI()), int(INF+EPS));VPII a;a.PB(b);VS s;}
#define ACC accumulate

typedef unsigned long long int LLU;

LLU T[100];

int main(void) {
    T[1] = 1;
    FOR(i, 2, 42)
        T[i] = 1+2*T[i-1];
    
    int n, k, t;
    scanf("%d", &t);
    FOR(i, 1, t+1) {
        scanf("%d %d", &n, &k);
        printf("Case #%d: ", i);
        if ((k+1) % (T[n]+1) == 0) 
            printf("ON\n");
        else 
            printf("OFF\n");
    }
    return 0;
}

