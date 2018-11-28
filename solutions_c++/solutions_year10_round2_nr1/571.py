#include <stdio.h>
#include <string.h>
#include <iostream>
#include <map>
#include <string>
#include <algorithm>
using namespace std;
int ans, n, m;
string tmp;
map<string ,bool> h;

bool cmp(const string &a, const string &b){
	return a>b;
}

void init(){
	h.clear();
	cin>>n>>m;
	for (int i=0; i<n; i++) {
		cin>>tmp;
		h[tmp] = true;
	}
	ans = 0;
	for (int i=0; i<m; i++) {
		cin>>tmp;
		if (h.count(tmp) == 0) { h[tmp] = true; ans++; }
		int len = tmp.length();
		for (int j=len-1; j>0; j--){
			if (tmp[j] == '/'){
				string sub=tmp.substr(0, j);
				if (h.count(sub) == 0) {
					h[sub] = true;
					ans++;
				} else break;
			}
		}
	}
}

int main(){
	int test; cin>>test;
	for (int cas=1; cas<=test; cas++){
		init();
		printf("Case #%d: %d\n", cas, ans);
	}
	return 0;
}
