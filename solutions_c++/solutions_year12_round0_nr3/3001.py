#include <iostream>
#include <cstdio>
#include <string>
#include <cmath>
using namespace std;

const int MAX_SIZE = 90000000;
int n,m,ans,len;
int vis[MAX_SIZE];

int getLen(int a){
	int n_=a;
	int l=0;
	while(n_){
		l++;
		n_/=10;
	}
	return l;
}

int getHigh(int len,int i,int index){
	return i/(int)pow(10,len-index);
}
int getLow(int len,int i,int index){
	return i%(int)pow(10,len-index);
}

void search(int num){
	int i,j,l;
	l=getLen(num);

	for(i=1;i<l;i++){
		int t=getHigh(l,num,i)+getLow(l,num,i)*pow(10,i);
		if(t>num&&t>=n&&t<=m){
			char ss[10]={0};
			sprintf(ss,"%d%d",num,t);
			
			long tt=atol(ss);
			if(!vis[tt]){
				ans++;
				vis[tt]=1;
			}
		}

	}
}
int solve(){
	int i,j;
	for(i=n;i<=m;i++){
		search(i);
	}
	return ans;
}	


int main()
{
	//freopen("C-small-attempt0.in","r",stdin);
	//freopen("C.out","w",stdout);
	int T,Case,i;
	cin>>T;
	Case=1;
	while(Case<=T){
		cout<<"Case #"<<Case++<<": ";
		memset(vis,0,sizeof(vis));
		ans=0;
		cin>>n>>m;
		solve();
		cout<<ans<<endl;
	}
	return 0;
}
