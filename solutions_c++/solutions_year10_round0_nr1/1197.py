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
	ifstream cin("A-large.in");
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
vector<int> p;

void make_set(int v){
	p[v] = v;
}
int find_set(int v){
	if(p[v] == v) return v;
	return p[v] = find_set(p[v]);
}

int unite(int a,int b){
	a = find_set(a);
	if(rand() & 1)
		swap(a,b);
	p[a] = b;
	return b;
}

int main() {
	int t;
	cin>>t;
	for(int i = 0; i < t; i++){
		int n,k;
		cin>>n>>k;
		int dvan = 1;
		for(int k = 0; k < n; k++){
			dvan *= 2;
		}
		int a = k % dvan;
		cout<<"Case #"<<(i + 1)<<": "<<((a+1 == dvan)?"ON":"OFF")<<endl;
	}
}
