#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <deque>
#include <complex>
#include <algorithm>
#include <cstdio>
#include <cmath>
#include <cstring>

#define REP(i,x) for(int i=0 ; i<(int)(x) ; i++)
#define ALL(x) (x).begin(),(x).end()
#define LL long long

using namespace std;

struct Vine{
	LL d,l;
	Vine(int _d,int _l):d(_d),l(_l){}
	Vine(){}
};

int D;
vector<vector<LL> > memo;

bool dfs(int a,int b,vector<Vine> &v){
	// 
	if(memo[a][b]!=-1)return memo[a][b]==1;
	LL apos = v[a].d;
	LL bpos = v[b].d;
	LL sub = min(bpos-apos,v[b].l);
	LL start = bpos-sub;
	LL next=start+2LL*sub;
	//cout << apos << " " << next << endl;
	if(next>=D){
		memo[a][b] = 1;
		return true;
	}
	for(int i=b+1 ; i<(int)v.size() ; i++){
		if(next>=v[i].d){
			if(dfs(b,i,v)){
				memo[a][b] = 1;
				return true;
			}
		}
		else break;
	}
	memo[a][b] = 0;
	return false;
}

string solve(){
	int N;
	scanf("%d",&N);
	vector<Vine> vines(N,Vine(0,0));
	REP(i,N)scanf("%lld%lld",&vines[i].d,&vines[i].l);
	scanf("%d",&D);
	LL apos = 0;
	LL bpos = vines[0].d;
	LL sub = vines[0].d;
	LL next = 2LL*sub;
	if(2*sub>=D)return "YES";
	memo.assign(N,vector<LL>(N,-1));
	for(int i=1 ; i<(int)vines.size() ; i++){
		if(next>=vines[i].d){
			if(dfs(0,i,vines))return "YES";
		}
		else break;
	}
	return "NO";
}

int main(){
	int T;
	scanf("%d",&T);
	REP(tt,T){
		cout << "Case #" << tt+1 << ": " << solve() << endl;
	}
	return 0;
}
