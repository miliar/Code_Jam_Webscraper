#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdio>
#include <string>
#include <cmath>
#include <list>
#include <cstdlib>
#include <map>
#include <cstring>
#include <set>
#include <stack>
#include <sstream>
#include <queue>
#include <ctime>

using namespace std;

#define debug(x) cout<<#x<<" = "<<x<<"\n"
#define FOR(t,a,n) for(int t=(a);(t)<(n);(t)++)
#define REP(I,N) FOR(I,0,N)
#define PB(X) push_back(X)
#define MP(X,Y) make_pair(X,Y)
#define ALL(x) (x).begin(), (x).end()
#define SET(A,v) memset(A,v,sizeof A)
#define INF (int)1e9

typedef long long LL;
typedef long double LD;
typedef vector<int> VI;
typedef list<int> LI;
typedef vector<string> VS;
typedef pair<int,int> PII;

int main()
{
    #ifdef VIN
        freopen("1_in.txt","r",stdin);
        freopen("2_out.txt","w",stdout);
    #else
        freopen("C-small.in","r",stdin);
        freopen("C-small.txt","w",stdout);
    #endif
        int T,nu=0;
        scanf("%d",&T);
        while(T--){
            int n;
            int ans=-INF;
            scanf("%d",&n);
            int ar[n];
            REP(i,n)scanf("%d",ar+i);
            int lmt = (1<<n)-1;
            FOR(x,1,lmt){
                int a=0,b=0;
                int Sx=0,Py=0;
                REP(j,n){
                    if(x&(1<<j))a=a^ar[j],Sx+=ar[j];
                    else b=b^ar[j],Py+=ar[j];
                    
                }
                if(a==b)ans=max(ans,max(Sx,Py));
            }
            if(ans==-INF) printf("Case #%d: NO\n",++nu);
            else printf("Case #%d: %d\n",++nu,ans);
        }
        return 0;
}
            
