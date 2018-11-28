#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<string>
#include<vector>
#include<map>
#include<set>
#include<queue>
#include<bitset>
#include<cassert>

using namespace std;

typedef long long ll;
typedef pair<int,int> pint;
typedef vector<int> vint;

#define mp make_pair
#define pb push_back
#define REP(i,a,b) for(int i=a;i<b;++i)
#define rep(i,n) REP(i,0,n)

int t;

int main(){
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	cin>>t;
	REP(cas,1,t+1){
		string st;
		cin>>st;
		vint hoge(0x100,-1);
		hoge[st[0]]=1;
		int cnt=0;
		REP(i,1,st.length()){
			if(hoge[st[i]]!=-1)continue;
			if(++cnt==1)hoge[st[i]]=0;
			else hoge[st[i]]=cnt;
		}
		ll ans=0;
		if(++cnt==1)++cnt;
		REP(i,0,st.length()){
			ans=ans*cnt+hoge[st[i]];
		}
		printf("Case #%d: %lld\n",cas,ans);
	}
	return 0;
}
