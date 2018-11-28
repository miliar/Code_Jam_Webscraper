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
	//ios_base::sync_with_stdio(false);
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
	int n;
	cin>>n;
	li s = 0;
	double a[222];
	for(int i=0;i<n;++i){
		int x;
		cin>>x;
		a[i] = x;
		s+=x;
		
	}
	for(int i=0;i<n;++i){
		a[i]/=s;
	}
	
	for(int i=0;i<n;++i){
		double l=0, r=1;
		for(int j=0;j<200;++j){
			double c = (l+r)/2;
			double we = c + a[i];
			//cerr<<l<<' '<<r<<' '<<we<<endl;
			double theyneed = 0;
			for(int k=0;k<n;++k){
				theyneed += max(0.0, we - a[k]);
			}
			//cerr<<theyneed<<endl;
			
			if(theyneed <= 1){
				l = c;
			}
			else
				r = c;
		}
		printf("%.18lf ", l*100);
	}
	return 0;
}