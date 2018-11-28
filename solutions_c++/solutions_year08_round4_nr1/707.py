/*
	Author : Vinay Emani
	Contact : VinayEmani AT gmail DOT com
*/
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
#define MAXN 25011

int m,v;
int val[MAXN];
int leaf[MAXN];
int L[MAXN],l;
int I[MAXN],in;
lint dp[MAXN][2];
int gate[MAXN];
int change[MAXN];
int inf = 1<<23;
void doit(){
	SET(leaf,true);
	int i;l=in=0;
	FORN(i,1,m+1)if(2*i<=m){
		leaf[i]=false;
	}
	FORN(i,1,m+1)if(!leaf[i])I[in++]=i;
	else L[l++]=i;
	SET(dp,-1);
	return;
};

int calc(int a,int b,int g){
	if(g)return a&b;
	return a|b;
};

lint solve(int x,int v2){
	if(val[x]==v2)return 0;
	if(leaf[x])return inf;
	lint& ans = dp[x][v2];
	if(ans==-1){
		ans=inf;
		if(true){
			lint a1 = solve(x+x,1);
			lint a2 = solve(x+x,0);
			lint b1 = solve(x+x+1,1);
			lint b2 = solve(x+x+1,0);
			if(calc(1,1,gate[x])==v2)
				ans=min(ans,a1+b1);
			if(calc(1,0,gate[x])==v2)
				ans=min(ans,a1+b2);
			if(calc(0,0,gate[x])==v2)
				ans=min(ans,a2+b2);
			if(calc(0,1,gate[x])==v2)
				ans=min(ans,a2+b1);
		}
		if(change[x]){
		if(calc(val[x+x],val[x+x+1],!gate[x])==v2)
			ans=1;
			lint a1 = solve(x+x,1);
			lint a2 = solve(x+x,0);
			lint b1 = solve(x+x+1,1);
			lint b2 = solve(x+x+1,0);
			if(calc(1,1,!gate[x])==v2)
				ans=min(ans,1+a1+b1);
			if(calc(1,0,!gate[x])==v2)
				ans=min(ans,1+a1+b2);
			if(calc(0,0,!gate[x])==v2)
				ans=min(ans,1+a2+b2);
			if(calc(0,1,!gate[x])==v2)
				ans=min(ans,1+a2+b1);		
		}
	}
	return ans;
};

int main(){
	int cas,t=0;
	cin >> cas;
	while(cas--){
		cin >> m >> v;
		SET(val,-1);
		doit();
		int i;
		SET(change,false);
		FOR(i,(m-1)/2){
			int g,c;
			cin >> g >> c;
			gate[I[i]]=g;
			change[I[i]]=c;
		}
		//cout << "ok" << endl;
		FOR(i,(m+1)/2)
			cin >> val[L[i]];
		for(i=m;i>=1;i--)if(!leaf[i]){
			if(gate[i])val[i]=val[2*i]&val[2*i+1];
			else val[i]=val[2*i]|val[2*i+1];
		}
		t++;
		int answer = solve(1,v);
		cout << "Case #" << t << ": ";
		if(answer >= inf){
			cout << "IMPOSSIBLE" << endl;
		}
		else{
			cout << answer << endl;
		}
	}
	return 0;
}
