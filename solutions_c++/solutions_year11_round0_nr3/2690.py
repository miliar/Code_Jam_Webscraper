#include <iostream>

using namespace std;

#define for0(i,n) for(int i = 0; i < (n); i ++)

int n;

int vals[10000];
int colour[10000];

int dfs(int i) {
	if (i == n) {
		int p1 = 0, p2 = 0;
		int v1 = 0, v2 = 0;
		for0(j,n) {
			// cout << colour[j] << "," << vals[j] << " ";
			if (colour[j] == 0) {p1 = p1 ^ vals[j]; v1 += vals[j];}
			if (colour[j] == 1) {p2 = p2 ^ vals[j]; v2 += vals[j];}
		}
		// cout << endl;
		// cout << "p1, p2, v1, v2 = " << p1 <<","<<p2<<","<<v1<<","<<v2<<endl;
		if (p1 != p2 || v1 == 0 || v2 == 0) return -1;
		return v1 > v2 ? v1 : v2;
	}
	
	colour[i] = 0;
	int v1 = dfs(i+1);
	colour[i] = 1;
	int v2 = dfs(i+1);
	
	return v1 > v2 ? v1 : v2;
}

int main() {
	int kases; cin >> kases;
	
	for0(kase, kases) {
		cin >> n;
		for0(i, n) cin >> vals[i];
		int val = dfs(0);
		cout << "Case #" << (kase+1) << ": ";
		if (val < 0) cout << "NO"; else cout << val;
		cout << endl;
	}
}