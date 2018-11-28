//{{{

#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <queue>
#include <list>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>
using namespace std;

#define VAR(a,b) __typeof(b) a=(b)
#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++) //Nice trick
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
#define REP(i,n) FOR(i,0,n)
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define REVERSE(c) reverse(ALL(c))
#define UNIQUE(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())
#define INF 1000000000
#define X first
#define Y second
#define pb push_back
#define SZ(c) (c).size()
typedef pair<int, int> PII;
typedef vector<int> VI;
typedef vector<PII> VPII;
typedef vector<VI> VVI;

//}}}

int SolveTest(int test){
    int N;
    int a,b;
    scanf("%d",&N);
    VPII P;
    REP(ii, N){
       scanf("%d %d",&a,&b);
       P.pb(make_pair(a,b));
    }
    SORT(P);
    int ans=0;
    for(int i=0;i<SZ(P)-1;i++){
        for(int j=i;j<SZ(P);j++){
          if(P[i].second>P[j].second)
              ans++;
          }
    }

    printf("Case #%d: %d\n",test,ans);
    return 0;
}

int main(void){

    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);

    int T,i;
    char buf[1<<7];
	gets(buf);
	sscanf(buf, "%d", &T);
	for(i=0;i<T;i++)
	{
		fprintf(stderr, "Solving %d/%d\n", i + 1, T);
		SolveTest(i+1);
	}

	return 0;
}
