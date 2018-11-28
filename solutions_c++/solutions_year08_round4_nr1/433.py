#include <iostream>
using namespace std;

#define MAX 10002
int n,gate[MAX],chg[MAX],val[MAX];

#define min(x,y) ((x)<(y)?(x):(y))

typedef pair<int,int> pii;
#define INF 100000000

pii solve(int node){
	//if (val[node]==v) return 0;
	if (node>(n-1)/2){
		if (val[node]==0) return make_pair(0,INF);
		return make_pair(INF,0);
	}
	pii ret[2];
	ret[0]=solve(node*2);
	ret[1]=solve(node*2+1);
	pii res=make_pair(INF,INF);
	//if (val[node]==0) res= make_pair(0,INF);
	//else res=make_pair(INF,0);
	if (gate[node]==0 || chg[node]){
		res.first =min(res.first,  ret[0].first +ret[1].first +(gate[node]!=0));
		res.second=min(res.second, ret[0].second+ret[1].first +(gate[node]!=0));
		res.second=min(res.second, ret[0].first +ret[1].second+(gate[node]!=0));
		res.second=min(res.second, ret[0].second+ret[1].second+(gate[node]!=0));
	}
	if (gate[node]==1 || chg[node]){
		res.first =min(res.first,  ret[0].first +ret[1].first +(gate[node]!=1));
		res.first =min(res.first, ret[0].second+ret[1].first +(gate[node]!=1));
		res.first =min(res.first, ret[0].first +ret[1].second+(gate[node]!=1));
		res.second=min(res.second, ret[0].second+ret[1].second+(gate[node]!=1));
	}
	return res;
}

int main(){
	int t,u,v,i;
	cin>>t;
	for (u=0; u<t; u++){
		cin>>n>>v;
		for (i=1; i<=(n-1)/2; i++){
			cin>>gate[i]>>chg[i];
			val[i]=0;
		}
		for (;i<=n; i++){
			cin>>val[i];
			chg[i]=0;
		}
		for (i=n-1; i>=2; i--){
			if (gate[i/2]==1) val[i/2]=val[i]&val[i+1];
			else val[i/2]=val[i]|val[i+1];
		}
		pii res = solve(1);
		int ret;
		if (v==0) ret=res.first;
		else ret=res.second;
		cout<<"Case #"<<(u+1)<<": ";
		if (ret==INF) cout<<"IMPOSSIBLE"<<endl;
		else cout<<ret<<endl;
	}
	return 0;
}
