#include<stdio.h>
#include<string.h>
#include<iostream>
#include<cmath>
#define fr(i,a,b) for(i=a;i<=b;i++)
using namespace std;
const int maxn=102;
char g[maxn][maxn];
int ans,i,n,m,ti,ca,x[maxn][maxn];
void dfs(int a,int b){
	if(a>n){
		ans++;
		return;
	}
	int c,d,i,xx,yy;
	if(g[a][b]=='|'){
		c=1;
		d=0;
	}
	if(g[a][b]=='-'){
		c=0;
		d=1;
	}
	if(g[a][b]=='/'){
		c=1;
		d=-1;
	}
	if(g[a][b]=='\\'){
		c=1;
		d=1;
	}
	for(i=1;i>=-1;i-=2){
		c*=i;
		d*=i;
		xx=(a+c-1+n)%n+1;
		yy=(b+d-1+m)%m+1;
		x[xx][yy]++;
		if(x[xx][yy]<2)
			dfs(a+b/m,b%m+1);
		x[xx][yy]--;
	}
}
int main(){
	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);
	cin>>ca;
	fr(ti,1,ca){
		cin>>n>>m;
		fr(i,1,n)
			scanf("%s",g[i]+1);				
		ans=0;
		memset(x,0,sizeof(x));
		dfs(1,1);
		cout<<"Case #"<<ti<<": "<<ans<<endl;
	}
}