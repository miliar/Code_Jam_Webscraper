#include <iostream>
#include <cstdio>
#include <algorithm>
#include <numeric>
using namespace std;

typedef long long ll;
const int maxn = 1000 + 10;
int R,K,N;
int gs[maxn];
ll sum[maxn];
ll v[maxn];
int idx[maxn];

int main()
{
	int T;
	cin>>T;
	int i,j,a,d,p,l;
	ll ans;
	for(i=1;i<=T;i++){
		scanf("%d%d%d",&R,&K,&N);
		sum[0] = 0;
		for(j=1;j<=N;j++){
			scanf("%d",&gs[j]);
			sum[j] = gs[j];
		}
		fill(idx+1,idx+N+1,-1);
		partial_sum(sum+1,sum+N+1,sum+1);
		p = 1;
		int score;
		for(j=1;j<=N+1;j++){
			score = 0;
			if(idx[p]>=0)break;
			idx[p] = j;
			for(l = 0; l<N && score + gs[p]<=K;l++){
				score += gs[p++];
				if(p>N) p-=N;
			}
			//cout<<score<<' '<<p<<endl;
			v[j] = score;
		}
		//cout<<"A"<<endl;
		d = j - idx[p];
		a = idx[p];
		partial_sum(v+1,v+j,v+1);
		//cout<<a<<' '<<d<<endl;
		//copy(v+1,v+j,ostream_iterator<int>(cout," "));
		if(R<a){
			ans = sum[R];
		}else{
			R -= a;
			ans = v[R % d + a];
			ans += (ll)R / d * (v[j - 1] - v[idx[p] - 1]);
			//cout<<(v[j-1] - v[idx[p]-1])<<' '<<ans<<endl;
		}
		printf("Case #%d: ",i);
		cout<<ans<<endl;
	}
	return 0;
}
