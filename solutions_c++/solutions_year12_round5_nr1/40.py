#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;

int n;
int l[1000];
int p[1000];

pair<int, int> v[1000];

void solve(){
	cin>>n;
	for (int i=0; i<n; ++i)
		cin>>l[i];
	for (int i=0; i<n; ++i)
		cin>>p[i];
	for (int i=0; i<n; ++i){
		v[i]=make_pair(l[i]*p[i], n-1-i);
	}
	sort(v, v+n);
	reverse(v, v+n);
	for (int i=0;i<n; ++i)
		cout<<n-1-v[i].second<<' ';
	cout<<endl;
}

int main(){
	freopen("input.txt", "r", stdin);
	freopen("output.txt","w", stdout);
	int t;
	cin>>t;
	for (int i=0; i<t; ++i){
		cout<<"Case #"<<i+1<<": ";
		solve();
	}
}