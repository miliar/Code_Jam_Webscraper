#include <cstdio>
#include <iostream>

using namespace std;

int R,limP,n;
int a[1010],nxt[1010];
long long tot[1010];
bool use[1010];
int t;
long long ans;
long long sum[1010];

int main(){
	//freopen("c0.in","r",stdin);
	int test=0;
	scanf("%d", &test);
	for ( int T=1; T<=test; ++T ){
		scanf("%d %d %d", &R, &limP, &n);
		memset(sum,0,sizeof(sum));
		for ( int i=0; i<n; ++i )
			scanf("%d", a+i);
		for ( int i=0; i<n; ++i ){
			long long s=0; nxt[i]=i;
			for ( int j=0; j<n; ++j ){
				s=s+a[(i+j)%n];
				if ( s>limP ){
					nxt[i]=(i+j)%n; break;
				}
				tot[i]=s;
			}
		}
		ans=0;
		memset(use,false,sizeof(use));
		int now=0;  t=0;
		while ( ! use[now] ){
			use[now]=true;
			now=nxt[now];
			++t;
		}
		if ( t<R ){
			int pp=now;
			now=0;
			while ( now!=pp ){
				ans+=tot[now]; now=nxt[now]; --R;
			}
			t=0; sum[0]=0;
			while ( nxt[now]!=pp ){
				++t;
				sum[t]=sum[t-1]+tot[now];
				now=nxt[now];
			}
			++t;
			sum[t]=sum[t-1]+tot[now];
			ans=ans+sum[t]*(R/t)+sum[R%t];
		} else {
			now=0; ans=0;
			for ( int i=0; i<R; ++i ){
				ans+=tot[now]; now=nxt[now];
			}
		}
		cout<<"Case #"<<T<<": "<<ans<<endl;
	}
}
