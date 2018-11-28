#include <cstdio>
#include <string>
#include <cstring>
#include <map>
#include <queue>
#include <iostream>
#include <vector>
#include <cmath>
#include <cstdlib>
#define maxl 100

using namespace std;

typedef long long ll;

int len;
bool flag;
char ans3[1000],ans2[10000],ans[1000],s[1000];
ll st;
ll two[70];

ll sq(ll x){
	ll temp=(ll)(sqrt((double)x)+0.1);
	return temp;
}

void fit(ll a){
	a=a*a;
	int i;
	for(i=len;i>0;--i){
		ll temp=a%2;
		a=a/2;
		if(temp==1){
			ans3[i]='1';
			if(s[i]=='0')return;
		}else {
			ans3[i]='0';
			if(s[i]=='1')return;
		}
	}
	for(i=1;i<=len;++i)ans2[i]=ans3[i];
	flag=true;
}

void fuckit(int k){
	ll st2=st,m1,m2;
	for(int i=k;i<=len;++i)if(s[i]=='?')st2=st2+two[len-i];
	m1=sq(st);m2=sq(st2)+1;
	while(!flag && m1<m2){
		fit(m1);
		m1=m1+1;
	}
}
int tot=0;

void dfs(int k,int now){
	if(flag)return;
	if(k>len){
		//if(++tot%1000==0)cout<<tot<<endl;
		ll mid=sq(st);
		if(mid*mid==st){
			for(int i=1;i<=len;++i)ans2[i]=ans[i];
			flag=true;
		}
		return;
	}
	if(now==21){
		fuckit(k);
		return;
	}
	if(s[k]!='?')dfs(k+1,now);else {
		ans[k]='0';
		dfs(k+1,now+1);
		ans[k]='1';
		st=st+two[len-k];
		dfs(k+1,now+1);
		st=st-two[len-k];
	}
}
		
		
		
void solve(){
	scanf("%s",s+1);
	len=strlen(s+1);
	st=0;
	int i;
	for(i=1;i<=len;++i){
		ans[i]=s[i];
		if(s[i]=='1')st=st+two[len-i];
	}
	flag=false;
	dfs(1,0);
	for(i=1;i<=len;++i)printf("%c",ans2[i]);
	printf("\n");
}
	
	

int main(){
	int t,i;
	two[0]=1;
	for(i=1;i<=63;++i)two[i]=two[i-1]*2;
	scanf("%d",&t);
	for(i=1;i<=t;++i){
		printf("Case #%d: ",i);
		solve();
	}
}
