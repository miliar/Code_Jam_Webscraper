#include <cstdio>
#include <map>
#include <set>
#include <vector>
#include <ctime>
#include <cmath>
#include <algorithm>
#include <fstream>
#include <queue>
#include <list>
#include <cstring>
#define FOR(i,a,n) for(int i=a;i<=n;i++)
#define REP(i,n) for (int i=0;i<n;i++)
#define FORD(i,n,a) for(int i=n;i>=a;i--)
#define PB push_back
#define MP make_pair
#define xx first
#define yy second
#define Min(a,b) a<b ? a:b
#define Max(a,b) a>b ? a:b
#define p2(a) ((a)*(a))
#define ALL(v) v.begin(),v.end()
using namespace std;
typedef vector<int> vi;
typedef pair<int,int> pi;
typedef double dd;
const int INF=100000000;
const int R=105;
int C[R][R];
int Pri[R];
int p,q;
int solve(void){
    scanf("%d %d",&p,&q);
    REP(i,q+3)
        REP(j,q+3)
            C[i][j]=INF;
    FOR(i,1,q)
        scanf("%d",&Pri[i]);
    Pri[0]=0;
    Pri[q+1]=p+1;
    REP(i,q+1)
        C[i][i+1]=0;
    FOR(k,2,q+1)
        FOR(i,0,q+1-k)
            FOR(j,i+1,i+k-1)
                C[i][i+k]=min(C[i][i+k],C[i][j]+C[j][i+k]+Pri[i+k]-Pri[i]-2);
    /*FOR(i,0,q)
        FOR(j,i+1,q+1)
            printf("%d %d : %d\n",i,j,C[i][j]);*/
    return C[0][q+1];
}
    
int main(){
    int tests;
    scanf("%d",&tests);
    REP(i,tests)
        printf("Case #%d: %d\n",i+1,solve());
    
    return 0;
}
