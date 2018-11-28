#include <iostream>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <vector>
#include <stack>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <complex>
#include <algorithm>
#include <utility>
#include <cstring>

using namespace std;
int n, k;
string ini[64];
char setup[64][64];
int len[64];

bool check_horz(char c){
	// check horizontal
	for (int i = 0; i < n; i++){
		int cnt = 0;
		for (int j = 0; j < n; j++){
			if (setup[i][j] != c) {
				cnt = 0;
				continue;
			}
			cnt++;
			if (cnt >= k) return true;
		}
	}
	return false;
}

bool check_vert(char c){
	for (int i = 0; i < n; i++){
		int cnt = 0;
		for (int j = 0; j < n; j++){
			if (setup[j][i] != c) {
				cnt = 0;
				continue;
			}
			cnt++;
			if (cnt >= k) return true;
		}
	}
	return false;
}

bool check_diag(char c){
	int ii = n-1, jj = 0;
	while(jj < n){
		int cnt = 0;
		for (int pos = 0; pos < n; pos++){
			int i = pos + ii;
			int j = pos + jj;
			if (i >= n || j >= n) break;
			if (setup[i][j] != c){
				cnt = 0;
				continue;
			}
			cnt++;
			if (cnt >= k) return true;
		}	
		if (ii > 0) ii--;
		else jj++;
	}	
	
	ii = n-1, jj = n-1;
	while(jj >= 0){
		int cnt = 0;
		for (int pos = 0; pos < n; pos++){
			int i = pos + ii;
			int j = -pos + jj;
			if (i >= n || j < 0) break;
			if (setup[i][j] != c){
				cnt = 0;
				continue;
			}
			cnt++;
			if (cnt >= k) return true;
		}	
		if (ii > 0) ii--;
		else jj--;
	}
	return false;
}

int main(){
	int t; cin >> t;	
	for (int zzz = 1; zzz <= t; zzz++){
		cin >> n >> k;
		for (int i = 0; i < n; i++)
			cin >> ini[i];
		memset(len,0,sizeof(len));
		memset(setup,'.',sizeof(setup));
		for (int i = 0; i < n; i++){
			for (int j = n-1; j >= 0; j--)
				if (ini[i][j] != '.')
					setup[i][len[i]++] = ini[i][j];
		}
		/*
		for (int i = 0; i < n; i++){
			for (int j = 0; j < n; j++)
				cout << setup[i][j];
			cout << endl;
		}
		cout << endl;
		*/
		bool red = check_horz('R') || check_vert('R') || check_diag('R');
		bool blue = check_horz('B') || check_vert('B') || check_diag('B');
		
		cout << "Case #" << zzz << ": ";
		if (red && blue) cout << "Both" << endl;
		else if (red) cout << "Red" << endl;
		else if (blue) cout << "Blue" << endl;
		else cout << "Neither" << endl;
	}
	return 0;
}
