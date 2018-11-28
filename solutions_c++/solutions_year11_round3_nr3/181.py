#include <string.h>
#include <stdio.h>
#include <sstream>
#include <vector>
#include <list>
#include <set>
#include <stack>
#include <algorithm>
#include <iostream>
#include <string>
#include <bitset>
#include <cstring>
#include <queue>
#include <cmath>
#include <map>
#include <iterator>
#define EPS 1e-9
#pragma comment(linker, "/STACK:256000000")

using namespace std;

void solve(){
	int n,l,r,a[113];
	cin>>n>>l>>r;
	for (int i=0;i<n;i++){
		cin>>a[i];
	}
	for (int i=l;i<=r;i++){
		bool pp=1;
		for (int j=0;j<n;j++){
			if (!(a[j]==0 || i%a[j]==0 || a[j]%i==0)){
				pp=0;
			}
		}
		if (pp){
			cout<<i;
			return;
		}
	}
	cout<<"NO";
	return;
}

int main(){
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	ios::sync_with_stdio(0);
	int t;
	cin>>t;
	for (int z=1;z<=t;z++){
		cout<<"Case #"<<z<<": ";
		solve();
		cout<<endl;
	}
	return 0;
	//cout.setf(ios::fixed);cout.precision(20);
}