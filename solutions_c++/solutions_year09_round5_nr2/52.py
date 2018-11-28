#include<iostream>
#include<vector>
#include<string>
#include<cmath>
#include<algorithm>
#include<sstream>
#define fr(i,a,b) for(i=a;i<=b;++i)
using namespace std;
int ti,ca,n,ans[1000],tot[1000],len,k;
char p[1000],dic[1000][1000],l[1000];
void init(){
	cin>>p>>k;
	len=strlen(p);
	cin>>n;
	int i;
	fr(i,1,n){
		cin>>dic[i];
		l[i]=strlen(dic[i]);
	}
}
void dfs(int now,int last){
	int i,j;
	if(now>1){
		int value=0,tmp=1;
		fr(i,0,len-1)
			if(p[i]=='+'){
				value+=tmp;
				tmp=1;
			}
			else
				tmp=(tmp*tot[p[i]])%10009;
		value+=tmp;
		ans[now-1]=(ans[now-1]+value)%10009;
	}
	if(now>k)
		return;
	fr(i,last+1,n){
		fr(j,0,l[i]-1)
			++tot[dic[i][j]];
		dfs(now+1,0);
		fr(j,0,l[i]-1)
			--tot[dic[i][j]];
	}
}
void work(){
	memset(ans,0,sizeof(ans));
	dfs(1,0);
	int i;
	fr(i,1,k)
		cout<<" "<<ans[i];
	cout<<endl;
}
int main(){
	freopen("b1.in","r",stdin);
	freopen("b1.out","w",stdout);
	cin>>ca;
	fr(ti,1,ca){
		init();
		printf("Case #%d:",ti);
		work();
	}
}