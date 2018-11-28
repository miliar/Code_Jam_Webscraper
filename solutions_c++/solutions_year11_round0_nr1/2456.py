#include <iostream>
#include <cstdlib>
#include <cstdio>

using namespace std;

int main(){
	int t;
	cin>>t;
	for(int i=1;i<=t;i++){
			
		int lp[]={1,1};
		int lt[]={0,0};
		int n;
		cin>>n;
		int ct=0;
		for(int j=0;j<n;j++){
			char b=3;
			cin>>b;
			while(b!='O' && b!='B'){
				cin>>b;
			}
			if(b=='O')
				b=0;
			else
				b=1;
			int vpos;
			cin>>vpos;
			int dp=abs(lp[b]-vpos);
			int dt=ct-lt[b];
			ct=lt[b]+max(dp,dt)+1;
			lt[b]=ct;
			lp[b]=vpos;
		}		
		cout<<"Case #"<<i<<": "<<ct<<endl;		
	}
	return 0;
}
