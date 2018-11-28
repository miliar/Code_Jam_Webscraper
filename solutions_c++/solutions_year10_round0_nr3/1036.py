#include<cstdio>
#include<queue>
using namespace std;

queue<int>qe,q;

int main(){
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);
	int i,j,t,r,k,n,g[1010],res[1010],f=1,p,ans;
	scanf("%d",&t);
	while(t--){
		scanf("%d %d %d",&r,&k,&n);
		qe=q;
	 	for(i=0;i<n;i++){
			scanf("%d",&g[i]);  qe.push(g[i]);
		}
		ans=0;
		for(i=0;i<r;i++){
			int count=p=0;
			if(qe.empty()) continue;
			while(!qe.empty()){
				if(count+qe.front()<=k){
					count+=qe.front();
					res[p++]=qe.front();
					qe.pop();
				}
				else break;
			}	
			ans+=count;
			for(j=0;j<p;j++){
				qe.push(res[j]);
			}
		}
		printf("Case #%d: %d\n",f++,ans);
	}
	return 0;
}
