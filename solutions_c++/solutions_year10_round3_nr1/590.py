#include <vector>
#include <list>
#include <set>
#include <stack>
#include <algorithm>
#include <iostream>
#include <string>
#include <cmath>
#include <map>

#pragma comment(linker, "/STACK:16000000")

using namespace std;

int sgnn(int a){
	if (a<0){
		return -1;
	}
	return 1;
}

void solve_gcj1c(){
	int n;
	cin>>n;
	pair <int,int> a[10010];
	for (int i=0;i<n;i++){
		cin>>a[i].first>>a[i].second;
	}
	int ans=0;
	for (int i=0;i<n;i++){
		for (int j=i+1;j<n;j++){
			if (sgnn(a[i].first-a[j].first)!=sgnn(a[i].second-a[j].second)){
				ans++;
			}
		}
	}
	cout<<ans;
	return;
}

int main(){
	freopen("input.txt","rt",stdin);
	freopen("output.txt","wt",stdout);	
	int z;
	cin>>z;
	for (int t=0;t<z;t++){
		cout<<"Case #"<<t+1<<": ";
		solve_gcj1c();
		cout<<endl;
	}
	return 0;
}