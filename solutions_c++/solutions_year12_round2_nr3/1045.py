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
#define N_MAX (1<<10)
#define S_MAX (1<<19)
#define bit(x) (1<<((x) - 1))

typedef vector<int> VI;
typedef pair<int,int> pi;
typedef pair<short int,short int> ps;
typedef vector<string> VS;
template<class T> string toString(T n) {ostringstream ost;ost<<n;ost.flush();return ost.str();}

int A[N_MAX],Q[1<<19],B[N_MAX];
int N,V[N_MAX];
map<int,int> M;

II void scan() {
    freopen(IN,"r",stdin);
    freopen(OUT,"w",stdout);
}

II void solve(int test) {
    scanf("%d",&N);
    FOR(i,1,N)
        scanf("%d\n",V+i);

    FOR(cfg,1,(1<<N) - 1) {
        M.clear();
        M[0] = 0;

        int SumA = 0;
        FOR(i,1,N)
            if(cfg & bit(i) )
                SumA += V[i];
            else {
                Q[0] = 0;

                FORit(it, M)
                    Q[++Q[0]] = it->f;
                FOR(j,1,Q[0])
                    if(Q[j] + V[i] <= SumA)
                        M[ Q[j] + V[i] ] = i;
            }

        if(M.find(SumA) != M.end() ) {

            A[0] = B[0] = 0;

            FOR(i,1,N)
                if(cfg & bit(i) )
                    A[++A[0]] = V[i];
            for(int ind = SumA;ind != 0;ind -= V[ M[ind] ])
                B[++B[0]] = V[ M[ind] ];

            break;
        }
    }


    printf("Case #%d:\n",test);
    FOR(i,1,A[0])
        printf("%d ",A[i]);
    printf("\n");
    FOR(i,1,B[0])
        printf("%d ",B[i]);
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
