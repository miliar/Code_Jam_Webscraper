#include <iostream>
#include <cstdio>
#include <cstdlib>
using namespace std;

int n;
int nxt[10];
int nxt0[10];
int h[10];

void solve(){
	cin>>n;
	for (int i=0; i<n-1; ++i)
		cin>>nxt[i];
	for (int i=0; i<10000000; ++i){
		for (int j=0; j<n; ++j)
			h[j]=rand()%55;
		for (int j=0; j<n-1; ++j){
			nxt0[j]=j+1;
			for (int k=j+1; k<n; ++k)
				if ((h[k]-h[j])*(nxt0[j]-j)>(h[nxt0[j]]-h[j])*(k-j)) nxt0[j]=k;
			if (nxt0[j]+1!=nxt[j])
				goto l;
		}
		for (int j=0; j<n; ++j){
			cout<<h[j]<<' ';
		}
		return;
		l:;
	}
	cout<<"Impossible";
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