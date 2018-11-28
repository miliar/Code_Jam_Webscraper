#include <iostream>
#include<cstdio>
using namespace std;

int l[101000], d[101000];
int a[101000];
int was[101000];
int n;
int D;

void solve(){
	cin>>n;
	for (int i=0;i<n; ++i)
		cin>>d[i]>>l[i], a[i]=0;
	cin>>D;
	a[0]=d[0];
	for (int i=0; i<n; ++i){
		for (int j=i+1; a[i]+d[i]>=d[j] && j<n; ++j){
			a[j]=max(a[j], min(d[j]-d[i], l[j]));
		}
		if (a[i]+d[i]>=D){
			cout<<"YES";
			return;
		}
	}
	cout<<"NO";
}

int main(){
	freopen("input.txt","r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin>>t;
	for (int i=1; i<=t; ++i){
		cout<<"Case #"<<i<<": ";
		solve();
		cout<<endl;
		cerr<<i<<endl;
	}
}