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
#define LD long double
#define PII pair<int, int>
#define PDD pair<double, double>
#define mkp(a,b) make_pair((a),(b))
#define y first
#define x second
#define sqr(a) ((a)*(a))
#define lowbit ((x)&(-(x)))
#define two(x) (1<<(x))
#define contain(mask,x) ((mask&two(x))!=0) 
LL R,K,N,g[11111];
LL rec[11111],dp[11111];
LL last[11111];

int main(){
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
	int Test;
	cin >> Test ;
	for(int c=1;c<=Test;c++){
		printf("Case #%d: ",c);
		cin >> R >> K >> N ;
		for(int i=0;i<N;i++){
			cin >> g[i];
			g[i+N]=g[i];
		}
		
		memset(rec,-1,sizeof(rec));
		LL ans=0LL;
		int now=0;
		for(int i=0;i<R;i++){
			//cout << now << "  "<< ans << endl;
			if(rec[now]!=-1){
				int len=i-last[now];
				LL Left=R-i;
				//cout << Left << "  " << len << endl;
				for(int j=last[now]+1;j<i;j++)
					rec[now]+=dp[j];
				ans+=Left/len*rec[now];
				Left%=len;
				for(int j=0;j<Left;j++)
					ans+=dp[j+last[now]];
				break;
			}
			LL tot=0LL;
			int j=0;
			while(j<N&&tot+g[now+j]<=K){
				tot+=g[now+j];
				j++;
			}
			dp[i]=tot;
			last[now]=i;
			ans+=tot;
			rec[now]=tot;
			now=(now+j)%N;
		}
		cout << ans << endl;
	}
	return 0;
}



