#include<map>
#include<iostream>
#include<vector>
#include<algorithm>
#include<cstdio>
using namespace std;
int lim = -2000000;

int get(map<int, int>& p){
	//cout << endl;
	for(typeof(p.begin()) it = p.begin(); it != p.end(); it++){
	//	cout << it->first << " " << it->second << endl;
		if(it->second > 1) return it->first;
	}
	return lim;
}

int main(){
	int t; cin >> t;
	for(int tt = 1; tt <= t; tt++){
		int n; cin >> n;
		map<int, int> p;
		for(int i = 0; i < n; i++){
			int a, b; scanf("%d %d", &a, &b);
			p[a] = b;
		}
		int veces = 0;
		while(true){
			int index = get(p);
			if(index == lim) break;
			veces++;
			p[index - 1]++;
			p[index + 1]++;
			p[index] -= 2;
			if(p[index] == 0) p.erase(index);
		}
		printf("Case #%d: %d\n", tt, veces);
	}
}
