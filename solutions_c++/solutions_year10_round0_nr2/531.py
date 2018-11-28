#include <fstream>
#include <cmath>
#include <string>
#include <map>
#include <vector>
#include <set>
#include <cstdlib>
#include <algorithm>
#define forn(i,n) for(int i = 0; i < n; i++)
#define lng long long
#define Uint unsigned
using namespace std;
#ifdef ___ASDASD___
	ifstream cin("input.txt");
	ofstream cout("output.txt");
#endif
#ifndef ___ASDASD___
#include <iostream>
#endif
lng f(lng y){
	return 0ll;
}
//////
//////
///////
///////
int NOD(int a, int b){
	while(a){
		b %= a;
		swap(a,b);
	}
	return b;
}
int main() {
	int t;
	cin>>t;
	forn(i,t){
		int n;
		cin>>n;
		int k = n - 1;
		vector<int> T(n);
		forn(j,n){
			cin>>T[j];
		}
		sort(T.begin(),T.end());
		vector<int> diff(k);
		forn(j,k){
			diff[j] = abs(T[j] - T[j + 1]);
		}
		forn(j,k - 1){
			diff[0] = NOD(diff[0],diff[j+1]);
		}
		cout<<"Case #"<<(i + 1)<<": "<<((T[0] % diff[0] == 0)? 0 :(diff[0] - T[0] % diff[0]))<<endl;
	}
}
