#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
using namespace std;
typedef long long LL;
const int maxn=2100000;
int Mp[maxn],Run,tt;

namespace Nprep{
	inline int get(int n){
		int Fc=n,x,N;
		for(N=1;N<n;N*=10);
		for(x=10;x<N;x*=10)
			Fc=min(Fc,n%x*(N/x)+n/x);
		return Fc;
	}
	void solve(){
		for(int i=1;i<=2000000;++i)Mp[i]=get(i);
	}
}

namespace Nmain{
	LL ans;
	int A,B,i,a[maxn];
	inline LL Comb(int n){
		return (LL)n*(n-1)/2;
	}
	void solve(){
		memset(a,0,sizeof a),ans=0;
		cin>>A>>B;
		for(i=A;i<=B;++i)++a[Mp[i]];
		for(i=1;i<=B;++i)ans+=Comb(a[i]);
		printf("Case #%d: %lld\n",Run,ans);
	}
}

int main(){
	//freopen("C-small-attempt0.in","r",stdin);
	freopen("C-large.in","r",stdin);
	freopen("love.out","w",stdout);
	Nprep::solve();
	for(cin>>tt,Run=1;tt;--tt,++Run)Nmain::solve();
	fclose(stdout);
	return 0;
}
