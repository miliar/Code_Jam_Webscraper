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

int n;
pair <char, int> a[113];

int next(int i, char ch){
	for (int j=i;j<n;j++){
		if (a[j].first==ch){
			return a[j].second;
		}
	}
	return -1;
}

void solve(){
	cin>>n;
	for (int i=0;i<n;i++){
		cin>>a[i].first>>a[i].second;
	}
	int cr1=1,cr2=1;
	int ans=0;
	for (int i=0;i<n;i++){
		if (a[i].first=='O'){
			int nx=next(i,'B');
			while (a[i].second!=cr1){
				ans++;
				if (a[i].second>cr1){
					cr1++;
				}
				else{
					cr1--;
				}
				if (nx>=0){
					if (cr2>nx){
						cr2--;
					}
					else{
						if (cr2<nx){
							cr2++;
						}
					}
				}
			}
			ans++;
			if (nx>=0){
				if (cr2>nx){
					cr2--;
				}
				else{
					if (cr2<nx){
						cr2++;
					}
				}
			}
		}
		if (a[i].first=='B'){
			int nx=next(i,'O');
			while (a[i].second!=cr2){
				ans++;
				if (a[i].second>cr2){
					cr2++;
				}
				else{
					cr2--;
				}
				if (nx>=0){
					if (cr1>nx){
						cr1--;
					}
					else{
						if (cr1<nx){
							cr1++;
						}
					}
				}
			}
			ans++;
			if (nx>=0){
				if (cr1>nx){
					cr1--;
				}
				else{
					if (cr1<nx){
						cr1++;
					}
				}
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