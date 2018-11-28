#include <cstdlib> 
#include <cctype> 
#include <cstring> 
#include <cstdio> 
#include <cmath> 
#include <algorithm> 
#include <vector> 
#include <string> 
#include <iostream> 
#include <sstream> 
#include <map> 
#include <set> 
#include <queue> 
#include <stack> 
#include <fstream> 
#include <numeric> 
#include <iomanip> 
#include <bitset> 
#include <list> 
#include <stdexcept> 
#include <functional> 
#include <utility> 
#include <ctime> 
using namespace std; 

#define PB push_back 
#define MP make_pair 

#define rep(i,n) for(int i=0;i<(n);++i) 
#define FOR(i,l,h) for(int i=(l);i<=(h);++i) 
#define FORD(i,h,l) for(int i=(h);i>=(l);--i) 
#define print(expr) cout<<(#expr)<<" : "<<(expr)<<endl

typedef vector<int> VI; 
typedef vector<string> VS; 
typedef vector<double> VD; 
typedef long long int64; 
typedef pair<int,int> pii; 

const int maxn=1050;
int c[maxn]={},n,ans=-1;

void solve(int x)
{
	if(x==0 || x==(1<<n)-1) return;
	int c1=0,c2=0;
	rep(i,n) if(x & (1<<i)) c1 ^= c[i]; else c2 ^= c[i];
	if(c1==c2 && c1 && c2)
	{
		int res=0;
		rep(i,n) if(x & (1<<i)) res += c[i];
		ans=max(ans,res);
	}
}

int main(void)
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);
	int T; cin>>T;
	FOR(Case,1,T)
	{
		ans=-1;
		cin>>n;
		rep(i,n) cin>>c[i];
		rep(i,(1<<n)) solve(i);
		cout<<"Case #"<<Case<<": ";
		if(ans==-1) cout<<"NO\n";
		else cout<<ans<<'\n';
	}
}