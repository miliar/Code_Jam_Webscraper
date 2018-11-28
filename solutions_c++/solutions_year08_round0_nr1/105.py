#include <iostream>
#include <cstring>
#include <string>
#include <sstream>
#include <queue>
#include <map>
#include <set>
#include <vector>
#include <utility>
using namespace std;
#define lint long long
#define SZ(s) ((int)(s.size()))
#define PB push_back
#define MP make_pair
#define FORN(i,a,b) for(i=(int)(a);i<(int)(b);i++)
#define FOR(i,n) FORN(i,0,n)
#define FOREACH(it,S) for(typeof(S.begin()) it = S.begin();it != S.end();it++)
#define SET(x,a) memset(x,a,sizeof x)
#define BEG(a) a.begin()
#define END(a) a.end()
#define ALL(a) BEG(a),END(a)

int s,q;
string names[128];
string qs[1024];
int ret[1024][128];
int len[1024][128];
char buf[1024];int inf = 1<<23;
int solve(int x,int p){
	if(x>=q)return 0;
	int& ans = ret[x][p+1];
	if(ans<0){
		ans=inf;
		int i;
		FOR(i,s)if(i!=p && len[x][i]>0)
			ans<?=1+solve(x+len[x][i],i);
	}
	return ans;
};

int main(){
	int t;
	cin.getline(buf,1000);
	sscanf(buf,"%d",&t);
	map<string,int> mp;
	for(int cases=1;cases<=t;cases++){
		mp.clear();
		cin.getline(buf,1000);
		sscanf(buf,"%d",&s);
		int i,j;
		FOR(i,s){
			cin.getline(buf,1000);
			names[i] = string(buf);
			mp[names[i]]=i;
			//cout<<names[i]<<endl;
		}
		cin.getline(buf,1000);
		sscanf(buf,"%d",&q);
		FOR(i,q){
			cin.getline(buf,1000);
			qs[i] = string(buf);
			//cout<<qs[i]<<endl;
		}
		if(q==0){
			cout<<"Case #"<<cases<<": "<<0<<endl;
			continue;
		}
		SET(ret,-1);
		FOR(i,q)FOR(j,s)len[i][j]=inf;
		FOR(i,q)FORN(j,i,q)len[i][mp[qs[j]]]<?=j-i;
		int ans = solve(0,-1)-1;
		cout << "Case #"<<cases<<": "<<ans<<endl;
	}
	return 0;
}
