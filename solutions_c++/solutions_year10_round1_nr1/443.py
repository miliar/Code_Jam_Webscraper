#include <iostream>
#include <sstream>
#include <vector>
#include <list>
#include <map>
#include <algorithm>

#include <cmath>
#include <cstdio>

using namespace std;

bool c(int n, int kv, char **m, char b) {
	for (int i = 0; i < n; i++) {
		for (int j = 0; j <= n-kv; j++) {
			bool g = true;
			for (int k = 0; k < kv; k++) {
				if (m[i][j+k]!=b) {g=false; break; }
			}
			if(g) return true;
		}
	}

	for (int i = 0; i < n; i++) {
		for (int j = 0; j <= n-kv; j++) {
			bool g = true;
			for (int k = 0; k < kv; k++) {
				if (m[j+k][i]!=b) {g=false; break; }
			}
			if(g) return true;
		}
	}

	for (int i = 0; i <= n-kv; i++) {
		for (int j = 0; j <= n-kv; j++) {
			bool g = true;
			for (int k = 0; k < kv; k++) {
				if (m[j+k][i+k]!=b) {g=false; break; }
			}
			if(g) return true;
		}
	}

	for (int i = 0; i <= n-kv; i++) {
		for (int j = 0; j <= n-kv; j++) {
			bool g = true;
			for (int k = 0; k < kv; k++) {
				if (m[j+kv-k-1][i+k]!=b) {g=false; break; }
			}
			if(g) return true;
		}
	}

	return false;
}

void w() {
	int n,k;
	cin >> n >> k >> ws;
	char **m = new char*[n];
	for (int i = 0; i < n; i++) {
		m[i] = new char[n+3];
		cin >> m[i];
	}
	
	for (int i = 0; i < n; i++) {
		int c = n-1;
		for(int j = n-1; j >= 0; j--) {
			if (m[i][j] != '.') {
				swap(m[i][c], m[i][j]);
				c--;
			}
		}
	}

	
	bool w1 = c(n,k,m,'R');
	bool w2 = c(n,k,m,'B');
	if (!w1&&!w2) cout << "Neither";
	else if (w1&&!w2) cout << "Red";
	else if (!w1&&w2) cout << "Blue";
	else cout << "Both";

	for (int i = 0; i < n; i++) delete[] m[i];
	delete[] m;
}
int main()
{
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for (int i = 0; i < t; i++) {
		cout << "Case #" << (i+1) << ": ";
		w();
		cout << endl;
	}
	return 0;
}