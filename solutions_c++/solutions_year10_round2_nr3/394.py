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

FILE *fin=freopen("C.in","r",stdin);
FILE *fout=freopen("C.out","w",stdout);

inline int sgn(double x){return fabs(x)<1e-12?0:(x<0?-1:1);}
LL f[510][510][510],mod=100003,C[600][600];

inline LL get(int num,int pos,int l){
	if(l<=0)
		return 0;
	if(pos==1)
		return l==1;
	LL &ret=f[num][pos][l];
	if(ret!=-1)
		return ret;
	ret=0;
	for(int k=pos-1;k>=1;--k)
		ret=(ret+get(pos,k,l-1)*C[num-pos-1][pos-k-1]%mod)%mod;
	return ret;
}

int main(){
	int T,c=0;
	memset(f,-1,sizeof(f));
	cin >> T;
	C[0][0]=1LL;
	for(int i=1;i<600;i++){
		C[i][0]=1LL;
		for(int k=1;k<=i;k++)
			C[i][k]=(C[i-1][k]+C[i-1][k-1])%mod;
	}
	while(T--){
		LL ans=0;
		int N;
		cin >> N;
		for(int i=N-1;i>=2;--i)
			for(int l=N-1;l>=1;--l)if(i-l>=0){
				LL t=get(N,i,l);
				ans=(ans+t)%mod;
			}
		cout << "Case #" << ++c << ": " << ans+1 << endl;
	}
	return 0;
}

//Powered by [KawigiEdit] 2.0!

