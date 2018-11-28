#include <iostream>
#include <sstream>
#include <cmath>
#include <vector>
#include <string>
#include <algorithm>
#include <queue>
#include <map>

#define ll long long 
#define pb push_back
#define mp make_pair
#define VI vector <int>
#define PII pair <int,int>
#define clr(x,y) memset(x,y,sizeof x)
#define FOR(x,y,z) for (x=(y);x<=(z);++x)
#define ROF(x,y,z) for (x=(y);x>=(z);--x)
#define PDD pair <double,double>
#define x first
#define y second

using namespace std;

int orz[110][26],now[26],p[110],fact[101],n,i,j,limk,k,test,tt,len;
int res[26];
string s,d[10000];

void work(){	
	int i,j,l;
	clr(now,0);
	FOR(i,1,k) FOR(j,0,25) now[j]+=orz[p[i]][j];
	l=fact[k];
	FOR(i,1,k){
		for (j=i;p[j]==p[i] && j<=k;++j);
		l/=fact[j-i];
		i=j-1;
	}
	int last=1 , sum=0;
	FOR(i,0,len-1) 
		if (s[i]=='+')sum+=last , last=1;
		else last*=now[s[i]-'a'];
	sum+=last;
	res[k]=(res[k]+(ll)l*sum)%10009;
}

void solve(int x,int last){
	if (last>n) return;
	if (x>k) { work(); return; }
	p[x]=last; solve(x+1,last);
	solve(x,last+1);
}

int main(){
	freopen("B-small-attempt1.in","r",stdin);
	freopen("B-small-attempt1.out","w",stdout);
	cin>>tt;
	fact[1]=1;
	FOR(i,2,10) fact[i]=fact[i-1]*i;
	FOR(test,1,tt){
		cin>>s>>limk>>n; len=s.size();
		FOR(i,1,n) 
			cin>>d[i];
		clr(orz,0); clr(res,0);
		FOR(i,1,n) FOR(j,0,d[i].size()-1) orz[i][d[i][j]-'a']++;
		FOR(k,1,limk) solve(1,1);
		printf("Case #%d: ",test);
		FOR(i,1,limk) cout<<res[i]<<' ';
		cout<<endl;
	}
}