using namespace std;

#include <set>
#include <map>
#include <list>
#include <deque>
#include <stack>
#include <queue>
#include <cmath>
#include <ctime>
#include <cctype>
#include <cstdio>
#include <vector>
#include <string>
#include <bitset>
#include <utility>
#include <iomanip>
#include <fstream>
#include <cstring>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <functional>

#define oo (1<<30)
#define f first
#define s second
#define II inline
#define db double
#define ll long long
#define pb push_back
#define mp make_pair
#define Size(V) ((ll)(V.size()))
#define all(V) (V).begin() , (V).end()
#define CC(V) memset((V),0,sizeof((V)))
#define CP(A,B) memcpy((A),(B),sizeof((B)))
#define FOR(i,a,b) for(int (i)=(a);(i)<=(b);++(i))
#define REP(i, N) for (int (i)=0;(i)<(int)(N);++(i))
#define FORit(it, x) for (__typeof((x).begin()) it = (x).begin(); it != (x).end(); ++it)
#define printll(x) printf("%lld",(x))
#define printsp() printf(" ")
#define newline() printf("\n")
#define readll(x) scanf("%lld",&(x))
#define debugll(x) fprintf(stderr,"%lld\n",(x))

#define IN "code.in"
#define OUT "code.out"
#define N_MAX 1<<21

typedef vector<int> VI;
typedef pair<int,int> pi;
typedef pair<short int,short int> ps;
typedef vector<string> VS;
template<class T> string toString(T n) {ostringstream ost;ost<<n;ost.flush();return ost.str();}

int N,S,P,Tests;

II void scan() {
    freopen(IN,"r",stdin);
    freopen(OUT,"w",stdout);
    scanf("%d\n",&Tests);
}

II void solve(int testCase) {

    scanf("%d%d%d",&N,&S,&P);

    int x;
    VI scores;
    FOR(i,1,N) {
        scanf("%d",&x);
        scores.pb(x);
    }
    sort( all(scores) );

    int res = 0;

    if(P == 1) {
        FOR(i,0,N)
            if(scores[i] != 0)
                ++res;
        printf("Case #%d: %d\n",testCase,res);
        return;
    }

    for(int i = N - 1;i >= 0;--i)
        if(scores[i] >= P * 3 - 2)
            ++res;
        else if(scores[i] >= P * 3 - 2 - 2 && S) {
            --S;
            ++res;
        }

    printf("Case #%d: %d\n",testCase,res);
}

int main() {
    scan();

    FOR(i,1,Tests)
        solve(i);
    return 0;
}
