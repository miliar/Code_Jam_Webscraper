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

int Tests,A,B;
bool viz[N_MAX];
VI stack;

II void scan() {
    freopen(IN,"r",stdin);
    freopen(OUT,"w",stdout);
    scanf("%d",&Tests);
}

II VI intToArray(int x) {
    VI res;
    for(;x;res.pb(x % 10), x /= 10);
    reverse( all(res) );
    return res;
}

II int arrayToInt(VI x) {
    int res = 0;
    FORit(it,x)
        res = res * 10 + *it;
    return res;
}

II void solve(int testCase) {
    int cnt = 0;

    scanf("%d%d",&A,&B);

    FOR(i,A,B) {
        VI stack = intToArray(i);
        VI Sol;

        FOR(k,1,Size(stack) - 1) {
            VI newStack;
            FOR(j,k,Size(stack) - 1)
                newStack.pb(stack[j]);
            FOR(j,0,k - 1)
                newStack.pb(stack[j]);

            int number = arrayToInt(newStack);

            if(number <= B && number > i) {
                Sol.pb(number);
                //fprintf(stderr,"we have %d %d\n", i, number);
            }

        }

        sort( all(Sol) );
        int last = -1;
        FORit(it,Sol)
            if(*it != last) {
                ++cnt;
                last = *it;
            }

    }


    printf("Case #%d: %d\n",testCase, cnt);
}

int main() {
    scan();

    FOR(i,1,Tests)
        solve(i);
    return 0;
}
