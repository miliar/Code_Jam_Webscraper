/* Author: Zuo.Overmind.Zerg */
#include<cassert>
#include<cstdio>
#include<cstdlib>
#include<cstring>
//#include<algorithm>
//#include<deque>
//#include<functional>
//#include<iostream>
//#include<list>
//#include<map>
//#include<set>
//#include<vector>
//using namespace std;

typedef long long i64;
typedef unsigned u32;
template<class _> void maz(_ &a,const _ b) {if(b>a)a=b;}
template<class _> void miz(_ &a,const _ b) {if(b<a)a=b;}

i64 p[63];
i64 base;
int cat; i64 opt[20];
int S;

void work(i64 x) {
	if(x) {
		work(x>>1);
		putchar((x&1)?'1':'0');
	}
}

bool check(i64 x) {
	i64 _l=0,_r=(1ll<<30),_m,_u;
	while(_l<=_r) {
		_m=((_l+_r)>>1);
		_u=_m*_m;
		if(_u<x) {
			_l=_m+1;
		} else if(_u>x) {
			_r=_m-1;
		} else {
			printf("Case #%d: ",S);
			work(x);
			puts("");
			return true;
		}
	}
	return false;
}

bool dfs(int dep,i64 now) {
	if(dep==cat)return check(now);
	if(!dfs(dep+1,now))dfs(dep+1,now+opt[dep]);
}

void solve() {
	dfs(0,base);
}

void input() {
	static char buf[128];
	int i,e,len;
	scanf("%s",buf);
	len=strlen(buf);
	if(*buf=='?')*buf='1';
	base=0;
	cat=0;
	for(i=0;i<len;i++) {
		e=len-i-1;
		if(buf[i]=='1')base+=p[e];
		else if(buf[i]=='?')opt[cat++]=p[e];
	}
}

int main() {
	int T,i;
	for(i=0;i<63;i++)p[i]=(1ll<<i);
	scanf("%d",&T);
	for(S=1;S<=T;S++) {
		input();
		solve();
	}
	return 0;
}
