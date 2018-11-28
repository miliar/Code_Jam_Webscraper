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
double solve(){
	int n;
	cin>>n;
	int cnt=0;
	int a[1013];
	int b[1013];
	for(int i=0; i<n; i++){
		cin>>a[i];
		b[i]=a[i];
	}
	sort(a,a+n);
	for(int i=0; i<n; i++){
		if(a[i]!=b[i]) cnt++;
	}
	return (double)cnt;

}
int  main(){
	int t;
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	cin>>t;
	for(int i=0; i<t; i++){
		cout<<"Case #"<<i+1<<": ";
		cout.setf(ios::fixed);
		cout.precision(6);
		cout<<solve();
		cout<<endl;
	}
	return 0;
}