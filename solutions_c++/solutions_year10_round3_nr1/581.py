#include <iostream>
#include <stdio.h>
using namespace std;

int n;
int a[1000], b[1000];

void solve() {
	int ans=0;
	for( int i=0; i<n; i++ ) {
		for( int j=i+1; j<n; j++ ) {

			if( ((a[j] < a[i]) && (b[j] > b[i])) || ((a[j] > a[i]) && (b[j] < b[i])) ) {
				ans++;
			}

		}
	}
	cout<<ans<<endl;
}
int main() {
	freopen("A-large.in", "rt", stdin);
	freopen("out.txt", "wt", stdout);
	int t;
	cin>>t;
	for( int i=0; i<t; i++ ) {
		cin>>n;
		for( int j=0; j<n; j++ ) {
			cin>>a[j]>>b[j];
		}

		cout<<"Case #"<<i+1<<": ";
		solve();



	}
}