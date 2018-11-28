#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<string>
#include<set>
#include<map>
#include<vector>
#include<algorithm>
#include<sstream>
#include<stack>
#include<queue>
#include<deque>
#include<iostream>
using namespace std;
#define sz(X) (int)X.size()
#define mp(X,Y) make_pair(X,Y)
#define pb(X) push_back(X)
#define clr(X) memset(X,0,sizeof(X))
#define klr(X) memset(X,-1,sizeof(X))
#define ll long long
#define pii pair<int,int>
map<ll, pair< pair<ll,ll>,ll> > mapa;
int n;
ll  v[510];

int main(){
	int t;
	scanf("%d",&t);
	for(int caso=1;caso<=t;caso++){
		scanf("%d",&n);
		for(int i=0;i<n;i++)
			scanf("%lld",&v[i]);	
		printf("Case #%d:\n",caso);
		pair< pair<ll,ll>,ll> r1, r2;
		mapa.clear();
		bool achou = false;
	
	
		for(int i=0;i<n;i++)
			mapa[v[i]] = mp(mp(v[i],-1),-1);
	
	
		for(int i=0;!achou && i<n;i++)
			for(int j=i+1;!achou && j<n;j++){
					ll sum = v[i] + v[j];
					if(mapa.find(sum)==mapa.end())
						mapa[sum] = mp(mp(v[i],v[j]),-1);
					else{
						map<ll, pair< pair<ll,ll>,ll> > :: iterator it = mapa.find(sum);
						if(v[i]!=it->second.first.first && v[i]!=it->second.first.second
						   && v[j]!=it->second.first.first && v[j]!=it->second.first.second){
						
						if(it->second.first.second==-1)
							printf("%lld\n",it->second.first.first);
						else printf("%lld %lld\n",it->second.first.first, it->second.first.second);
						printf("%lld %lld\n",v[i],v[j]);
						achou = true;
						break;
						}
						else mapa[sum] = mp(mp(v[i],v[j]),-1);
					}
			}
			
		for(int i=0;!achou && i<n;i++)
			for(int j=i+1;!achou && j<n;j++)
				for(int k = j+1;k<n;k++){
					ll sum = v[i] + v[j] + v[k];
					if(mapa.find(sum)==mapa.end())
						mapa[sum] = mp(mp(v[i],v[j]),v[k]);
					else{
						map<ll, pair< pair<ll,ll>,ll> > :: iterator it = mapa.find(sum);
						if(v[i]!=it->second.first.first && v[i]!=it->second.first.second && v[i]!=it->second.second &&
						   v[j]!=it->second.first.first && v[j]!=it->second.first.second && v[j]!=it->second.second &&
						   v[k]!=it->second.first.first && v[k]!=it->second.first.second && v[k]!=it->second.second
						   ){
						if(it->second.first.second==-1)
							printf("%lld\n",it->second.first.first);
						else if(it->second.second==-1)
							printf("%lld %lld\n",it->second.first.first, it->second.first.second);
						else printf("%lld %lld %lld\n",it->second.first.first, it->second.first.second,it->second.second);
						printf("%lld %lld %lld\n",v[i],v[j],v[k]);
						achou = true;
						break;
						}
						else mapa[sum] = mp(mp(v[i],v[j]),v[k]);
					}
				}
		if(!achou)
			printf("Impossible\n");
	}
	return 0;
}
