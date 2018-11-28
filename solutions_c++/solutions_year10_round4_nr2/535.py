#include <vector> 
#include <list> 
#include <map> 
#include <set> 
#include <deque> 
#include <queue> 
#include <stack> 
#include <bitset> 
#include <algorithm> 
#include <functional> 
#include <numeric> 
#include <utility> 
#include <complex> 
#include <sstream> 
#include <iostream> 
#include <iomanip> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <cstring> 
#include <ctime> 
#include <cassert> 
using namespace std;

#define ME(s) memset((s), 0, sizeof((s)))
#define MM(s,a) memset((s),(a),sizeof((s)))
#define MCP(s,a) memcpy((s), (a), sizeof(s))
#define LL long long
#define PII pair<int, int>
#define mkp(a,b) make_pair((a),(b))
#define x first
#define y second
#define FOR(i,n) for (int (i)=0;(i)<(n);++(i))

int m[1<<10],cost[11][1<<10],dp[11][1<<10][11];
int n,T,t;
void init(){
    scanf("%d",&n);
    //cout<<n<<endl;
    FOR(i,1<<n) scanf("%d",&m[i]);
    for(int i=1;i<=n;++i) FOR(j,1<<(n-i)) scanf("%d",&cost[i][j]);
}
void updata(int &a,int b){
    if (b!=-1) if (a==-1 || b<a) a=b;
}
void work(){
    MM(dp,-1);
    FOR(j,1<<n) dp[0][j][m[j]]=0;

    for(int i=1;i<=n;++i) FOR(j,1<<(n-i)){
        int x1=j*2;int x2=j*2+1;
            //    cout<<"y"<<i<<" "<<j<<" "<<x1<<" "<<x2<<endl;
        FOR(p1,n+1) if (dp[i-1][x1][p1]!=-1)
        FOR(p2,n+1) if (dp[i-1][x2][p2]!=-1) {
            int p=min(p1,p2);
            updata(dp[i][j][p],dp[i-1][x1][p1]+dp[i-1][x2][p2]+cost[i][j]);
            if (p>0) updata(dp[i][j][p-1],dp[i-1][x1][p1]+dp[i-1][x2][p2]);
            
          //  cout<<i<<" "<<j<<" "<<p<<" "<<dp[i][j][p]<<endl;
        } 
    }
    
    int ans=-1;
    FOR(p,n+1) updata(ans,dp[n][0][p]);
    printf("Case #%d: %d\n",++t,ans);
}
int main(){
    freopen("B.in","r",stdin);
    freopen("B.out","w",stdout); 
    cin>>T;
    t=0;
    while(T--){
        init();
        work();
    }
    //while (1>0) {}
    return 0;
}
