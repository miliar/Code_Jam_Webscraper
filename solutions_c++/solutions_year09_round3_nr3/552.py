#include<iostream>
using namespace std;
const int mmax=1000000000;
int n,m;
int a[110];
bool empty[110];
bool use[110];
int ans;
int cal(int j){
	int r=0;
	int i=j+1;
	while(i<=n){
		if(!empty[i]){
			r++;
			i++;
		}
		else break;
	}
	i=j-1;
	while(i>=1){
		if(!empty[i]){
			r++;
			i--;
		}
		else break;
	}
	return r;
}
void dfs(int i,int r){
	if(ans<r)return ;
	if(i==m){
		if(ans>r)ans=r;
		return ;
	}
	int j;
	for(j=0;j<m;j++){
		if(!use[j]){
			use[j]=true;
			empty[a[j]]=true;
			dfs(i+1,r+cal(a[j]));
			use[j]=false;
			empty[a[j]]=false;
		}
	}
}
int solve(){
	ans=mmax;
	dfs(0,0);
	return ans;
}
int main(){
	int t;
	int count=1;
	scanf("%d",&t);
	while(t--){
		scanf("%d%d",&n,&m);
		memset(empty,false,sizeof(empty));
		memset(use,false,sizeof(use));
		int i;
		for(i=0;i<m;i++)scanf("%d",&a[i]);
		cout<<"Case #"<<count<<": "<<solve()<<endl;
		count++;
	}
	return 0;
}