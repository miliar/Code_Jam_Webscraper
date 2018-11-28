#include <vector> 
#include <list> 
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

const int L=256;
int dp[2][300],a[200];
int D,I,M,n;

void updata(int a,int &b){
	if (b==-1 || a<b) b=a;
//	cout<<a<<" "<<b<<endl;
}
int T,t;
int main(){
	freopen("a.in","r",stdin);
	freopen("b.out","w",stdout);
	cin>>T;
	FOR(t,T){
		scanf("%d%d%d%d",&D,&I,&M,&n);
		FOR(i,n) cin>>a[i];
	//	cout<<D<<" "<<I<<" "<<M<<" ";FOR(i,n) cout<<a[i]<<" ";
		MM(dp,-1);
		FOR(i,256) dp[0][i]=0;
		int t1=0,t2;
		FOR(k,n){
		//	cout<<k<<endl;
			t2=t1^1;
			FOR(i,L) dp[t2][i]=-1;
			FOR(i,L) updata(dp[t1][i]+D,dp[t2][i]);
			FOR(i,L) if (abs(i-a[k])<=M) updata(dp[t1][i],dp[t2][a[k]]);
			if(M==0) FOR(i,L) updata(dp[t1][i]+abs(i-a[k]),dp[t2][i]);
			else 
			FOR(i,L) FOR(j,L)  updata(dp[t1][i]+abs(a[k]-j)+max(0,( (abs(i-j)-1) /M)*I),dp[t2][j]);
			t1=t2;
			
		//	if(t==98) cout<<endl;for (int i=40;i<=50;++i) cout<<dp[t1][i]<<" ";
		
		}
		int ans=-1;
		FOR(i,L) updata(dp[t1][i],ans);
	
		cout<<"Case #"<<t+1<<": "<<ans<<endl; 
	}
//	while (1>0){}
}
