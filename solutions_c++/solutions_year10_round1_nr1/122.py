#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <string>
#include <sstream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cassert>
#include <ctime>
#include <cctype>

using namespace std;
typedef long long int64;
const int inf = 0x3f3f3f3f;
typedef double real;
const real eps = 1e-6;
typedef pair<int,int> pip;
#define Eo(x) { cerr << #x << " = " << (x) << endl; }

const int maxn = 64;
string a[maxn],b[maxn];

int n,k;

int dx[] = {1,1,1,0,-1,-1,-1,0};
int dy[]= {1,0,-1,-1,-1,0,1,1,};

char has(char x, int sdfsafagk){
	for (int d = 0; d < 8; d++){
		for (int i = 0;i < n; i++){
			for (int j = 0; j < n; j++) if (b[i][j] == x){
				int z = 1;
				int ay = i;
				int ax = j;
				for (int t = 1; t < k; t++){
					ay += dy[d];
					ax += dx[d];
					if (ay < 0 || ax < 0 || ay >= n || ax >= n || b[ay][ax] != x) break;
					z++;
				}
				if (z >= k) return true;
			}
		}
	}
	return 0;
}

int main(){
	int T; cin >> T;
	for (int  _ = 0; _ < T; _++){
		cin >> n >> k;
		for (int i = 0; i < n; i++){
			cin >> a[i];
			b[i] = string(a[i].size(),'.');
		}
		for (int i = 0; i < n; i++){
			int k = n-1;
			for (int j =0 ; j < n; j++){
				for (;k >= 0 && a[i][k] == '.';k--);
				if (k == -1) break;
				b[n-1-j][n-1-i] = a[i][k];
				k--;
			}
		}
		int res = has('B',k) | ((has('R',k)<<1));
		printf("Case #%d: %s\n",_+1, res == 0 ? "Neither" : res == 1 ? "Blue" : res == 2 ? "Red" : "Both");
	}
	return 0;
}

