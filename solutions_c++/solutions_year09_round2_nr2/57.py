#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <cassert>

using namespace std;

#define Eo(x) { cerr << #x << " = " << x << endl; }

vector<int> a;

void least(string& n, int p, vector<int> b){
	int l = 0;
	for (int i = p; i < n.size(); i++){
		while (!b[l]) l++;
		assert(l < 10);
		b[l]--;
		n[i] = l+'0';
	}
}

bool go(string& n, int p){
	vector<int> b(a);
	for (int i = 0; i < p; i++)
		b[n[i]-'0']--;
	int f = n[p]-'0';
	int i;
	for (i = f+1; i < 10 && !b[i]; i++) ;
	if (i == 10) return false;
	n[p] = '0'+i;
	b[i]--;
	least(n,p+1,b);
	return true;
}

int main(){
	int T; cin >> T;
	a.resize(10);
	for (int _ = 0; _ < T; _++){
		string n; cin >> n;
		for (int i = 0; i < 10; i++) a[i] = 0;
		for (int i = 0; i < n.size(); i++)
			a[n[i]-'0']++;
		bool did = false;
		for (int i = n.size()-1; i >= 0; i--){
			if (go(n,i)){
				did = true;
				printf("Case #%d: %s\n",_+1,n.c_str());
				break;
			}
		}
		if (did) continue;
		n = '0' + n;
		a[0]++;
		assert(go(n,0));
		printf("Case #%d: %s\n",_+1,n.c_str());
	}
	return 0;
}
