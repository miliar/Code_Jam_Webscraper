#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <climits>
#include <cmath>
#include <ctime>
#include <cassert>
#include <iostream>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <complex>
#include <string>
#include <vector>
#include <list>
#include <deque>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <bitset>
#include <iterator>
#include <functional>
#include <utility>
#include <algorithm>
#include <numeric>
#include <typeinfo>

using namespace std;

#define dump(n) cout<<"# "<<#n<<"="<<(n)<<endl
#define repi(i,a,b) for(int i=int(a);i<int(b);i++)
#define rep(i,n) repi(i,0,n)
#define iter(c) __typeof((c).begin())
#define foreach(i,c) for(iter(c) i=(c).begin();i!=(c).end();++i)
#define allof(c) (c).begin(),(c).end()
#define mp make_pair

typedef unsigned int uint;
typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<string> vs;
typedef pair<int,int> pii;

void dfs(int depth,vs& dic,string& lst,vi& group,vs& states,vi& res)
{
	if(group.size()==1){
		//res[group[0]]=depth;
		return;
	}
	vi hist(26);
	rep(i,group.size()){
		string& word=dic[group[i]];
		string& state=states[group[i]];
		rep(j,word.size()){
			if(state[j]=='_')
				hist[word[j]-'a']=1;
		}
	}
	string apps;
	rep(i,26)
		if(hist[lst[i]-'a'])
			apps+=lst[i];
	
	//dump(apps);
	
	//puts("group");
	//rep(i,group.size())
	//	cout<<group[i]<<","<<states[group[i]]<<" ";
	//cout<<endl;
	
	map<string,int> ma;
	rep(i,group.size()){
		string& word=dic[group[i]];
		string& state=states[group[i]];
		if(count(allof(word),apps[0])==0){
			res[group[i]]++;
		}
		else{
			rep(j,word.size())
				if(word[j]==apps[0])
					state[j]=word[j];
		}
		ma.insert(mp(state,ma.size()));
	}
	
	//dump(ma.size());
	vvi ngroups(ma.size());
	rep(i,group.size()){
		int j=group[i];
		ngroups[ma[states[j]]].push_back(j);
	}
	
	//puts("ngroups");
	//rep(i,ngroups.size()){
	//	rep(j,ngroups[i].size())
	//		cout<<ngroups[i][j]<<","<<states[ngroups[i][j]]<<" ";
	//	cout<<endl;
	//}
	
	rep(i,ngroups.size())
		dfs(depth+1,dic,lst,ngroups[i],states,res);
}

void solve()
{
	int n,m; cin>>n>>m;
	vs dic(n);
	rep(i,n) cin>>dic[i];
	vs lsts(m);
	rep(i,m) cin>>lsts[i];
	
	rep(li,m){
		vi lens;
		map<int,int> ma;
		rep(i,n){
			int wsize=dic[i].size();
			if(ma.find(wsize)==ma.end())
				ma.insert(mp(wsize,ma.size()));
		}
		
		//puts("ma");
		//foreach(i,ma)
		//	cout<<i->first<<" "<<i->second<<endl;
		
		vvi groups(ma.size());
		rep(i,n){
			groups[ma[dic[i].size()]].push_back(i);
		}
		
		//puts("group");
		//rep(i,groups.size()){
		//	rep(j,groups[i].size())
		//		cout<<groups[i][j]<<" ";
		//	cout<<endl;
		//}
		
		vs states(n);
		rep(i,n)
			states[i]=string(dic[i].size(),'_');
		
		//puts("states");
		//rep(i,n)
		//	cout<<states[i]<<endl;
		
		vi res(n);
		//puts("dfs");
		rep(i,groups.size())
			dfs(0,dic,lsts[li],groups[i],states,res);
		
		//puts("res");
		//rep(i,n)
		//	cout<<res[i]<<" ";
		//cout<<endl;
		
		int ri=-1;
		rep(i,n){
			if(ri==-1 || res[i]>res[ri])
				ri=i;
		}
		cerr<<li<<"="<<li<<endl;
		cout<<dic[ri]<<(li==m-1?'\n':' ');
	}
}

int main()
{
	int cases; scanf("%d ",&cases);
	rep(i,cases){
		printf("Case #%d: ",i+1);
		solve();
	}
	
	return 0;
}
