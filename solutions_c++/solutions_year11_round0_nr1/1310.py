#include <cstdio>
#include <iostream>
using namespace std;



int max(int a,int b){return a>b?a:b;}
int abs(int a){
	return a>0?a:-a;
}
int main(){
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);

	int T,n,ans,i,j,now,x;
	int p[2],t[2];
	char c;
	cin>>T;
	for(i=1;i<=T;++i){
		p[0]=p[1]=1;
		t[0]=t[1]=0;
		cin>>n;
		for(j=1;j<=n;++j){
			cin>>c>>now;
			x=(c=='O')?0:1;
			t[x]=max(t[x]+abs(now-p[x])+1,t[1-x]+1);
			p[x]=now;
		}
		ans=max(t[0],t[1]);
		printf("Case #%d: %d\n",i,ans);
	}
	return 0;
}
