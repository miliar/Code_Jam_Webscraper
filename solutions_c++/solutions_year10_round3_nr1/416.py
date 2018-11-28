#include<iostream>
using namespace std;
int main(){
	int t,n,m;
	int h[1000][2];
	int ans;
	cin>>t;
	for(int tt=1;tt<=t;++tt){
		cin>>n;
		for(int x=0;x<n;++x)
			cin>>h[x][0]>>h[x][1];
		ans=0;
		for(int x=0;x<n;++x){
			for(int y=0;y<x;++y){
				if(h[x][0]>h[y][0]&&h[x][1]>h[y][1])
					continue;
				if(h[x][0]<h[y][0]&&h[x][1]<h[y][1])
					continue;
				++ans;
			}
		}
		printf("Case #%d: %d\n",tt,ans);
	}
	
}
