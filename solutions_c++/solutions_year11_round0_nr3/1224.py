#include <cstdio>
#include <vector>
#include <stack>
#include <algorithm>
#include <iostream>
#include <string>
#include <cstring>
#include <queue>
#include <cmath>
using namespace std;

int solve(){
	int n;
	cin>>n;
	int a[1013];
	int t=0;
	for(int i=0; i<n; i++){
		cin>>a[i];
		t^=a[i];
	}
	if(t!=0) return -1;
	sort(a,a+n);
	int ans=0;
	for(int i=1; i<n; i++) ans+=a[i];
	return ans;
}

int  main(){
	int t;
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	cin>>t;
	int k;
	for(int i=0; i<t; i++){
		k=solve();
		if(k>-1){
			cout<<"Case #"<<i+1<<": "<<k<<endl;
		}else{
			cout<<"Case #"<<i+1<<": "<<"NO"<<endl;
		}
	}
	return 0;
}