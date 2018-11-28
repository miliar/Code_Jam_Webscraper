#include<cstdio>
#include<algorithm>
#include<vector>
#include<queue>
using namespace std;

priority_queue<int> q;

int main(){
	int cas,N,S,p,in,cm;
	scanf("%d",&cas);
	for(int i=1;i<=cas;i++){
		scanf("%d %d %d",&N,&S,&p);
		int ans=0;
		while(q.size()) q.pop();
		for(int j=0;j<N;j++){
			scanf("%d",&in);
			if(in>28) ans++;
			else if(in<2){
				if(in>=p) ans++;
			}
			else q.push(in);
		}
		while(q.size()){
			cm=q.top();
			cm+=2;
			cm/=3;
			if(cm<p) break;
			ans++;
			q.pop();
		}
		while(S&&q.size()){
			cm=q.top();
			cm+=4;
			cm/=3;
			if(cm<p) break;
			ans++;
			S--;
			q.pop();
		}
		printf("Case #%d: %d\n",i,ans);
	}
}
