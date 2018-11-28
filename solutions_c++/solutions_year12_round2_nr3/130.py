#include <iostream>
#include <cstdio>
#include <set>
#include <vector>
#include <map>
#include <string>
#include <cstring>
#include <cmath>
#include <memory.h>
#include <algorithm>
#include <cstdlib>
#include <cassert>
#include <sstream>
#include <fstream>
using namespace std;


#define pb push_back
#define mp make_pair

typedef long long li;
typedef vector<li> vi;
typedef pair<int, int> pi;
li solve();
int main() {
	freopen("input", "r", stdin);
	freopen("output","w", stdout);
	ios_base::sync_with_stdio(false);
	int t;
	cin>>t;
	string s;
	getline(cin,s);
	for(int i=1;i<=t;++i){
		cout<<"Case #"<<i<<": ";
		solve();
		cout<<'\n';
	}
	return 0;
}

li solve(){
	cout<<'\n';
	int n;
	cin>>n;
	int a[200];
	for(int i=0;i<n;++i){
		cin>>a[i];
	}
	for(int i=1;i<(1<<n);++i){
		li si = 0;
		for(int j=0;j<n;++j){
			if(i & (1<<j)){
				si +=a[j];
			}
		}
		int obr = (1<<n) - i -1;
		for (int j=obr; j; j=(j-1)&obr) {
			li sj = 0;
			for(int k=0;k<n;++k){
				if(j & (1<<k)){
					sj +=a[k];
				}
			}
			if(si == sj){
				for(int t=0;t<n;++t){
					if((1<<t) & i)
						cout<<a[t]<<' ';
				}
				cout<<'\n';
				for(int t=0;t<n;++t){
					if((1<<t) & j)
						cout<<a[t]<<' ';
				}
				return 0;
			}
		}
	}
	cout<<"Impossible";
	return 0;
}