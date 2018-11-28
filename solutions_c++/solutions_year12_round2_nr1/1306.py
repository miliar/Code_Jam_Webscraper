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
#define N_MAX 1<<8

typedef vector<int> VI;
typedef pair<int,int> pi;
typedef pair<short int,short int> ps;
typedef vector<string> VS;
template<class T> string toString(T n) {ostringstream ost;ost<<n;ost.flush();return ost.str();}

int N,J[N_MAX];
double Sol[N_MAX],Sum;

II void scan() {
    freopen(IN,"r",stdin);
    freopen(OUT,"w",stdout);
}

II void solve(int test) {

    Sum = 0.0;
    scanf("%d",&N);

    FOR(i,1,N) {
        scanf("%d",J+i);
        Sum += J[i];
    }

    FOR(i,1,N) {

        double m = 0.0,step = 1.0;

        for(m = 1.0;step > 1e-7;step /= 2)
            if(m - step >= 0.0) {
                double total = 1.0 - (m - step);
                double score = (double)J[i] + (m - step) * Sum;

                FOR(j,1,N) {
                    if(j == i)
                        continue;
                    double reqScore = (score + 1e-7) - J[j];

                    if(reqScore > 0)
                        total -= (reqScore / Sum);
                }

                //then is ok
                if(total < 0)
                    m -= step;
            }

        Sol[i] = m * 100.0;
    }

    printf("Case #%d: ",test);

    FOR(i,1,N)
        printf("%lf ",Sol[i]);
    printf("\n");
}

int main()
{
    scan();

    int Tests;
    scanf("%d",&Tests);
    FOR(i,1,Tests)
        solve(i);
    return 0;
}
