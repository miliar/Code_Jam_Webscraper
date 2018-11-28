#include <cstdio>
#include <cstring>
typedef long long ll;

ll choose(int n, int k) {
	if(k>n) return 0;
	if(k>n/2) k=n-k;
	ll ans=1;
	for(int i=1;i<=k;++i)
		ans*=(n-k+i), ans/=i;
	return ans;
}

int main() {
	int N,n,A,B,C,D,x0,y0,M;
	ll mod3[3][3];
	ll x,y;
	scanf("%d",&N);
	for(int nc=0;nc<N;++nc) {
		scanf("%d%d%d%d%d%d%d%d",&n,&A,&B,&C,&D,&x0,&y0,&M);
		x=x0,y=y0;
		memset(mod3,0,sizeof(mod3));
		mod3[x%3][y%3]++;
		for(int i=1;i<n;++i) {
			x=(A*x+B)%M;
			y=(C*y+D)%M;
			mod3[x%3][y%3]++;
		}
		ll ans=0;
		for(int i=0;i<3;++i)
			for(int j=0;j<3;++j)
				ans+=choose(mod3[i][j],3);
		for(int i=0;i<3;++i) {
			ll xsum=1, ysum=1;
			for(int j=0;j<3;++j)
				xsum*=mod3[i][j], ysum*=mod3[j][i];
			ans+=xsum+ysum;
		}
		ans+=mod3[0][0]*mod3[1][1]*mod3[2][2];
		ans+=mod3[0][0]*mod3[1][2]*mod3[2][1];
		ans+=mod3[0][1]*mod3[1][0]*mod3[2][2];
		ans+=mod3[0][1]*mod3[1][2]*mod3[2][0];
		ans+=mod3[0][2]*mod3[1][1]*mod3[2][0];
		ans+=mod3[0][2]*mod3[1][0]*mod3[2][1];
		printf("Case #%d: %lld\n",nc+1,ans);
	}
}