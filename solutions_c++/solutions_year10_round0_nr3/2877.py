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

#define oo 1<<30
#define f first
#define s second
#define II inline
#define db double
#define ll long long
#define pb push_back
#define mp make_pair
#define Size(V) ((int)(V.size()))
#define all(v) v.begin() , v.end()
#define CC(v) memset((v),0,sizeof((v)))
#define CP(v,w) memcpy((v),(w),sizeof((w)))
#define FOR(i,a,b) for(int (i)=(a);(i)<=(b);++(i))
#define REP(i, N) for (int (i)=0;(i)<(int)(N);++(i))
#define FORit(it, x) for (__typeof((x).begin()) it = (x).begin(); it != (x).end(); ++it)

#define IN  "code.in"
#define OUT "code.out"

typedef vector<int> VI;
typedef pair<int,int> pi;
typedef vector<string> VS;
template<class T> string toString(T n) {ostringstream ost;ost<<n;ost.flush();return ost.str();}

int T,R,K,N,C[1<<17];
deque<int> Q;

II void scan()
{
    freopen(IN,"r",stdin);
    freopen(OUT,"w",stdout);
}

II void solve(int Test)
{
    int val(0),rez = 0;
    scanf("%d%d%d",&R,&K,&N);
    Q.clear();

    FOR(i,1,N)
    {
        scanf("%d",&val);
        Q.push_back(val);
    }

    FOR(i,1,R)
    {
        int sum = 0;
        C[0] = 0;

        for(;!Q.empty() && sum + Q.front() <= K;)
        {
            int aux = Q.front();
            Q.pop_front();
            sum += aux;

            C[++C[0]] = aux;
        }

        FOR(i,1,C[0])
        {
            //printf("%d ",C[i]);
            Q.push_back(C[i]);
            rez += C[i];
        }
        //printf("\n");
    }

    printf("Case #%d: %d\n",Test,rez);
}

int main()
{
    scan();

    scanf("%d",&T);
    FOR(i,1,T)
        solve(i);

    return 0;
}
