#include <vector>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <string>
#include <cmath>
#include <set>
#include <cassert>
#include <cstdio>
#include <queue>
using namespace std;
#define LET(x,a) __typeof(a) x(a)
#define FOR(i,a,b) for(int i=a;i!=(b);++i)
#define EACH(it,v) FOR(it,(v).begin(),(v).end())
#define REP(i,n) FOR(i,0,n)
#define pb push_back
#define GI ({int t;scanf("%d",&t);t;})
#define GII ({LL t;scanf("%Ld",&t);t;})
#define INF (int)1e8
#define MAX 100010
#define mkp make_pair
typedef long long LL;
typedef double D;
#define sz size()
#define bset(i,j) (((1)<<(j))&(i))
#define VI vector<int>

int kk, cnt[2000][30];
char full[2000];
vector <string> v;
int go(VI t)
{
	string ss="";
	REP(i,v.sz) {
		REP(j,t.sz) ss+=v[i][t[j]];
	}
	int ans=1;
	ss+="A";
	FOR(i,1,ss.sz) {
		if(ss[i] == ss[i-1]) continue;
		else {
			ans++;
		}
	}
	
	return ans-1;
}


int main()
{
	int t=GI;
	
	REP(kase,t) {
		printf("Case #%d: ", kase+1);
		kk=GI;
		const int k=kk;
		memset(cnt,0,sizeof(cnt));
		string s;
		cin>>s;
		v.clear();
		int num=s.sz/k;
		REP(i,num) {
			full[i] = s[i*k];
			string tmp=""; 
			for(int j=i*k; tmp.sz<k; j++) {
				if(s[j] != full[i]) { 
					full[i]='#'; 
				}
				tmp += s[j];
			}
			if(tmp.sz) v.pb(tmp);
		}
		REP(i,v.sz) {
			REP(j,v[i].sz) cnt[i][v[i][j]-'a']++;
		
		}
		kk=k;
		int a[k], ans=INF;
		REP(i,k) a[i]=i;
		do {
			VI vv;
			REP(i,k) vv.pb(a[i]);
			ans <?= go(vv);
		}
		while(next_permutation(a,a+k));
		
		printf("%d \n", ans);
	}		
	
}
	
	
	
	
	
	
	
	
	
