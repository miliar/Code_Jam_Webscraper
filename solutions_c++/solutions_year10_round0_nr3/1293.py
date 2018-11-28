#include<cstdio>
#include<iostream>
#include<algorithm>

using namespace std;

typedef long long ll;

int r,k,n;
int g[2010];
int next[1010];
int sum[1010];
int id[1010],pp=0;
int main(){
	int t;
	cin>>t;
	for(int ca=1;ca<=t;++ca){
		cin>>r>>k>>n;
		for(int i=0;i<n;++i)scanf("%d",&g[i]),g[n+i]=g[i];
		
		ll wa=0,ans=0;
		for(int i=0;i<n;++i)wa+=g[i];
		if(wa<=k){
			printf("Case #%d: %lld\n",ca,r*wa);
			continue;
		}
		for(int i=0;i<1010;++i)id[i]=0;
		pp=0;
		
		int now=0,hoge=0;
		for(int i=0;i<n;++i){
			if(i)now-=g[i-1];
			while(now+g[hoge]<=k)now+=g[hoge++];
			next[i]=hoge%n;
			sum[i]=now;
//			cout<<i<<" "<< next[i]<<" "<<sum[i]<<endl;
		}
		int shuki=0,ju=0,ima=0,nanka;
		do{
			if(id[ima]){
				shuki=pp-id[ima]+1;
				nanka=ima;
				break;
			}
			id[ima]=++pp;
//			if(ima>next[ima])ju++;
//			++shuki;
			ima=next[ima];
		}while(1);
		do{
			if(ima>next[ima])++ju;
			ima=next[ima];
		}while(ima!=nanka);
		
//		cout<<shuki<<" "<<nanka<<" "<<ju<<endl;
		
		int turn=0;
		for(int no=0;turn<id[nanka]-1;++turn){
			if(turn == r) goto print;
			ans+=sum[no];
			no=next[no];
		}
//		cout<<ans<<endl;
		ans+=wa*ju*((r-turn)/shuki);
		
		turn += (r-turn)/shuki*shuki;
//		cout<<ans<<endl;
		
		for(int no=nanka;turn < r;++turn){
			ans+=sum[no];
			no=next[no];
		}
		
		print:;
		printf("Case #%d: %lld\n",ca,ans);
	}
	return 0;
}
