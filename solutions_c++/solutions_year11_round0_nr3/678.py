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
	int n,a[1013];
	cin>>n;
	int ans=0,mm=1000000000,pr=0;
	for (int i=0;i<n;i++){
		cin>>a[i];
		pr^=a[i];
		ans+=a[i];
		mm=min(mm,a[i]);
	}
	if (pr!=0){
		cout<<"NO";
		return;
	}
	cout<<ans-mm;
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