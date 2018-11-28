#include<iostream>
#include<vector>
#include<string>
#include<cmath>
#include<algorithm>
#include<sstream>
#include<stdio.h>
#include<string.h>
#define fr(i,a,b) for(i=a;i<=b;i++)
using namespace std;
const int maxn=1002;
int i,j,n,x[maxn],ti,ca,ans,now,nxt,tot;
int main(){
	freopen("d2.in","r",stdin);
	freopen("d2.out","w",stdout);
	cin>>ca;
	fr(ti,1,ca){
		cin>>n;
		fr(i,1,n)
			cin>>x[i];
		ans=0;
		fr(i,1,n){
			if(x[i]==0)
				continue;
			tot=0;
			now=i;
			do{
				nxt=x[now];
				++tot;
				x[now]=0;
				now=nxt;
			}while(now!=i);
			if(tot>1)
				ans+=tot;
		}
		cout<<"Case #"<<ti<<": "<<ans<<endl;
	}
}