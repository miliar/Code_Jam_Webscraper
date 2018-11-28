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
	int wo=0,wb=0,no=1,nb=1;
	char ch;
	int cn;
	int ans=0;
	for(int i=0; i<n; i++){
		cin>>ch>>cn;
		if(ch=='O'){
			int dist=abs(cn-no);
			dist=max(0,dist-wo)+1;
			wo=0;
			wb+=dist;
			ans+=dist;
			no=cn;
		}else{
			int dist=abs(cn-nb);
			dist=max(0,dist-wb)+1;
			wb=0;
			wo+=dist;
			ans+=dist;
			nb=cn;
		}
	}
	return ans;

}

int  main(){
	int t;
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	cin>>t;
	for(int i=0; i<t; i++){
		cout<<"Case #"<<i+1<<": "<<solve()<<endl;
	}
	return 0;
}