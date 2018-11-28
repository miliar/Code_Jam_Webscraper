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
	int n;
	cin>>n;
	int a[1013];
	for (int i=0;i<n;i++){
		cin>>a[i];
		a[i]--;
	}
	bool b[1013];
	memset(b,0,sizeof(b));
	int ans=0;
	for (int i=0;i<n;i++){
		if (!b[i]){
			int cr=a[i],c=1;
			b[i]=1;
			while (cr!=i){
				b[cr]=1;
				cr=a[cr];
				c++;
			}
			if (c>1){
				ans+=c;
			}
		}
	}
	cout<<ans;
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