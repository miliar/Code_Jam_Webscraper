#include <cmath>
#include <ctime>
#include <cstdio>
#include <cctype>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <string>
#include <vector>
#define maxn 11000
#define maxl 1000000000
using namespace std;

typedef long long ll;

typedef map<vector<int>,int>::iterator It;
string s,a[maxn];
int f[maxn];
int show[100];

bool check(int x,int now){
	int i;
	for(i=0;i<a[x].size()-1;++i)if(show[a[x][i]-'a'+1]>=now)return false;
	return true;
}

void dfs(int k,int now,const vector<int> &v1){
	//cout<<k<<endl;
	//for(int i=0;i<v1.size();++i)cout<<v1[i]<<" ";
	//cout<<endl;
	if(k==s.size()){
		for(int i=0;i<v1.size();++i)f[v1[i]]=now;
		return;
	}
	map<vector<int>,int> mm;
	mm.clear();
	vector< vector<int> > v;
	vector<int> mid,em;
	em.clear();
	v.clear();
	int i,j,temp;
	for(i=0;i<v1.size();++i){
		mid.clear();
		if(check(v1[i],k)){
			f[v1[i]]=now;
			continue;
		}
		for(j=0;j<a[v1[i]].size();++j)if(a[v1[i]][j]==s[k])mid.push_back(j);
		if(!mm.count(mid)){
			v.push_back(em);
			mm[mid]=v.size()-1;
		}
		v[mm[mid]].push_back(v1[i]);
	}
	if(v.size()==0)return;
	if(v.size()==1){
		dfs(k+1,now,v[0]);
		return;
	}
	for(It it=mm.begin();it!=mm.end();++it){
		temp=(*it).second;
		if((*it).first.size()==0)dfs(k+1,now+1,v[temp]);else dfs(k+1,now,v[temp]);
	}
}

int n;

void did(){
	cin>>s;
	s=" "+s;
	int i,ans,i1;
	for(i=1;i<=26;++i)show[s[i]-'a'+1]=i;
	for(i=1;i<=n;++i)f[i]=30;
	vector<int> v1;
	v1.clear();
	for(i=1;i<=n;++i)v1.push_back(i);
	dfs(0,0,v1);
	ans=-1;i1=0;
	for(i=1;i<=n;++i)if(f[i]>ans){
		ans=f[i];
		i1=i;
	}
//	cout<<ans<<endl;
	cout<<" "<<a[i1].substr(0,a[i1].size()-1);
}
	
void solve(){
	int m,i;
	cin>>n>>m;
	for(i=1;i<=n;++i){
		cin>>a[i];
		a[i]=a[i]+" ";
	}
	for(i=1;i<=m;++i)did();
	cout<<endl;
}
	
		

int main(){
	ios::sync_with_stdio(false);
	int t,i;
	cin>>t;
	for(i=1;i<=t;++i){
		cout<<"Case #"<<i<<":";
		solve();
	}
	return 0;
}
