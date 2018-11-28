#include<iostream>
#define fr(i,a,b) for(i=a;i<=b;++i)
using namespace std;
const int maxn=1002;
long long g[maxn],next[maxn],tot[maxn],ca,ti,r,k,n,i,j,now;
int main(){
	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);
	cin>>ca;
	fr(ti,1,ca){
		cin>>r>>k>>n;
		long long ans=0,all=0;		
		fr(i,1,n){
			cin>>g[i];
			all+=g[i];
		}
		if(all<=k){
			cout<<"Case #"<<ti<<": "<<r*all<<endl;
			continue;
		}
		fr(i,1,n){
			tot[i]=g[i];
			j=i;
			while(tot[i]+g[j%n+1]<=k){
				j=j%n+1;
				tot[i]+=g[j];
			}
			next[i]=j%n+1;
		}
		now=1;
		while(r--){
			ans+=tot[now];
			now=next[now];
		}
		cout<<"Case #"<<ti<<": "<<ans<<endl;
	}
}
