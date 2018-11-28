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
	long long t,n,a[1000013];
	int c,l;
	cin>>l>>t>>n>>c;
	t*=2;
	for (int i=0;i<c;i++){
		cin>>a[i];
		a[i]*=2;
	}
	for (int i=c;i<n;i++){
		a[i]=a[i%c];
	}
	long long ans1=0,ans2=0;
	long long tt=t;
	int k;
	for (k=0;k<n;k++){
		if (tt<a[k]*2){
			break;
		}
		else{
			tt-=a[k]*2;
		}
	}
	if (k==n){
		cout<<(t-tt)/2;
		return;
	}
	ans1=t-tt;
	ans2=ans1;
	ans1+=a[k]*2;
	ans2+=tt+(a[k]-tt/2);
	k++;
	int l1=l,l2=l-1;
	sort(a+k,a+n);
	for (int i=n-1;i>=k;i--){
		if (l1>0){
			ans1+=a[i];
			l1--;
		}
		else{
			ans1+=a[i]*2;
		}
		if (l2>0){
			ans2+=a[i];
			l2--;
		}
		else{
			ans2+=a[i]*2;
		}
	}
	if (l==0){
		cout<<ans1/2;
		return;
	}
	cout<<min(ans1,ans2)/2;
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