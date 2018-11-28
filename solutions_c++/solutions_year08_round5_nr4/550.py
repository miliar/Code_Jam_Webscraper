#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <cmath>
using namespace std;

typedef long long ll;
typedef vector<int> vi;
const int INF=1000000005;
#define mset(a,x) memset(a,x,sizeof(a))
#define MIN(a, b) ((a) < (b) ? (a) : (b))
#define MAX(a, b) ((a) > (b) ? (a) : (b))
#define ABS(a) ((a) >= 0 ? (a) : -(a))
#define SIZE(x) (int(x.size()))
#define FOR(k,a,b) for(int k=(a); k < (b); ++k)
#define FORREV(k,a,b) for(int k=(b); (a) <= (--k);)
template <class T>void printarr(const T* a,int n){for(int i=0;i<n;i++)cerr<<a[i]<<" ";cerr<<endl;}
#define dbg(x) cerr<<#x<<" : "x<<endl
#define dbgarr(x,n) cerr<<#x<<" : ",printarr(x,n)

int H,W,R;
int Map[105][105];
int dp[105][105];

void init(){
	mset(Map,0);
	mset(dp,0);
}

int main()
{
	int T,kcase(0);
	scanf("%d",&T);
	while(T--){
		init();
		scanf("%d%d%d",&H,&W,&R);
		for(int i=0;i<R;i++){
			int r,c;
			scanf("%d%d",&r,&c);
			Map[r][c]=1;
		}
		dp[1][1]=1;
		for(int i=2;i<=H;i++){
			for(int j=2;j<=W;j++){
				if(!Map[i][j]){
					if(i-2>=1)(dp[i][j]+=dp[i-2][j-1])%=10007;
					if(j-2>=1)(dp[i][j]+=dp[i-1][j-2])%=10007;
				}
			}
		}
		printf("Case #%d: %d\n",++kcase,dp[H][W]);
	}
}
