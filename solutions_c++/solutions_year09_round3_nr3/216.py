#include <iostream>
#include <map>
#include <vector>
#include <cstdlib>
#include <algorithm>
using namespace std;
int N,n,q,x;
bool isq[10000];
map<pair<int,int>,int > dp;
int solve(int st,int en){
	map<pair<int,int>,int >::iterator it=dp.find(make_pair(st,en));
	if(it!=dp.end())
		return it->second;
	int ret=1000000000;
	for(int i=st;i<=en;i++)
		if(isq[i])
			ret=min(ret,en-st+solve(st,i-1)+solve(i+1,en));
	if(ret==1000000000)
		ret=0;
	return dp[make_pair(st,en)]=ret;
}
int main() {
	freopen("C-large.in", "rt", stdin);
	freopen("C-large.out", "wt", stdout);
	cin>>N;
	for(int nn=0;nn<N;nn++){
		cin>>n>>q;
		memset(isq,0,sizeof isq);
		for(int i=0;i<q;i++){
			cin>>x;
			isq[x-1]=1;
		}
		dp.clear();
		cout<<"Case #"<<nn+1<<": "<<solve(0,n-1)<<endl;
	}
	return 0;
}
